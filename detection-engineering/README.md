# Detection Engineering

This directory contains detection rules, methodologies, and documentation developed as part of my detection engineering practice. The focus is on creating high-quality, well-documented detection logic across multiple platforms and rule types.

## 📁 Directory Structure

| Folder | Description |
|--------|-------------|
| `sigma-rules/` | Sigma detection rules for various platforms |
| `yara-rules/` | YARA rules for file and memory scanning |
| `suricata-rules/` | Suricata network detection rules |
| `documentation/` | Methodologies and best practices |

## 🎯 Detection Principles

All detection rules in this repository follow these core principles:

1. **Evidence-Based**: Built on observed threat actor behavior or validated techniques
2. **Well-Documented**: Include clear descriptions, logic explanations, and references
3. **MITRE Mapped**: Associated with relevant MITRE ATT&CK techniques
4. **Tested**: Validated against real or simulated data
5. **Tunable**: Include guidance on false positive handling and tuning

## 🧠 Development Methodology

Each detection rule follows this development process:

1. **Research Phase**: Study threat behavior, TTPs, and existing detection approaches
2. **Logic Development**: Craft initial detection logic with careful field selection
3. **Testing**: Validate against known-good and known-bad data
4. **Documentation**: Create comprehensive documentation including context
5. **Publication**: Add to repository with metadata and references
6. **Maintenance**: Update based on feedback and evolving threats

## 🔎 Rule Format

Sigma rules follow this structure:
```yaml
title: Descriptive Title of Detection
id: unique-uuid-for-rule
status: experimental|stable|test
description: Detailed description of what this rule detects
author: Zoerab Tchahkiev
date: YYYY/MM/DD
modified: YYYY/MM/DD
logsource:
    product: windows|linux|aws|azure
    service: specific-service
    category: log-category
detection:
    selection:
        field1: value1
        field2: value2
    condition: selection
falsepositives:
    - Known false positive scenario
level: low|medium|high|critical
tags:
    - attack.tactic
    - attack.technique
references:
    - https://reference-url
```

## 📊 Current Status

| Rule Type | Count | Status |
|-----------|-------|--------|
| Sigma | 2 | In Development |
| YARA | 0 | Planned Q2 2025 |
| Suricata | 0 | Planned Q3 2025 |

## 🧪 Integration with Threat Hunting

The detection rules in this directory are developed in concert with the threat hunting activities documented in the `threat-hunting/` directory. Many rules originated from successful hunt hypotheses that were converted into production detections.

## 📚 Resources

- [Sigma Project](https://github.com/SigmaHQ/sigma)
- [YARA Documentation](https://yara.readthedocs.io/)
- [Suricata Rules Documentation](https://suricata.readthedocs.io/en/suricata-6.0.0/rules/intro.html)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
