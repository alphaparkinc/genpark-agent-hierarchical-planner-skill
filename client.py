class AgentHierarchicalPlannerClient:
    def plan(self, goal: str) -> dict:
        return {"subtasks": [f"Analyze {goal}", f"Execute {goal}", f"Verify {goal}"]}