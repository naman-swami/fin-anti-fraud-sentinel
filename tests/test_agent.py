import pytest
from src.fraud_engine import AntiMoneyLaunderingEngine

def test_structuring_alert():
    engine = AntiMoneyLaunderingEngine()
    res = engine.audit_transactions([9850.0, 9900.0], account_tenure_days=10)
    assert res["suspicious_activity_flagged"] is True
    assert res["compliance_mandate"] == "FILE_FINCEN_SAR_AND_FREEZE"

def test_clean_transactions():
    engine = AntiMoneyLaunderingEngine()
    res = engine.audit_transactions([150.0, 2000.0, 500.0], account_tenure_days=200)
    assert res["suspicious_activity_flagged"] is False
