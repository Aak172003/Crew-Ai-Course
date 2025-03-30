from crewai.flow.flow import Flow , start, listen
from litellm import completion
from dotenv import load_dotenv , find_dotenv

# Import the crew
from crew_ai_project.crews.teaching_crew.teachingcrew import TeachingCrew

# Here we load the environment variables from the .env file
_:bool = load_dotenv(find_dotenv())


class PanaFlow(Flow):
    @start()
    def generate_topic(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user", 
                    "content": "Share the most trending topic in AI World in 2025 . Only share the topic name."
                }
            ]
        )
        self.state['topic'] = response['choices'][0]['message']['content']  
        print(f"Step -1: Topic: {self.state['topic']}")
    

    @listen(generate_topic)
    def generate_content(self):
        print(f"Step -2: Generate Content: {self.state['topic']}")
        # Create the crew
        teaching_crew = TeachingCrew()
        crew = teaching_crew.build_crew(topic=self.state['topic'])
        result = crew.kickoff()
        # Run the crew  

        self.state['content'] = result.raw
        print(result.raw)
    
    @listen(generate_content)
    def save_content(self):
        print("Saving content")
        with open("content.md", "w") as f:
            f.write(self.state['content'])
            

def kickoff():
    flow = PanaFlow()
    flow.kickoff()

def plot():
    poem_flow = PanaFlow()
    poem_flow.plot()

