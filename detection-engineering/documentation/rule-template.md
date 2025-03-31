# Sigma Rule: [Rule Name]

**Author:** Zoerab Tchahkiev  
**Creation Date:** YYYY-MM-DD  
**Last Modified:** YYYY-MM-DD  
**Status:** [experimental/stable/deprecated]

## 🎯 Rule Overview

**Purpose:** [Brief description of what the rule detects]

**MITRE ATT&CK Mapping:**
- Tactic: [Tactic name]
- Technique: [Technique ID] - [Technique name]
- Sub-technique: [Sub-technique ID] - [Sub-technique name] (if applicable)

**Target Log Sources:**
- Product: [Product name, e.g., Windows, Zeek, CloudTrail]
- Service: [Service name, if applicable]
- Category: [Log category, e.g., process_creation, network_connection]

**Severity:** [critical/high/medium/low/informational]

---

## 🛠️ Technical Details

### Rule Logic

```yaml
# Sigma rule content
title: [Rule Name]
id: [UUID]
status: experimental
description: [Description]
author: Zoerab Tchahkiev
date: YYYY/MM/DD
modified: YYYY/MM/DD
logsource:
    category: [Category]
    product: [Product]
detection:
    selection:
        [Field]: [Value]
    filter:
        [Field]: [Value to exclude]
    condition: selection and not filter
falsepositives:
    - [Known FP scenarios]
level: [medium/high]
tags:
    - attack.[tactic].[technique]
```

### Rule Explanation

| Component | Description |
|-----------|-------------|
| Selection | [Explain what the selection criteria are looking for] |
| Filter | [Explain what the filter is removing and why] |
| Condition | [Explain the logic of the condition] |

---

## 📊 Validation Details

### Test Data

```
# Sample log entry that should trigger this rule
[Sample log data]
```

### Testing Methodology

1. [Step 1 of testing process]
2. [Step 2 of testing process]
3. [Step 3 of testing process]

### False Positive Analysis

| False Positive Scenario | Mitigation Strategy |
|-------------------------|---------------------|
| [FP scenario 1] | [How to handle/filter] |
| [FP scenario 2] | [How to handle/filter] |

---

## 🌐 Context and Threat Intelligence

### Adversary Behavior
[Description of the adversary TTPs this rule is designed to detect]

### Related IOCs
- [IP/Domain/Hash/etc. if applicable]
- [IP/Domain/Hash/etc. if applicable]

### Related Rules
- [Link to related rule 1]
- [Link to related rule 2]

---

## 🔄 Tuning and Maintenance

### Version History
- **v1.0** (YYYY-MM-DD): Initial creation
- **v1.1** (YYYY-MM-DD): [Changes made]

### Tuning Considerations
- [Parameter that might need tuning]
- [Environment-specific considerations]

### Performance Impact
[Assessment of any performance considerations]

---

## 🧠 References and Resources

- [Link to research that informed this rule]
- [Link to documentation on the technique]
- [Link to blog post or other resource]

---

## 📋 Integration Notes

### SIEM Implementation
[Notes about implementation in specific SIEM platforms]

### Response Automation
[Suggestions for SOAR playbook or automated response]
