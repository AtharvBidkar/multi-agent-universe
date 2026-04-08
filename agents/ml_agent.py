from agents.base_agent import BaseAgent

class MLAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ML Agent",
            role="Designs and explains machine learning models"
        )