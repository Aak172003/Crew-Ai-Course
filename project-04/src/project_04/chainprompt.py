# return se sirf next wale function me variable pass hoga 
# but self.state me save krne se everyone can use 
# This Process is known a sprompt chaining . 

from crewai.flow.flow import Flow , start ,listen
from litellm import completion

API_KEY ="AIzaSyBdGgUN6obXQRzV1ZzxfacUzP-CHKXTFHo"
# here start and lister are decorators 

class cityFunFact(Flow):

    # use start decorator
    @start()
    def generate_random_city(self):
        # So if i store my API_KEY in so so i can extract from it 
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content":"Return any random city name from India" , "role":"user"}],

        )
        random_city = result['choices'][0]['message']['content']
        print("random_city : ", random_city)
        # this means those function will execute jst after this so random_city arible pass to that function
        return random_city
    

    @listen(generate_random_city)
    def generate_fun_fact(self , random_city):
        print("this is random city name . ", random_city)
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[{"content":f"write some histroical moments about {random_city} city. " , "role":"user"}],
        )
        fun_fact = result['choices'][0]['message']['content']
        print("fun_fact : ", fun_fact)
        # means store func_fact variable inside its own state 
        self.state["fun-fact"] = fun_fact


    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_fact.md", 'w') as file:
            file.write(self.state["fun-fact"])
            return self.state["fun-fact"]




def kickoff():
    print("Hello from chaning prompt file")
    obj = cityFunFact()
    # This kickoff is here because this SimpleFlow class inherit Flow
    result = obj.kickoff()
    print("final outcome : ", result)
