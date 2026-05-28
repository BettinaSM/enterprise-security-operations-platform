# 🛡️ Enterprise Security Operations Platform

Unified Enterprise Security Operations Platform focused on:

- SIEM & Security Monitoring
- Detection Engineering
- Threat Intelligence
- UEBA & Risk Analysis
- MITRE ATT&CK
- IAM & Access Governance
- SOAR Automation
- Compliance & Audit
- Hybrid Infrascture Security
- Cloud & Kubernetes Monitoring

Built with Python + Streamlit + Ansible for enterprise security operations, auditing, automation and detection engineering simulations.

---

# 🚀 Core Features

### Operating Systems

* Linux monitoring
* AIX monitoring
* Windows monitoring

### Cloud Platforms

* AWS CloudTrail
* Azure Entra Sign-In Logs
* GCP Audit Logs
* Oracle Cloud Audit
* IBM Cloud Activity Tracker

### Container & Runtime Security

* Kubernetes audit visibility
* Runtime activity monitoring
* Container event ingestion

---

# 🧠 Detection Engineering

* Sigma-like detections
* YAML-based detections
* IOC matching engine
* MITRE ATT&CK mapping
* Detection severity scoring
* Threat correlation engine
* Lateral movement detection
* UEBA anomaly detection

---

# 🛡️ Threat Intelligence

* IOC enrichment
* Threat feed ingestion
* CVE enrichment
* Threat correlation
* IOC severity analysis
* Threat chain simulation

---

# 👥 IAM & Access Governance

* User audit automation
* LDAP audit automation
* Privileged access review
* Sudoers analysis
* Group membership analysis
* Root/admin activity monitoring
* Access baseline validation
* Identity governance simulations

---

# ⚙️ SOAR Automation

* Ansible playbook execution
* Automated audit collection
* Temporary inventory generation
* Dynamic server targeting
* Security response orchestration
* Evidence collection workflows

---

# 📋 Compliance & Audit

### Framework Visibility

* ISO27001
* NIST
* CIS Controls
* PCI-DSS

### Audit Capabilities

* User privilege auditing
* Access governance reviews
* Baseline validation
* Infrastructure inventory tracking
* Security evidence generation
* Executive PDF reports

---

# 📊 SOC Capabilities

* SIEM correlation
* Incident management
* Threat hunting console
* Executive dashboards
* SOC analytics
* MITRE ATT&CK heatmaps
* Real-time syslog monitoring

---

# 🏗️ Enterprise Architecture

```text
Linux / AIX / Windows
        ↓
Cloud Providers
(AWS / Azure / GCP / OCI / IBM)
        ↓
Kubernetes Runtime Security
        ↓
Collectors & Log Parsers
        ↓
Detection Engine
        ↓
Threat Intelligence
        ↓
MITRE ATT&CK Correlation
        ↓
UEBA & Risk Scoring
        ↓
SIEM Analytics
        ↓
SOC Dashboard
        ↓
Incident Response
        ↓
SOAR Automation
        ↓
Audit & Compliance Reporting
```

---

# ⚙️ Technologies

## Backend

* Python
* FastAPI
* SQLite

## Security & Automation

* Ansible
* YAML
* JWT
* MITRE ATT&CK

## Visualization

* Streamlit
* Plotly
* Pandas

## Infrastructure

* Docker
* Docker Compose

---

# 📂 Project Structure

```text
dashboard-app/
├── agents/
│   ├── linux/
│   ├── aix/
│   ├── windows/
│   ├── aws/
│   ├── azure/
│   ├── gcp/
│   ├── oracle-cloud/
│   ├── ibm-cloud/
│   └── kubernetes/
│
├── ansible/
│   ├── inventories/
│   ├── playbooks/
│   └── reports/
│
├── collectors/
├── configs/
├── detections/
├── parsers/
├── reporting/
├── sections/
├── services/
├── security/
├── logs/
├── database/
├── api/
└── app.py
```

---

# 🐳 Docker Deployment

```bash
docker compose up --build
```

---

# ▶️ Local Execution

```bash
pip install -r requirements.txt

streamlit run dashboard-app/app.py
```

---

# 🔐 Authentication & RBAC

Current implementation includes:

* Simulated RBAC
* Session management
* JWT support
* Role-based authentication model

Planned improvements:

* LDAP integration
* Active Directory integration
* Azure Entra ID SSO
* OAuth2 / OpenID Connect
* MFA support
* Password hashing
* Vault/Secrets integration
* Enterprise IAM federation

---

# 🎯 MITRE ATT&CK Coverage

* Initial Access
* Execution
* Persistence
* Privilege Escalation
* Defense Evasion
* Credential Access
* Discovery
* Lateral Movement
* Collection
* Exfiltration

---

# 📈 Roadmap

## SOC & SIEM

* [ ] Elastic integration
* [ ] Splunk integration
* [ ] Real-time syslog ingestion
* [ ] Sigma correlation engine

## IAM & Governance

* [ ] Full LDAP connector
* [ ] Active Directory auditing
* [ ] PAM integration
* [ ] Access certification workflows

## Detection Engineering

* [ ] YARA integration
* [ ] AI-assisted detections
* [ ] Behavioral correlation engine
* [ ] Threat simulation engine

## SOAR

* [ ] Automated remediation
* [ ] Incident workflows
* [ ] Slack/Teams integration
* [ ] Case management

## Cloud Security

* [ ] CSPM integrations
* [ ] Multi-cloud posture analysis
* [ ] Kubernetes RBAC analysis

---

# ⚠️ Disclaimer

This platform is intended for:

* educational purposes
* security engineering practice
* portfolio demonstrations
* enterprise security simulations
* defensive cybersecurity research

No offensive capabilities are included.

---

# 👩‍💻 Author

Developed by Bettina Meirelles

Cybersecurity | Detection Engineering | SIEM | IAM | Cloud Security | DevSecOps | SOAR | Enterprise Infrastructure


