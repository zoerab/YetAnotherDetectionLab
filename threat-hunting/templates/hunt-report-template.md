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

---

## 🔍 Methodology

### Step 1: [Initial Analysis]
[Description of initial approach and queries/filters used]

```
# Example code or query
zeek-cut ts id.orig_h id.resp_h id.resp_p < conn.log | grep -E "PORT|IP"
```

### Step 2: [Secondary Analysis]
[Description of follow-up approach based on initial findings]

### Step 3: [Deep Dive]
[Description of focused analysis on specific artifacts]

---

## 🔎 Key Findings

### Network Indicators
| Indicator | Type | Description | Confidence |
|-----------|------|-------------|------------|
| 1.2.3.4   | IP   | C2 Server   | High       |
| evil.com  | Domain | Phishing Site | Medium  |

### Behavioral Indicators
- [Description of suspicious behavioral pattern 1]
- [Description of suspicious behavioral pattern 2]

### JA3/JA4+ Fingerprints
| Hash | Client/Server | Associated Process | Context |
|------|--------------|-------------------|---------|
| `7e7b...` | Client | chrome.exe | TLS to C2 |

### Timeline of Activity
- **[Timestamp]**: [Event description]
- **[Timestamp]**: [Event description]

---

## 📊 Visualizations

### Traffic Pattern
[Insert visualization or link to visualization file]

### Beaconing Analysis
[Insert visualization or link to visualization file]

---

## 🔄 Detection Opportunities

### Proposed Sigma Rule
```yaml
title: [Rule Name]
id: [UUID]
status: experimental
description: [Description]
author: Zoerab Tchahkiev
date: YYYY/MM/DD
logsource:
    category: [Category]
    product: [Product]
detection:
    selection:
        [Field]: [Value]
    condition: selection
falsepositives:
    - [Known FP scenarios]
level: [medium/high]
tags:
    - attack.[tactic].[technique]
```

### Enrichment Opportunities
- [Enrichment idea 1]
- [Enrichment idea 2]

---

## 🧠 Lessons Learned

- [Key insight 1]
- [Key insight 2]
- [Key insight 3]

---

## 📎 References

- [Link to relevant article/blog/research]
- [Link to relevant documentation]
