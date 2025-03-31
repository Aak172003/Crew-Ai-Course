from crewai.flow.flow import Flow , start, listen
from litellm import completion
import os
from dotenv import load_dotenv , find_dotenv

# Here we load the environment variables from the .env file
_:bool = load_dotenv(find_dotenv())

# Get the model from the .env variable file
MODEL = os.getenv("MODEL")
print("MODEL ::::::::; ", MODEL)

class LitellmFlow(Flow):
    @start()
    def start(self):
        output = completion(
            model=MODEL,
            messages=[{"role": "user", "content": "Hello, how are you?"}]
        )
        print("output ::::::::; ", output)

        return output['choices'][0]['message']['content']



def run_litellm_flow():
    flow = LitellmFlow()
    response = flow.kickoff()
    print("response ::::::::; ", response)





