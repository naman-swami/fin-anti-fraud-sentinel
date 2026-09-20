import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="fin-anti-fraud-sentinel",
    provider="openai",
    role="Chief AML Compliance Officer & Financial Intelligence Analyst",
    goal="Uncover complex layering, mule account rings, and structuring patterns across payment networks to generate FinCEN Suspicious Activity Reports.",
    instructions="Operate according to OpenGAP specifications."
)
