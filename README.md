# Fin Anti-Fraud & AML Sentinel

> **Bank Secrecy Act (BSA) & FinCEN Currency Transaction Monitoring System**  
> Detecting Smurfing / Structuring Patterns and Generating Automated Suspicious Activity Reports (SAR).

---

### Regulatory Rules Matrix

Under Title 31 of the Code of Federal Regulations (31 CFR Chapter X), financial institutions must monitor transaction streams for evasion tactics:

```
                      Transaction Stream Ingestion
                                   │
                   ┌───────────────┴───────────────┐
                   ▼                               ▼
       Single Deposit >= $10,000         Multiple Sub-$10k Deposits
                   │                      Within 48h Window (Sum >= $10k)
                   ▼                               ▼
      [Mandatory CTR Trigger]             [Smurfing / Structuring Flag]
       31 CFR § 1010.311                   31 CFR § 1010.314 (31 U.S.C. 5324)
                   │                               │
                   └───────────────┬───────────────┘
                                   ▼
                   Generate FinCEN Form 111 (SAR Narrative)
```

---

### Automated SAR Narrative Generation

When temporal aggregation confirms smurfing behavior across multiple branches:

```json
{
  "filing_type": "SUSPICIOUS_ACTIVITY_REPORT",
  "subject_account": "ACT-8921-X",
  "detected_pattern": "STRUCTURING_SMURFING",
  "aggregate_amount_usd": 18400.00,
  "transaction_count": 3,
  "window_hours": 36.5,
  "narrative": "Subject conducted 3 consecutive cash deposits ($9,200, $4,800, $4,400) at distinct branch locations within 36.5 hours, exhibiting clear structuring to evade Currency Transaction Reporting thresholds."
}
```

---

### Compliance Engine Execution

```bash
# Monitor sample transaction ledger
python monitor.py --demo

# Run anti-money laundering rule unit tests
pytest tests/ -v
```

Detailed statutory mandates, retention schedules, and law enforcement escalation guidelines are published in [FINCEN_COMPLIANCE.md](FINCEN_COMPLIANCE.md).
