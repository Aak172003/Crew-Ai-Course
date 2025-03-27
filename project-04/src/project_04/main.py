from crewai.flow.flow import Flow , start ,listen
import time
# here start and lister are decorators 


# extend flow class
class SimpleFlow(Flow):

    @start()
    def function1(self):
        print("step 1...")
        time.sleep(3)
    
    # this will tell after start which function will goona execute 
    # also we can tell one more things this function will execute after @listen(function_name)

    @listen(function1)
    def function2(self):
        print("step 2...")
        time.sleep(3)

 
    @listen(function2)
    def function3(self):
        print("step 3...")
        time.sleep(3)



def kickoff():
    print("Hello from kickoff file")
    obj = SimpleFlow()
    # This kickoff is here because this SimpleFlow class inherit Flow
    obj.kickoff()
