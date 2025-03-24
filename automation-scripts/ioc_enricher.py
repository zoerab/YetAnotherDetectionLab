"""
ioc_enricher.py

Created by: Zoerab
Created on: 2025-03-24
Version: 1.1
License: MIT

Description:
    Enrich a list of IP addresses using threat intelligence APIs:
    - VirusTotal
    - AbuseIPDB
    - OTX AlienVault

    Outputs color-coded tables using the Rich library.

Changelog:
    v1.0 (2025-03-24) - Initial release: IP enrichment from VT, AbuseIPDB, OTX
    v1.1 (2025-03-24) - Added color-coded Rich table output for visibility

To Do:
    - Add support for domain and hash enrichment
    - Add JSON export option for results
    - Add caching to avoid redundant API hits
    - Use configfile for API storage in case no API environment variables found(?)

Usage:
    $ export VT_API_KEY="..."
    $ export ABUSEIPDB_API_KEY="..."
    $ export OTX_API_KEY="..."
    $ python3 ioc_enricher.py

Requirements:
    - Python 3.8+
    - rich
    - requests
"""

import os
import requests
import time
from rich.console import Console
from rich.table import Table
from rich import box
from rich.style import Style

# Initialize Rich console
console = Console()

# Load API keys from environment variables
VT_API_KEY = os.getenv("VT_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
OTX_API_KEY = os.getenv("OTX_API_KEY")

INPUT_FILE = "input_iocs.txt"


def enrich_with_virustotal(ioc):
    headers = {"x-apikey": VT_API_KEY}
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        return {
            "VT_harmless": stats.get("harmless", 0),
            "VT_malicious": stats.get("malicious", 0),
        }
    return {"VT_error": "Error or Not Found"}


def enrich_with_abuseipdb(ioc):
    headers = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ioc, "maxAgeInDays": "90"}
    response = requests.get(
        "https://api.abuseipdb.com/api/v2/check", headers=headers, params=params
    )
    if response.status_code == 200:
        data = response.json()["data"]
        return {
            "AbuseScore": data.get("abuseConfidenceScore", 0),
            "Country": data.get("countryCode", "N/A"),
        }
    return {"AbuseIPDB_error": "Error or Not Found"}


def enrich_with_otx(ioc):
    headers = {"X-OTX-API-KEY": OTX_API_KEY}
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ioc}/general"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "OTX_reputation": data.get("reputation", 0),
            "OTX_pulses": len(data.get("pulse_info", {}).get("pulses", [])),
        }
    return {"OTX_error": "Error or Not Found"}


def is_ip(ioc):
    return "." in ioc and ":" not in ioc


def color_value(value, field):
    if isinstance(value, int):
        if field in ["VT_malicious", "AbuseScore", "OTX_reputation"]:
            if value >= 20:
                return f"[bold red]{value}[/]"
            elif value >= 10:
                return f"[yellow]{value}[/]"
            else:
                return f"[green]{value}[/]"
        if field in ["VT_harmless"]:
            if value >= 10:
                return f"[green]{value}[/]"
            else:
                return f"[dim]{value}[/]"
    return str(value)


def main():
    if not all([VT_API_KEY, ABUSEIPDB_API_KEY, OTX_API_KEY]):
        console.print(
            "[red bold]❌ Missing one or more API keys. Set VT_API_KEY, ABUSEIPDB_API_KEY, and OTX_API_KEY.[/]"
        )
        return

    if not os.path.exists(INPUT_FILE):
        console.print(f"[red bold]❌ Input file '{INPUT_FILE}' not found.[/]")
        return

    with open(INPUT_FILE, "r") as f:
        iocs = [line.strip() for line in f if line.strip()]

    for ioc in iocs:
        console.rule(f"[bold cyan]🔍 Enriching: {ioc}")
        if not is_ip(ioc):
            console.print("[yellow]⚠️ Skipping non-IP IOCs for now.[/]")
            continue

        vt_data = enrich_with_virustotal(ioc)
        abuse_data = enrich_with_abuseipdb(ioc)
        otx_data = enrich_with_otx(ioc)

        result = {**vt_data, **abuse_data, **otx_data}

        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)

        table.add_column("Field")
        table.add_column("Value")

        for k, v in result.items():
            table.add_row(k, color_value(v, k))

        console.print(table)
        time.sleep(1)  # Respect API rate limits


if __name__ == "__main__":
    main()
