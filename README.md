# Fin Anti-Fraud & AML Sentinel

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![RegTech](https://img.shields.io/badge/Domain-AML_BSA_Compliance-crimson.svg)](docs/fincen_bsa_guidelines.md)
[![Standard](https://img.shields.io/badge/Regulation-FinCEN_31CFR-darkblue.svg)](docs/fincen_bsa_guidelines.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An enterprise anti-money laundering (AML) and BSA transaction monitoring system detecting structuring/smurfing evasions, CTR obligations, and generating SAR filing advisories.

```
                    ┌─────────────────────────┐
                    │ Raw Transaction Ledger  │
                    │   (Amounts & Timestamps)│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  analyzers/structuring  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  CTR Check (>$10k)  │         │ Smurfing Evaluation │
      │   (FinCEN Form 112) │         │  (SAR Recommendation)│
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Compliance Action Gate  │
                    │ (FREEZE / REPORT / PASS)│
                    └─────────────────────────┘
```

## Features

- **Structuring Detection**: Identifies accounts executing multiple deposits between $8,000–$9,999 to evade CTR thresholds.
- **Mandatory CTR Flags**: Immediately highlights single currency operations $\ge \$10,000$.
- **Audit-Ready Evidence**: Maps every flag directly to 31 U.S.C. § 5324 statutory authorities.

## Directory Structure

```
fin-anti-fraud-sentinel/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint AML audit provenance
├── analyzers/
│   └── structuring_detector.py      # Smurfing & CTR evaluation engine
├── rules/
│   └── bsa_aml_rules.yaml           # FinCEN compliance rule thresholds
├── fixtures/
│   └── transactions/
│       └── sample_ledger.json       # Benchmark transaction streams
├── docs/
│   └── fincen_bsa_guidelines.md     # Statutory legal reference
├── tests/
│   └── test_agent.py                # AML rule verification suite
├── main.py                          # Compliance CLI
└── requirements.txt
```

## Quick Start

```bash
# Run AML audit test suite
pytest tests/ -v

# Audit benchmark transaction ledger
python main.py --demo
```
