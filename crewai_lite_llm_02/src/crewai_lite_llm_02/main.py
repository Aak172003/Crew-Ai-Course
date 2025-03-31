#!/usr/bin/env python
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv , find_dotenv
from .crews.dev_crew.dev_crew import DevCrew


# Here we load the environment variables from the .env file
_:bool = load_dotenv(find_dotenv())

class DevFlow(Flow):
    @start()
    def run_dev_crew(self):
        print("Running dev crew")
        result = (
            DevCrew()
            .crew()
            .kickoff(
                inputs={"problem_statement": "Write a python code for adding two numbers."}
                )
        )
        print("Dev crew output", result.raw)
        return result.raw


def kickoff():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print("Dev flow result", result)
