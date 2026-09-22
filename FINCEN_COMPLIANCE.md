# FinCEN Compliance & Anti-Money Laundering (AML) Standards

## 1. Statutory Mandates & Regulatory Authorities
Fin Anti-Fraud Sentinel operates under the statutory authorities of:
- **The Bank Secrecy Act of 1970 (BSA), 31 U.S.C. § 5311 et seq.**
- **The USA PATRIOT Act of 2001 (Title III: International Money Laundering Abatement and Financial Anti-Terrorism Act)**
- **Financial Crimes Enforcement Network (FinCEN) Regulations (31 CFR Chapter X)**

---

## 2. Mandatory Reporting Thresholds & Protocols

### A. Currency Transaction Report (CTR) — 31 CFR § 1010.311
Financial institutions are legally obligated to file FinCEN Form 112 (CTR) for each deposit, withdrawal, exchange of currency, or other payment or transfer by, through, or to such financial institution which involves a transaction in currency of **more than $10,000**:
- Aggregate cash transactions by or on behalf of the same person during any one business day must be treated as a single transaction.
- Filing Deadline: Within **15 calendar days** following the date of the transaction.

### B. Suspicious Activity Report (SAR) — 31 CFR § 1020.320
A financial institution must file FinCEN Form 111 (SAR) for any transaction conducted or attempted by, at, or through the institution involving an aggregate of **$5,000 or more**, where the institution knows, suspects, or has reason to suspect that:
1. The transaction involves funds derived from illegal activities or is intended to hide or disguise assets derived from illegal activities.
2. The transaction is designed, whether through structuring or other means, to evade any requirements under the BSA.
3. The transaction has no business or apparent lawful purpose or is not the sort in which the particular customer would normally be expected to engage.
- Filing Deadline: Within **30 calendar days** after the date of initial detection of facts that constitute a basis for filing.

---

## 3. Smurfing & Structuring Detection Algorithm
Structuring (31 U.S.C. § 5324) occurs when an individual conducts multiple currency transactions in amounts below the $10,000 threshold specifically to evade CTR generation.

The structuring detection engine (`analyzers/structuring_detector.py`) applies a temporal clustering algorithm:
1. **Temporal Rolling Window**: Evaluates all deposit events for account $A$ across a sliding $48\text{-hour}$ window ($[t - 48h, t]$).
2. **Sub-Threshold Pattern**: Flags individual deposits $d_i \in [\$2,000, \$9,950]$.
3. **Cumulative Volume**: Computes $\sum_{i} d_i$. If $\sum d_i \ge \$10,000$ and $count(d_i) \ge 2$, an automated Structuring Alert is triggered.
4. **Geographic Diversity**: Multiple branch deposits within short time deltas elevate the priority score to **CRITICAL**.

---

## 4. Audit Trail & Confidentiality (Tipping-Off Prohibition)
- **31 U.S.C. § 5318(g)(2)**: Strict federal prohibition against disclosing to any person involved in the transaction that a SAR has been reported or considered.
- All transaction logs, scoring weights, and SAR draft narratives must be stored in encrypted, append-only ledgers and retained for a statutory minimum of **5 years**.
