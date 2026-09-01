
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature = 0, groq_api_key='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', model = "llama-3.3-70b-versatile"
)

history = []

while True:
    user_input = input("You: ")
    history.append(user_input)
    if user_input == "exit":
        break
    result = llm.invoke(history)
    history.append((result.content))
    print("AI: ", result.content)