from pathlib import Path
import json

from crewai import Agent


ROOT = Path(__file__).resolve().parents[1]


def load_persona(path):
    with open(ROOT / path, encoding="utf-8") as f:
        return json.load(f)


def create_marketing_agent():
    persona = load_persona("personas/marketing_manager.json")

    agent = Agent(
        role=persona["role"],
        goal=", ".join(persona["goals"]),
        backstory="A strategic marketing leader focused on product growth.",
    )

    return agent
