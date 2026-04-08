from utils import call_claude

class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def act(self, task, context):
        prompt = f"""
You are {self.name}, {self.role}.

Your job is to complete the following task:

Task: {task}

Context from previous agents:
{context}

Give a clear and useful output.
"""
        return call_claude(prompt)

    def decide_next_agent(self, task, context, available_agents):
        prompt = f"""
You are an intelligent system deciding task delegation.

Task: {task}

Context:
{context}

Available agents:
{available_agents}

Which agent should handle this task next?

Return ONLY the agent name.
"""
        response = call_claude(prompt)
        return response.strip().lower()