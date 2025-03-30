from crewai import Agent, Task, Crew,Process
from crewai.project import CrewBase, agent, crew, task


from dotenv import load_dotenv


load_dotenv()

import yaml

@CrewBase
class TeachingCrew:
    """Teaching Crew"""
    # Using the CrewBase pattern without trying to parse YAML files manually
    # Instead, we'll use the config directly in the agent and task methods
    
    # Define paths to config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    print("agent_config : ", agents_config)
    print("task_config : ", tasks_config)
    
    # Define the agents
    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            config=self.agents_config["sir_zia"],
        )
    
    # Define the tasks
    @task
    def describe_topic(self) -> Task:
        return Task(
            config=self.tasks_config["describe_topic"],

        )
    
    # Define the crew
    @crew
    def crew(self) -> Crew:
        # Update the task description with the topic
        # task = self.describe_topic()
        # task.description = f"Explain the following AI topic in detail with examples and applications: {topic}"
        
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Use the updated task
            # process=Process.sequential,
            verbose=True,
        )