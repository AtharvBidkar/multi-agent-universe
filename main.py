from orchestrator import Orchestrator

from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.ml_agent import MLAgent
from agents.backend import BackendAgent
from agents.frontend import FrontendAgent
from agents.reviewer import ReviewerAgent


def main():
    agents = {
        "planner": PlannerAgent(),
        "researcher": ResearchAgent(),
        "ml agent": MLAgent(),
        "backend agent": BackendAgent(),
        "frontend agent": FrontendAgent(),
        "reviewer": ReviewerAgent(),
    }

    orchestrator = Orchestrator(agents)

    user_input = input("\nEnter your task: ")

    result = orchestrator.run(user_input)

    print("\n================ FINAL RESULT ================\n")
    for task, output in result.items():
        print(f"{task}:\n{output}\n")


if __name__ == "__main__":
    main()