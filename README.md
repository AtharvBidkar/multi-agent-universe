🚀 Multi-Agent Universe System 

This project implements a dynamic multi-agent system where multiple AI agents collaborate and delegate tasks to solve complex workflows.

Unlike traditional scripted pipelines, this system:

- Dynamically breaks down tasks
- Assigns tasks to appropriate agents
- Uses AI (Claude) to decide delegation
- Works for ANY type of user input


🏗️ Architecture

User Input

↓
Planner Agent (task breakdown)

↓
Dynamic Delegation (Claude decides next agent)

↓
Execution Loop (agents collaborate)

↓
Final Output



🤖 Agents

- Planner Agent → Breaks user request into tasks
- Research Agent → Finds best approaches
- ML Agent → Designs ML solutions
- Backend Agent → Builds APIs
- Frontend Agent → Designs UI/UX
- Reviewer Agent → Validates output


⚙️ Tech Stack

- Python
- Claude API (Anthropic)
- Custom Multi-Agent Framework


⚙️ Setup Instructions

1. Clone the repository

git clone https://github.com/AtharvBidkar/multi-agent-universe.git

2. Install dependencies
pip install anthropic python-dotenv

3. Run the system
python main.py

---

🧪 Example Inputs

Try different types of tasks:

- Build a crop recommendation system
- Create a blog website
- Design a marketing strategy for a startup
