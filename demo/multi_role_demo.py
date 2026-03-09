from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from crewai_agents.marketing_agent import create_marketing_agent


def main():
    marketing_agent = create_marketing_agent()

    print("Agent created:")
    print(marketing_agent.role)


if __name__ == "__main__":
    main()
