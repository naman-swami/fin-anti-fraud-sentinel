import argparse
import json
import os
from analyzers.structuring_detector import AMLTransactionAuditor

def main():
    parser = argparse.ArgumentParser(description="FinAntiFraud AML Sentinel CLI")
    parser.add_argument("--demo", action="store_true", help="Audit benchmark transaction stream")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "transactions", "sample_ledger.json")

    if args.demo:
        with open(data_file, "r") as f:
            txs = json.load(f)
        res = AMLTransactionAuditor.audit_ledger(txs)
        print("=== FIN-ANTI-FRAUD AML TRANSACTION MONITORING REPORT ===\n")
        print(f"Total Transactions Audited: {res['total_transactions_scanned']}")
        print(f"Compliance Risk Tier: {res['risk_tier']} | Active Alerts: {res['alerts_count']}\n")
        for a in res["alerts"]:
            print(f"[{a['rule_id']}] Severity: {a['severity']} | {a['title']}")
            print(f"  Account: {a.get('account_id')} | Filing Action: {a['filing_required']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
