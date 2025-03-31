# Cloud Security

This directory contains cloud security detection rules, methodologies, and tooling for AWS, Azure, and GCP environments. The focus is on cloud-native threat detection with special attention to IAM, infrastructure, and runtime security.

## 📁 Directory Structure

| Folder | Description |
|--------|-------------|
| `aws/` | AWS-specific detection rules and methodologies |
| `azure/` | Azure-specific detection rules and methodologies |
| `gcp/` | GCP-specific detection rules and methodologies |
| `runtime/` | Container and runtime security components |

## ☁️ Cloud Security Approach

The cloud security components in this repository follow these principles:

1. **Cloud-Native**: Leveraging cloud-specific logs and APIs
2. **IAM-Focused**: Emphasis on identity and access management risks
3. **Multi-Cloud**: Consistent approaches across AWS, Azure, and GCP
4. **Detection-as-Code**: Implementing detection logic as code
5. **Runtime Visibility**: Integrating container and runtime security

## 🔐 AWS Security Components

AWS security detection and response:

1. **CloudTrail Analysis**: Detection rules for CloudTrail logs
2. **GuardDuty Enhancement**: Custom detection to enhance GuardDuty
3. **IAM Security**: Focus on identity and privilege misuse
4. **S3 Security**: Object storage security monitoring
5. **VPC Traffic**: Network traffic analysis in AWS environments

### Current AWS Components

| Component | Purpose | Status |
|-----------|---------|--------|
| CloudTrail Sigma Rules | Detection rules for CloudTrail logs | Planned Q3 2025 |
| IAM Access Analyzer | Custom IAM analysis techniques | Planned Q3 2025 |
| CloudGoat Scenarios | Documented attack simulations | Planned Q4 2025 |

## 🛡️ Azure Security Components

Azure security detection and response:

1. **Sign-In Analysis**: Detection of suspicious authentication
2. **Azure AD Monitoring**: Identity security in Azure AD
3. **Microsoft 365 Security**: Cloud service security monitoring
4. **Azure Sentinel**: Custom detections for Sentinel
5. **KQL Queries**: Advanced hunting queries

### Current Azure Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Sign-In Sigma Rules | Detection rules for Azure Sign-In logs | Planned Q3 2025 |
| AAD Anomaly Detection | Identity-based anomaly detection | Planned Q3 2025 |
| KQL Hunt Queries | Threat hunting queries for Azure | Planned Q4 2025 |

## 🔒 GCP Security Components

GCP security detection and response:

1. **Cloud Audit Logs**: Detection rules for audit logs
2. **IAM Analysis**: Identity and access monitoring
3. **GKE Security**: Kubernetes security monitoring
4. **Cloud Functions**: Serverless security monitoring
5. **Security Command Center**: Custom detection rules

### Current GCP Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Audit Log Sigma Rules | Detection rules for GCP Audit Logs | Planned Q4 2025 |
| IAM Role Analysis | Custom IAM analysis techniques | Planned Q4 2025 |

## 🐳 Runtime Security

Container and runtime security:

1. **Falco Rules**: Custom Falco detection rules
2. **Sysdig Configuration**: Sysdig security monitoring
3. **Container Analysis**: Container security monitoring
4. **Runtime Detection**: Runtime behavior analysis

### Current Runtime Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Falco Rules | Custom runtime detection rules | Planned Q4 2025 |
| Sysdig Setup | Configuration for Sysdig security | Planned Q4 2025 |

## 🧪 Attack Simulation

Cloud attack simulation and validation:

1. **CloudGoat**: AWS-focused attack scenarios
2. **Stratus Red Team**: Multi-cloud attack simulation
3. **Custom Scenarios**: Tailored attack simulations
4. **Detection Validation**: Validating detection capabilities

## 📊 MITRE ATT&CK Mapping

All cloud security components are mapped to the MITRE ATT&CK Cloud Matrix:

1. **Technique Coverage**: Mapping detection to specific techniques
2. **Gap Analysis**: Identifying coverage gaps
3. **Detection Strategy**: Using ATT&CK to guide detection development

## 📚 Resources

- [AWS Security Documentation](https://docs.aws.amazon.com/security/)
- [Azure Security Documentation](https://docs.microsoft.com/en-us/azure/security/)
- [GCP Security Documentation](https://cloud.google.com/security)
- [MITRE ATT&CK Cloud Matrix](https://attack.mitre.org/matrices/enterprise/cloud/)
- [Falco Documentation](https://falco.org/docs/)
