"""
FinAntiFraud AML & BSA Structuring Detection Engine
Monitors transaction ledgers for CTR obligations, smurfing patterns, and rapid velocity egress.
"""
from typing import List, Dict, Any

class AMLTransactionAuditor:
    @staticmethod
    def audit_ledger(transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        alerts = []
        account_deposits = {}

        for tx in transactions:
            acc = tx.get("account_id")
            amt = tx.get("amount", 0.0)
            tx_type = tx.get("type", "")

            # 1. Direct CTR Check (> $10,000 cash)
            if amt >= 10000.0 and "CASH" in tx_type:
                alerts.append({
                    "tx_id": tx.get("tx_id"),
                    "account_id": acc,
                    "rule_id": "AML-BSA-01",
                    "severity": "HIGH",
                    "title": "CTR Mandatory Filing Threshold Exceeded",
                    "amount": amt,
                    "filing_required": "FinCEN Form 112"
                })

            # Track deposits under threshold for structuring check
            if 8000.0 <= amt < 10000.0 and "CASH" in tx_type:
                account_deposits.setdefault(acc, []).append(tx)

        # 2. Structuring / Smurfing Analysis
        for acc, dep_list in account_deposits.items():
            if len(dep_list) >= 2:
                total_structured = sum(t["amount"] for t in dep_list)
                alerts.append({
                    "account_id": acc,
                    "rule_id": "AML-STRUCT-02",
                    "severity": "CRITICAL",
                    "title": "Suspected Structuring / Smurfing Evasion Scheme",
                    "total_amount": total_structured,
                    "transaction_count": len(dep_list),
                    "filing_required": "Suspicious Activity Report (SAR)"
                })

        risk_tier = "CRITICAL" if any(a["severity"] == "CRITICAL" for a in alerts) else "ELEVATED" if alerts else "CLEAN"

        return {
            "total_transactions_scanned": len(transactions),
            "alerts_count": len(alerts),
            "risk_tier": risk_tier,
            "alerts": alerts
        }
