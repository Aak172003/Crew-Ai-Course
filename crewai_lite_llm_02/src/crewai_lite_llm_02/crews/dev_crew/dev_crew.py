from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


# Connect with Multi LLM
from crewai import LLM


from dotenv import load_dotenv

load_dotenv()


# But by default Gemini is connected to the crew . 
# This is how we can connect with Multi LLM
llm_1 = LLM(
    model="ollama/deepseek-r1:1.5b",
    base_url="http://localhost:11434"
)

llm_2 = LLM(
    model="gemini/gemini-2.0-flash"
)





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
            config=self.agents_config["junior_python_developer"],
            # llm=llm_1
        )
    
        # define the agents
    @agent
    def senior_python_developer(self) -> Agent:
        print("inside senior_python_developer agent")
        return Agent(
            config=self.agents_config["senior_python_developer"],
            llm=llm_2
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
            # If we want to run the crew in parallel we can use process=Process.parallel
            # in this sequence will be matter 
            
            # process=Process.sequential,
            verbose=True,
        )