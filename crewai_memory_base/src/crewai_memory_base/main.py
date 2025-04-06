import os
from dotenv import load_dotenv, find_dotenv
from crewai.flow.flow import Flow, start, listen

# Here we load the environment variables from the .env file
result: bool = load_dotenv(find_dotenv())
print("Environment variables loaded:", result)

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
print(" ::::::: ", api_key)

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")


class MyFlow(Flow):
    print("start")
    @start()
    def funcion1(self):  # Added self parameter
        print("step : : : : 1")

    print("listen")
    @listen(funcion1)
    def funcion2(self):  # Added self parameter
        print("step : : : : 2")


def kickoff():
    print("create object")
    flow = MyFlow()
    flow.kickoff()



