import json
import argparse
from src.fraud_engine import AntiMoneyLaunderingEngine

def main():
    parser = argparse.ArgumentParser(description="FinSentinel AML Fraud Detection CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated transaction structuring audit")
    args = parser.parse_args()

    engine = AntiMoneyLaunderingEngine()
    sample_txs = [9800.0, 9750.0, 9900.0, 450.0]
    report = engine.audit_transactions(sample_txs, account_tenure_days=14)
    print("="*60)
    print(" FINSENTINEL AML TRANSACTION AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
