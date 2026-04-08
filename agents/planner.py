from agents.base_agent import BaseAgent
from utils import call_claude

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Planner",
            role="Breaks user goal into structured step-by-step tasks"
        )

    def act(self, user_input, context):
        prompt = f"""
You are a Planner Agent.

Your job is to break the user request into clear, logical steps.

User Request:
{user_input}

Rules:
- Break into 5–7 meaningful steps
- Each step should be short and clear
- Steps should be executable by different agents

Return ONLY a numbered list.
"""
        response = call_claude(prompt)

        # Convert response into list
        tasks = [line.strip() for line in response.split("\n") if line.strip()]

        return tasks