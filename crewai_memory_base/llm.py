print("llm.py")

from crewai import LLM
llm1 = LLM(
    model="gemini/gemini-2.0-flash",
    api_key="AIzaSyBdGgUN6obXQRzV1ZzxfacUzP-CHKXTFHo" 
)
messages = [{ "role": "user", "content": "Hello, how are you?"}]

response = llm1.call(messages)
print("response :::::::::: ", response)



