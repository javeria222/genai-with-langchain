from typing import TypedDict
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature = 0, groq_api_key='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', model = "llama-3.3-70b-versatile"
)


class review(TypedDict):  # Schemea
    summary:str
    sentiment:str
structured_model = llm.with_structured_output(review)
#result = model.invoke(""" The hardware is great, but the software feels bloated. There are two many preinstalled apps that i can not remove. Also the UI looks outdated compared to other brands. Hoping the software update will fix this
#""")
result = structured_model.invoke(""" The hardware is great, but the software feels bloated. 
There are two many preinstalled apps that i can not remove. Also the UI looks outdated compared to other brands. 
Hoping the software update will fix this
""")
print(result)
print(result['summary'])
print(result['sentiment'])
