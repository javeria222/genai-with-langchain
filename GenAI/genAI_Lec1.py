#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

from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature = 0, groq_api_key='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', model = "llama-3.3-70b-versatile"
)

response = llm.invoke("the first person on moon was ")
print(response.content)


