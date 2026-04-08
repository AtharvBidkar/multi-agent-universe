from agents.base_agent import BaseAgent

class BackendAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Backend Agent",
            role="Builds APIs and backend systems"
        )