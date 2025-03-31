from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class TeachingCrew:
    """Teaching Crew"""

    # Define paths to config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
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
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,  
            verbose=True,
        )