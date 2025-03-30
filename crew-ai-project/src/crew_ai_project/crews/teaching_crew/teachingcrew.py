from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
import os
import yaml

@CrewBase
class TeachingCrew():
    # Using the CrewBase pattern without trying to parse YAML files manually
    # Instead, we'll use the config directly in the agent and task methods
    
    # Define paths to config files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    agent_config = os.path.join(script_dir, "..", "config", "agents.yaml")
    task_config = os.path.join(script_dir, "..", "config", "tasks.yaml")

    print("agent_config : ", agent_config)
    print("task_config : ", task_config)
    
    # Define the agents
    @agent
    def sir_zia(self) -> Agent:
        return Agent(
            name="Sir Zia",
            role="AI Expert and Teacher",
            goal="To explain AI concepts clearly and effectively",
            backstory="An experienced AI educator with deep knowledge in artificial intelligence and teaching methodologies.",
            verbose=True,
            allow_delegation=False,
            tools=[]
        )
    
    # Define the tasks
    @task
    def describe_topic(self) -> Task:
        return Task(
            name="Describe AI Topic",
            description="Explain the given AI topic in detail with examples and applications",
            expected_output="A comprehensive explanation of the AI topic",
            agent=self.sir_zia(),  # Call the agent method to get the instance
            context=[]  # Initialize as empty list
        )
    
    # Define the crew
    @crew
    def build_crew(self, topic: str) -> Crew:
        # Update the task description with the topic
        task = self.describe_topic()
        task.description = f"Explain the following AI topic in detail with examples and applications: {topic}"
        
        return Crew(
            agents=[self.sir_zia()],  # Call the agent method to get the instance
            tasks=[task],  # Use the updated task
            verbose=True
        )