from crewai import Agent, Task, Crew , Process , LLM

import os
from dotenv import load_dotenv, find_dotenv

# Here we load the environment variables from the .env file
result: bool = load_dotenv(find_dotenv())
print("Environment variables loaded:", result)

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
print(" ::::::: ", api_key)


from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource


llm1 = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=api_key
)

content = """ User Name is Aakash Prajapati. He is 25 years old and lives in Ghaziabad, Uttar Pradesh, India.
He is a software engineer and loves to code. He is a good person.
"""

string_source = StringKnowledgeSource(
    content=content,
)
print("string_source :::::::::: ", string_source)

# Create  an agent with the knowledge source
agent = Agent(
    role="About User",
    goal="You know everything about the user",
    backstory="You are master at understanding the user and provide the information about the user",
    verbose=True,
    allow_delegation= True,
    llm=llm1
)


# Create a task with the agent
task = Task(
    description="Answer the following question based on the user information : {question}",
    expected_output="An answer to the question",
    agent=agent
)

crew = Crew(
    memory=True,
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": api_key,
        }
    }
)



def kickoff():
    result = crew.kickoff(inputs={"question": "What is the name of the user? And what is his age? And where does he live?"})
    print("result --------------- ", result)












