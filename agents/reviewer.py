from agents.base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Reviewer",
            role="Reviews and improves the final output"
        )