from litellm import completion

def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash",
    messages=[{ "content": "Hello, how are you?","role": "user"}],
    api_key="AIzaSyBX8EtUPwumwmgRkrOZRhNk66dCFUC2b-E"
    # stream=True,
    )
    print(response['choices'][0]['message']['content'])