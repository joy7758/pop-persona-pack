import json

from crewai import Agent, Task, Crew


def load_persona(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_agent_from_persona(path: str, backstory: str) -> Agent:
    persona = load_persona(path)
    return Agent(
        role=persona["role"],
        goal="; ".join(persona["goals"]),
        backstory=backstory,
        verbose=True,
    )


def build_crew() -> Crew:
    marketing_agent = create_agent_from_persona(
        "personas/marketing_manager.json",
        "A strategic marketing leader focused on product growth, messaging, and launch planning.",
    )

    engineer_agent = create_agent_from_persona(
        "personas/software_engineer.json",
        "A pragmatic software engineer focused on feasibility, architecture, and implementation planning.",
    )

    designer_agent = create_agent_from_persona(
        "personas/product_designer.json",
        "A product designer focused on user needs, usability, and interaction design.",
    )

    marketing_task = Task(
        description=(
            "Propose a go-to-market and launch strategy for a new AI productivity product. "
            "Focus on target users, core messaging, and launch channels."
        ),
        expected_output="A short launch strategy with target audience, messaging, and channels.",
        agent=marketing_agent,
    )

    engineer_task = Task(
        description=(
            "Outline a practical implementation plan for a new AI productivity product. "
            "Focus on core features, technical feasibility, and delivery priorities."
        ),
        expected_output="A short implementation plan with core features and technical priorities.",
        agent=engineer_agent,
    )

    designer_task = Task(
        description=(
            "Suggest a user experience direction for a new AI productivity product. "
            "Focus on onboarding flow, usability, and core interaction design."
        ),
        expected_output="A short UX proposal with onboarding, usability, and interface priorities.",
        agent=designer_agent,
    )

    return Crew(
        agents=[marketing_agent, engineer_agent, designer_agent],
        tasks=[marketing_task, engineer_task, designer_task],
        verbose=True,
    )


if __name__ == "__main__":
    crew = build_crew()
    result = crew.kickoff()
    print("\n=== CREW RESULT ===")
    print(result)
