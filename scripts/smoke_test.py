from crew import build_crew


def main():
    crew = build_crew()

    assert crew is not None, "Crew object should be created"
    assert hasattr(crew, "agents"), "Crew should expose agents"
    assert hasattr(crew, "tasks"), "Crew should expose tasks"

    assert len(crew.agents) == 3, f"Expected 3 agents, got {len(crew.agents)}"
    assert len(crew.tasks) == 3, f"Expected 3 tasks, got {len(crew.tasks)}"

    roles = [getattr(agent, "role", None) for agent in crew.agents]
    assert "Marketing Strategist" in roles or "Marketing Manager" in roles
    assert "Software Engineer" in roles
    assert "Product Designer" in roles

    print("SMOKE TEST OK")
    print(f"agents={len(crew.agents)} tasks={len(crew.tasks)}")
    print(f"roles={roles}")


if __name__ == "__main__":
    main()
