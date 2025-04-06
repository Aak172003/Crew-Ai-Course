import os
from crewai import LLM
from dotenv import load_dotenv, find_dotenv

result: bool = load_dotenv(find_dotenv())
print("Environment variables loaded:", result)
print("kickoff :::::::::: ")
api_key = os.getenv("GEMINI_API_KEY")

# Get the API key from environment variables
llm1 = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=api_key
)


from crewai import Crew , Process, Agent, Task
from crewai.memory import LongTermMemory , ShortTermMemory, EntityMemory

from crewai.memory.storage.ltm_sqlite_storage import  LTMSQLiteStorage
from crewai.memory.storage.rag_storage import RAGStorage

from  typing import List , Optional



embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": api_key,
        }
    }
# create an agent
agent = Agent(
    role="About the user",
    goal="You know everything about the user",
    backstory="You are a master at understanding the user and their preferences",
    verbose=True,
    allow_delegation=False,
    llm=llm1
)


# create Task
task = Task(
    description="Answer the following question based on the user information : {question}",
    expected_output="An answer to the question",
    agent=agent
)

# create crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    memory=True,

    # long term memory for persistence storage across sessions
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path="./my_crew2/long_term_memory_storage1.db"
        )
    ),


    # Short Term Memory for current context from RAG
    short_term_memory=ShortTermMemory(
        storage=RAGStorage(
            embedder_config=embedder,
            type="short_term",
            path="./my_crew2/short_term1/"
        )
    ),

    # Entity Memory for storing entities
    entity_memory=EntityMemory(
        storage=RAGStorage(
            embedder_config=embedder,
            type="short_term",
            path="./my_crew2/entity1/"
        )
    )
        
)


def memory_kickoff():
    # Here we load the environment variables from the .env file
   

    os.environ['CREWAI_STORE_DIR'] = "/my_crewai_store"
    print("os.environ['CREWAI_STORE_DIR'] :::::::::: ", os.environ['CREWAI_STORE_DIR'])







