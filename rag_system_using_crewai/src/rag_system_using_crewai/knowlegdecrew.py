from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import os


# By default knowledge in crewai uses "knowledge"  or we can say it internally uses chroma db for storing knowledge
# We can use other knowledge sources like web search, file, etc.
# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
print("GEMINI_API_KEY ", GEMINI_API_KEY)

# Create a knowledge source
content = "Users name is Aakash Prajapati. He is 30 years old and lives in India. Working as a software engineer at MoonDive. He is a good person and loves to help others."
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

def kickoff_crew():
    result = crew.kickoff(inputs={"question": "What city does Aakash Prajapati live in and how old is he?"})
    print(result)
