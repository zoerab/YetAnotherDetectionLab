# Email Auto Forwarding Rule Detections (KQL)

This folder contains KQL detection rules to identify suspicious creation of email forwarding or redirect rules in Microsoft 365 environments. These rules are commonly abused by threat actors during Business Email Compromise (BEC) incidents.

## 1. `auto_forward_global.kql`

**Purpose**: Detects auto-forwarding or redirect rules across all mailboxes.

- **Use Case**: Detection Engineering
- **Mapped Tactic**: Exfiltration
- **Technique**: MITRE ATT&CK T1114.003
- **Data Source**: `CloudAppEvents`

## 2. `auto_forward_user_specific.kql`

**Purpose**: Detects if a specific user created forwarding or redirect rules.

- **Use Case**: Threat Hunting / VIP Monitoring
- **Supports Parameterization**: Yes (`specificUser`)
- **Data Source**: `CloudAppEvents`

