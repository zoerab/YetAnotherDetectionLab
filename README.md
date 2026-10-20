# 🧪 YetAnotherDetectionLab

A hands-on cybersecurity lab focused on threat hunting, network packet analysis, detection development, and security automation.

---

## 🔍 Purpose

This repository documents practical experiments, tools, and methodologies related to:

- 🔎 Threat hunting and adversary behaviour analysis
- 📡 Network packet analysis, protocols, and network telemetry
- 🛡️ Detection development using Sigma, YARA, Suricata, and KQL
- 🐍 Security automation and threat intelligence enrichment
- ☁️ Cloud security monitoring and detection
- 🧪 Threat simulation and detection validation
- ⚙️ Security orchestration with Cortex XSOAR

Projects are built, tested, and documented to explore practical techniques, validate detection logic, and improve investigative capabilities.

---

## 📁 Repository Structure

| Folder                         | Description                                            |
|--------------------------------|--------------------------------------------------------|
| `detection-engineering/`       | Detection rules, methodologies, and documentation      |
| &nbsp;&nbsp;└─`documentation/` | Methodology guides and templates                       |
| &nbsp;&nbsp;└─`sigma-rules/`   | Sigma detection rules for various platforms            |
| &nbsp;&nbsp;└─`suricata-rules/`| Suricata network detection rules                       |
| &nbsp;&nbsp;└─`yara-rules/`    | YARA rules for file/memory detection                   |
| &nbsp;&nbsp;└─`kql/`           | KQL detections and snippets                            |
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
| `resources/     `              | Learning resources used/worth mentioning               |
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
- [Email Auto Forwarding Global Rule Detection](detection-engineering/kql/email-redirect-detections/auto_forward_global.kql) - Detects auto-forwarding or redirect rules across all mailboxes.
- [Email Auto Forwarding User-Specific Rule Detection](detection-engineering/kql/email-redirect-detections/auto_forward_user_specific.kql) - Detects if a specific user created forwarding or redirect rules.


### Documentation & Templates

- [Detection Rule Template](detection-engineering/documentation/rule-template.md) - Standardized template for documenting detection rules
- [Hunt Report Template](threat-hunting/templates/hunt-report-template.md) - Template for documenting threat hunting exercises
- [XSOAR Playbook Template](xsoar-playbooks/xsoar-playbook-template.md) - Template for documenting Cortex XSOAR playbooks

### Packet Analysis

- [Wireshark Security Profiles](packet-analysis/wireshark/) - Custom Wireshark profiles optimized for security analysis

---

## 🧠 Skills Demonstrated

- Threat Hunting (Zeek, Suricata, JA3/JA4+, DNS tunneling, C2 detection)
- Network packet analysis and forensics
- Detection-as-Code (Sigma, YAML, Panther-style CI/CD)
- Cloud-native detection (AWS CloudTrail, Azure Sign-In logs)
- Python automation for detection logic
- Security Orchestration (Cortex XSOAR)

---

## 🌐 Background & Experience

This repository builds on my professional experience across cybersecurity, systems administration, and IT infrastructure.

- Cyber Security Analyst / Threat Hunter at Universiteit Antwerpen (2022-present)
- Security System Administrator at AP Hogeschool (2017-2022)
- ICT System Engineer, specialising in various IT fields (2007-2014)

---

## 📬 Contact & Connect

- GitHub: [zoerab](https://github.com/zoerab)
- LinkedIn: [Zoerab Tchahkiev](https://be.linkedin.com/in/zoerab)

---

<div align="center">
  <p>Licensed under <a href="LICENSE">MIT License</a></p>
</div>
