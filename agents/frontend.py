from agents.base_agent import BaseAgent

class FrontendAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Frontend Agent",
            role="Designs UI and frontend experience"
        )