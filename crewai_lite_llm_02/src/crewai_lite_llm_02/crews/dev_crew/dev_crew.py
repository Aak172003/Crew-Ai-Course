from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class DevCrew:  
    """Development Crew"""

    # load the agents and tasks from the yaml files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # define the First agent
    @agent
    def junior_python_developer(self) -> Agent:
        print("inside junior_python_developer agent")
        return Agent(
            config=self.agents_config["junior_python_developer"]
        )
    
        # define the agents
    @agent
    def senior_python_developer(self) -> Agent:
        print("inside senior_python_developer agent")
        return Agent(
            config=self.agents_config["senior_python_developer"]
        )
    


    # define the First task
    @task
    def write_python_code(self) -> Task:
        print("inside write_python_code task")
        return Task(
            config=self.tasks_config["write_python_code"]
        )
    
    # define the Second task
    @task
    def review_python_code(self) -> Task:
        print("inside review_python_code task")
        return Task(
            config=self.tasks_config["review_python_code"]
        )


    # define the crew
    @crew
    def crew(self) -> Crew:
        print("inside crew")
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            verbose=True,
        )