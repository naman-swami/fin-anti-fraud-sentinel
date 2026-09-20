# Explainability — fin-anti-fraud-sentinel

## Decision Reasoning
FinSentinel constructs directed graph models of funds flow velocity, detecting cyclical graph closures, structuring just beneath $10k reporting limits, and synthetic identity markers.

## Data Sources and Inputs Used
Core banking transaction ledgers, OFAC Specially Designated Nationals sanctions lists, device fingerprint telemetry, and FinCEN BSA filing guidelines.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, fin-anti-fraud-sentinel assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, fin-anti-fraud-sentinel will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, fin-anti-fraud-sentinel explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
fin-anti-fraud-sentinel actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Legal Asset Seizure: Freezes internal transfers according to bank policy but cannot seize assets without law enforcement court order.
- Criminal Prosecution: Does not file criminal indictments; acts as intelligence provider to FinCEN and law enforcement.
- Cash In-Hand: Cannot trace physical paper cash once withdrawn from an ATM.
- Sovereign Sanctions Policy: Does not unilaterally establish national foreign policy sanctions.

## Uncertainty Quantification Approach
When corporate ultimate beneficial ownership (UBO) structures terminate in non-cooperative offshore secrecy jurisdictions, FinSentinel elevates risk tier to maximum and mandates manual enhanced due diligence.
