# Alert Correlation

## Correlation Workflow

Falco Runtime Alert
        ↓
SIEM Ingestion
        ↓
MITRE Classification
        ↓
Threat Intelligence Enrichment
        ↓
SOC Triage
        ↓
Incident Escalation

## Correlation Examples

| Event | Correlated With |
|---|---|
| Container shell execution | Privilege escalation |
| Unauthorized access | Suspicious process execution |
| Failed authentication spikes | Potential brute force |

## Objectives

- Reduce false positives
- Improve incident prioritization
- Enhance threat visibility
