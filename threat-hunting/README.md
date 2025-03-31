# Threat Hunting

This directory contains threat hunting methodologies, reports, and templates developed as part of my proactive threat detection practice. The focus is on hypothesis-driven hunting across network, endpoint, and cloud environments.

## 📁 Directory Structure

| Folder | Description |
|--------|-------------|
| `hunt-reports/` | Documented threat hunting exercises and findings |
| `methodologies/` | Hunting methodologies and frameworks |
| `templates/` | Templates for hunt planning and reporting |

## 🎯 Hunting Principles

All threat hunting activities in this repository follow these core principles:

1. **Hypothesis-Driven**: Begin with a specific hypothesis about adversary behavior
2. **Data-Informed**: Leverage relevant data sources to test the hypothesis
3. **TTP-Focused**: Target specific adversary tactics, techniques, and procedures
4. **Well-Documented**: Document methodology, findings, and lessons learned
5. **Outcome-Oriented**: Generate actionable results (IOCs, detection rules, etc.)

## 🧠 Hunting Methodology

Each hunt follows this structured process:

1. **Hypothesis Formation**: Develop a testable hypothesis based on threat intelligence
2. **Data Collection**: Identify and gather relevant data sources
3. **Analysis**: Apply analytical techniques to test the hypothesis
4. **Validation**: Confirm or refute the hypothesis with evidence
5. **Documentation**: Document findings, evidence, and recommendations
6. **Operationalization**: Convert findings into detection rules or response actions

## 📊 Hunt Report Format

Hunt reports follow this structure:

```markdown
# Threat Hunt Report: [Title]

**Date:** YYYY-MM-DD  
**Author:** Zoerab Tchahkiev  
**Hunt ID:** HUNT-[YYYYMMnn]

## 🎯 Hunt Summary

**Hypothesis:** [Brief statement of what you're looking for and why]

**Data Sources:**
- PCAP: [Source and timeframe]
- Zeek Logs: [Types and timeframe]
- [Other Sources]

**Tools Used:**
- [Tool 1]
- [Tool 2]
- [Tool 3]

**TTP Mapping:**
- MITRE ATT&CK: [Relevant techniques]
- [Optional] MITRE Cloud Matrix: [Relevant techniques]

## 🔍 Methodology

### Step 1: [Initial Analysis]
[Description of approach and queries]

### Step 2: [Secondary Analysis]
[Description of follow-up approach]

### Step 3: [Deep Dive]
[Description of focused analysis]

## 🔎 Key Findings

### Network Indicators
| Indicator | Type | Description | Confidence |
|-----------|------|-------------|------------|
| 1.2.3.4   | IP   | C2 Server   | High       |

### Behavioral Indicators
- [Description of suspicious behavioral pattern]

## 📊 Visualizations

[Insert visualizations]

## 🔄 Detection Opportunities

[Proposed detection rules]

## 🧠 Lessons Learned

- [Key insight 1]
- [Key insight 2]
```

## 🧪 Current Hunt Status

| Hunt Category | Count | Status |
|---------------|-------|--------|
| Network-based | 0 | Planned for Q1 2025 |
| Endpoint-based | 0 | Planned for Q2 2025 |
| Cloud-based | 0 | Planned for Q3 2025 |

## 🔎 Hunting Focus Areas

### Q1 2025: Network-Focused Hunts
- DNS tunneling and anomalies
- JA3/JA4+ TLS fingerprinting
- Beaconing detection
- HTTP anomaly analysis

### Q2 2025: Anomaly Detection Hunts
- Statistical outlier analysis
- Credential usage patterns
- Process execution anomalies
- Account and identity anomalies

### Q3-Q4 2025: Cloud Environment Hunts
- IAM privilege escalation
- AWS CloudTrail anomalies
- Azure Sign-In behavioral analysis
- Container runtime anomalies

## 📚 Resources

- [SANS Hunt Evil Paper](https://www.sans.org/white-papers/hunt-evil/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Sqrrl Threat Hunting Reference](https://www.threathunting.net/files/framework-for-threat-hunting-whitepaper.pdf)
- [Zeek Documentation](https://docs.zeek.org/)
