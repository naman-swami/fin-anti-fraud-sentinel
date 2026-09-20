# FinSentinel — Real-Time Transaction Graph Anomaly & AML Watchdog

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Real-time anti-money laundering and transaction fraud detection agent utilizing graph topological features, synthetic identity profiling, and SAR filing generation.

## Domain Category
**Finance**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Chief AML Compliance Officer & Financial Intelligence Analyst
- **Primary Goal**: Uncover complex layering, mule account rings, and structuring patterns across cross-border payment networks to deliver FinCEN Suspicious Activity Reports.

## Skills Included
- **`graph-clustering-mule-detection`**: Identifying tightly coupled subgraphs and cyclic payment flows indicative of coordinated money mule networks.
- **`structuring-smurfing-detection`**: Detecting repeated transactions kept deliberately beneath regulatory cash transaction reporting (CTR) thresholds.
- **`fincen-sar-narrative-synthesis`**: Drafting legally compliant SAR narratives detailing suspicious transaction sequences, typologies, and subject chronologies.

## Tools Schema
- **`trace-entity-graph-lineage`**: Traverse financial entity graphs to discover common beneficiary owners, device fingerprints, and shared IP infrastructure.
- **`score-structuring-risk`**: Compute statistical deviation of deposit velocity against standard deviation of natural consumer behavior.
- **`compose-fincen-sar-filing`**: Synthesize structured financial evidence into FinCEN BSA E-Filing specification XML format.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
