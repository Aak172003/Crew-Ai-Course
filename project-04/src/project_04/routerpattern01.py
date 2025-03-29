# from crewai.flow.flow import Flow, listen, router, start
# import random
# from litellm import completion

# API_KEY = "AIzaSyBdGgUN6obXQRzV1ZzxfacUzP-CHKXTFHo"

# class RouteFlow(Flow):

#     @start()
#     def greeting(self):
#         print("Hello, I am the greeting function")

#     @router(greeting)
#     def select_city(self):
#         cities = ["karachi", "islamabad", "lahore"]
#         selected_city = random.choice(cities)

#         self.state['city'] = selected_city
#         print("Selected city:", selected_city)
#         return selected_city  

#     @listen(select_city)  
#     def generate_fun_fact(self):
#         city = self.state['city']
#         print("Generating fun fact for:", city)

#         result = completion(
#             model="gemini/gemini-2.0-flash-exp",
#             api_key=API_KEY,
#             messages=[{"content": f"Write some fun fact about {city} city.", "role": "user"}],
#         )

#         fun_fact = result['choices'][0]['message']['content']
#         print("Fun fact:", fun_fact)

#         self.state["fun-fact"] = fun_fact  

#     @listen(generate_fun_fact)  
#     def save_fun_fact(self):
#         with open("router_fun_fact.md", 'w') as file:
#             file.write(self.state["fun-fact"])
#         return self.state["fun-fact"]

# def kickoff():
#     obj = RouteFlow()
#     result = obj.kickoff() 
#     print("Final outcome:", result)

# def plot():
#     obj = RouteFlow()
#     obj.plot()



from crewai.flow.flow import Flow, listen, router, start, or_
import random
from litellm import completion

API_KEY = "AIzaSyBdGgUN6obXQRzV1ZzxfacUzP-CHKXTFHo"

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Hello, I am the greeting function")

    @router(greeting)
    def select_city(self):
        cities = ["karachi", "islamabad", "lahore"]
        selected_city = random.choice(cities)

        self.state['city'] = selected_city
        print("Selected city:", selected_city)

        return selected_city  # Returning the city name directly

    @listen("karachi")    
    def karachi_fun(self):
        print(f"Some fact about {self.state['city']}")
        # return f"Some fact about {self.state['city']}"

    @listen("islamabad")
    def islamabad_fun(self):
        print(f"Some fact about {self.state['city']}")
        # return f"Some fact about {self.state['city']}"

    @listen("lahore")
    def lahore_fun(self):
        print(f"Some fact about {self.state['city']}")
        return f"Some fact about {self.state['city']}"

    @listen(select_city)
    def generate_fun_fact(self):
        city = self.state['city']
        print("Generating fun fact for:", city)

        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=API_KEY,
            messages=[{"content": f"Write some fun fact about {city} city.", "role": "user"}],
        )

        fun_fact = result['choices'][0]['message']['content']
        print("Fun fact:", fun_fact)

        self.state["fun-fact"] = fun_fact  # Store fun fact in state

    @listen(generate_fun_fact)  # Listen for fun fact generation
    def save_fun_fact(self):
        with open("router_fun_fact.md", 'w') as file:
            file.write(self.state["fun-fact"])
        return self.state["fun-fact"]

def kickoff():
    obj = RouteFlow()
    result = obj.kickoff()  # Starts the flow execution
    print("Final outcome:", result)

def plot():
    obj = RouteFlow()
    obj.plot()


    # def plot():
    # flow = RouteFlow()
    # flow.plot("flow_diagram.png")  # Generates visualization

