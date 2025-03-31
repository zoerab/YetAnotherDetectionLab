# 🧪 YetAnotherDetectionLab

Welcome to my detection engineering & threat hunting lab — a living portfolio that documents my journey from on-prem to cloud-native detection engineering and threat hunting.

---

## 🔍 Purpose

This repo showcases my work in:

- 📦 Detection rule creation (Sigma, YARA, Suricata)
- 🐍 Python automation for threat detection & enrichment
- ⚙️ Cortex XSOAR playbook development
- ☁️ Cloud-native threat detection and response
- 🧪 Real-world threat simulation and hunting

Each project is **built, tested, and documented** as part of my transition into a **Cloud Threat Detection Engineer** role.

---

## 📁 Repository Structure

| Folder                         | Description                                            |
|--------------------------------|--------------------------------------------------------|
| `detection-engineering/`       | Detection rules, methodologies, and documentation      |
| &nbsp;&nbsp;└─`documentation/` | Methodology guides and templates                       |
| &nbsp;&nbsp;└─`sigma-rules/`   | Sigma detection rules for various platforms            |
| &nbsp;&nbsp;└─`suricata-rules/`| Suricata network detection rules                       |
| &nbsp;&nbsp;└─`yara-rules/`    | YARA rules for file/memory detection                   |
| `automation/`                  | Scripts, playbooks, and CI/CD configurations           |
| &nbsp;&nbsp;└─`scripts/`       | Python scripts for security automation                 |
| &nbsp;&nbsp;└─`playbooks/`     | Automation playbook definitions                        |
| &nbsp;&nbsp;└─`ci-cd/`         | CI/CD pipeline configurations                          |
| `cloud-security/`              | Cloud-native security detection and response           |
| &nbsp;&nbsp;└─`aws/`           | AWS-specific detection rules and tools                 |
| &nbsp;&nbsp;└─`azure/`         | Azure-specific detection rules and tools               |
| &nbsp;&nbsp;└─`gcp/`           | GCP-specific detection rules and tools                 |
| &nbsp;&nbsp;└─`runtime/`       | Runtime security tools and configurations              |
| `packet-analysis/`             | Network packet analysis tools and methods              |
| &nbsp;&nbsp;└─`wireshark/`     | Wireshark profiles and configurations                  |
| &nbsp;&nbsp;└─`zeek/`          | Zeek scripts and log analysis                          |
| &nbsp;&nbsp;└─`pcaps/`         | PCAP analysis methodologies (no actual PCAPs)          |
| &nbsp;&nbsp;└─`stratoshark/`   | Cloud-native packet analysis                           |
| `threat-hunting/`              | Threat hunting reports, methodologies, and templates   |
| &nbsp;&nbsp;└─`hunt-reports/`  | Documented threat hunting exercises                    |
| &nbsp;&nbsp;└─`methodologies/` | Hunting methodologies and frameworks                   |
| &nbsp;&nbsp;└─`templates/`     | Templates for hunt planning and reporting              |
| `xsoar-playbooks/`             | Cortex XSOAR playbooks for automation and response     |

---

## 🚀 Latest Projects

### Detection Engineering

- [Suspicious PowerShell Download - Script Block Logging](detection-engineering/sigma-rules/Windows/suspicious_powershell_download_scriptblock.yml) - Detects System.Net.WebClient downloads via Script Block Logging
- [Suspicious PowerShell Download - Classic Event Logs](detection-engineering/sigma-rules/Windows/suspicious_powershell_download_classic.yml) - Similar detection for classic PowerShell logs

### Documentation & Templates

- [Detection Rule Template](detection-engineering/documentation/rule-template.md) - Standardized template for documenting detection rules
- [Hunt Report Template](threat-hunting/templates/hunt-report-template.md) - Template for documenting threat hunting exercises
- [XSOAR Playbook Template](xsoar-playbooks/xsoar-playbook-template.md) - Template for documenting Cortex XSOAR playbooks

### Packet Analysis

- [Wireshark Security Profiles](packet-analysis/wireshark/) - Custom Wireshark profiles optimized for security analysis

---

## 🧠 Skills Demonstrated

- Detection-as-Code (Sigma, YAML, Panther-style CI/CD)
- Threat Hunting (Zeek, Suricata, JA3/JA4+, DNS tunneling, C2 detection)
- Cloud-native detection (AWS CloudTrail, Azure Sign-In logs)
- Python automation for detection logic
- Security Orchestration (Cortex XSOAR)
- Network packet analysis and forensics

---

## 🗓️ Roadmap (Apr 2025 → Mar 2026)

This portfolio follows a structured quarterly roadmap **(subject to change)**:

- **Q1 (Apr-Jun)**: DE&TH Core – rules, PCAPs, enrichment scripts
- **Q2 (Jul-Sep)**: Detection Automation – tuning + pipelines
- **Q3 (Oct-Dec)**: Cloud Bridge – Sigma for cloud, MITRE cloud mapping
- **Q4 (Jan-Mar)**: Cloud Specialization – detection-as-code, threat sims, final portfolio polish

---

## 🌐 Background & Experience

The work in this repository leverages my professional background as:

- Cyber Security Analyst at Universiteit Antwerpen (2022-present)
- Security System Administrator at AP Hogeschool (2017-2022)
- ICT System Engineer specializing in various IT fields (2007-2014)

My career transition builds on strong foundations in Threat Hunting, Network Engineering, Endpoint Security Management, and Threat Detection.

---

## 📬 Contact & Connect

- GitHub: [zoerab](https://github.com/zoerab)
- LinkedIn: [Zoerab Tchahkiev](https://be.linkedin.com/in/zoerab)

---

<div align="center">
  <p>Licensed under <a href="LICENSE">MIT License</a></p>
</div>
