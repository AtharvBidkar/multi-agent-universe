class Orchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.context = {}

    def run(self, user_input):
        print("\n SYSTEM STARTED\n")

        # Step 1: Planning
        planner = self.agents["planner"]
        tasks = planner.act(user_input, self.context)

        print(" Tasks Generated:")
        for t in tasks:
            print("-", t)

        current_agent = planner

        # Step 2: Execute tasks dynamically
        for task in tasks:
            if not task.strip():
                continue

            print(f"\n CURRENT TASK: {task}")

            # Ask AI which agent should handle this
            next_agent_name = current_agent.decide_next_agent(
                task,
                self.context,
                list(self.agents.keys())
            )

            # Fallback safety
            if next_agent_name not in self.agents:
                next_agent_name = "reviewer"

            next_agent = self.agents[next_agent_name]

            print(f" Delegated to: {next_agent.name}")

            # Execute task
            result = next_agent.act(task, self.context)

            print(f" Result (short): {result[:150]}...\n")

            # Store context
            self.context[task] = result

            # Move to next agent
            current_agent = next_agent

        print("\n FINAL OUTPUT GENERATED\n")
        return self.context