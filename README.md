# 🛡️ Enterprise Security Operations Platform

Unified Enterprise Security Operations Platform focused on:

- SIEM
- Detection Engineering
- Threat Intelligence
- UEBA
- MITRE ATT&CK
- Cloud Security
- Kubernetes Runtime Security
- SOC Operations
- Incident Response
- SOAR Automation

Built with Python + Streamlit for enterprise security monitoring simulations.

---

# 🚀 Features

## Security Monitoring
- Linux monitoring
- AIX monitoring
- Windows monitoring
- Kubernetes runtime visibility
- Cloud security visibility

## Detection Engineering
- Sigma-like detections
- IOC matching
- MITRE ATT&CK mapping
- YAML detection rules
- Threat scoring engine

## Threat Intelligence
- IOC enrichment
- Threat severity analysis
- Attack chain simulation

## SOC Operations
- SIEM correlation
- Incident management
- SOC analyst queue
- Threat hunting console

## Governance & Compliance
- ISO27001
- NIST
- CIS Controls
- PCI-DSS

---

# 🏗️ Architecture

```text
Linux / AIX / Windows
        ↓
Cloud Providers
(AWS / Azure / GCP / OCI / IBM)
        ↓
Kubernetes Runtime Monitoring
        ↓
Detection Engine
        ↓
Threat Intelligence
        ↓
MITRE ATT&CK Mapping
        ↓
SIEM Correlation
        ↓
SOC Dashboard
        ↓
Incident Response
        ↓
SOAR Automation
```

---

# ⚙️ Technologies

- Python
- Streamlit
- Pandas
- Plotly
- YAML
- JSON
- Docker

---

# 📂 Project Structure

```text
dashboard-app/
├── agents/
├── configs/
├── detections/
├── logs/
├── parsers/
├── simulations/
├── app.py
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

# 🎯 MITRE ATT&CK Coverage

- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement

---

# 🛣️ Roadmap

- [ ] AI SOC Analyst
- [ ] Real-time IOC feeds
- [ ] YARA integration
- [ ] Sigma correlation engine
- [ ] Elastic/Splunk integrations
- [ ] Multi-tenant SOC
- [ ] RBAC support
- [ ] API integrations

---

Authentication currently uses a simulated RBAC model with hardcoded credentials for demonstration and portfolio purposes.

Future improvements planned:

* LDAP / Active Directory integration
* Azure Entra ID SSO
* OAuth2 / OpenID Connect
* JWT authentication
* Password hashing
* Streamlit Secrets / Vault integration
* Role-based session management

---

# 👩‍💻 Author

Developed by Bettina Meirelles

Cybersecurity | Detection Engineering | Cloud Security | SIEM | DevSecOps
