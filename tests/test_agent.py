import os
import json
import pytest
from analyzers.structuring_detector import AMLTransactionAuditor

def test_ctr_mandatory_alert():
    txs = [{"tx_id": "T1", "account_id": "A1", "amount": 12000.0, "type": "CASH_DEPOSIT"}]
    res = AMLTransactionAuditor.audit_ledger(txs)
    assert res["alerts_count"] == 1
    assert res["alerts"][0]["rule_id"] == "AML-BSA-01"

def test_structuring_smurfing_alert():
    txs = [
        {"tx_id": "T1", "account_id": "A2", "amount": 9200.0, "type": "CASH_DEPOSIT"},
        {"tx_id": "T2", "account_id": "A2", "amount": 9400.0, "type": "CASH_DEPOSIT"}
    ]
    res = AMLTransactionAuditor.audit_ledger(txs)
    assert res["risk_tier"] == "CRITICAL"
    rules = [a["rule_id"] for a in res["alerts"]]
    assert "AML-STRUCT-02" in rules

def test_benchmark_fixture_detection():
    data_file = os.path.join(os.path.dirname(__file__), "..", "fixtures", "transactions", "sample_ledger.json")
    with open(data_file, "r") as f:
        txs = json.load(f)
    res = AMLTransactionAuditor.audit_ledger(txs)
    assert res["alerts_count"] >= 2
