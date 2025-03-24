# 🧠 Sigma Rules – Detection Engineering

This directory contains Sigma rules I’ve written, tested, or customized as part of my detection engineering work. Rules are organized by platform (e.g., Windows, Linux, Cloud).

---

## 📁 Structure

| Folder     | Description                         |
|------------|-------------------------------------|
| `windows/` | Sigma rules for Windows logs        |
| `linux/`   | (TBD) Linux-based detections        |
| `cloud/`   | (TBD) Cloud-native detections (AWS, Azure, GCP) |

---

## ✅ Rule Development Principles

- Based on **real threat behaviors**
- Mapped to **MITRE ATT&CK**
- Tested with `sigma-cli` or aligned to known log sources
- Written for **clarity and reuse** in real environments

---

## 🧪 Currently Included (Windows)

| Rule File | Description | MITRE | Logsource |
|-----------|-------------|--------|------------|
| `suspicious_powershell_download_scriptblock.yml` | Detects `System.Net.WebClient` downloads via Script Block Logging | `T1059.001` | `windows/ps_script` |
| `suspicious_powershell_download_classic.yml` | Detects same behavior via classic PowerShell logs | `T1059.001` | `windows/ps_classic_start` |

---

## 🧰 Tools

All rules are compatible with:

- [Sigma CLI](https://github.com/SigmaHQ/sigma-cli)
- Sigma-to-Splunk / Sigma-to-Elastic converters
- `sigma convert -t x` for detection-as-code pipelines

---

> These rules are part of a progressive portfolio to transition from Detection Engineering & Threat Hunting to Cloud Threat Detection.
