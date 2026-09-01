import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0, groq_api_key="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", model = "llama-3.3-70b-versatile"
)

st.header("Research Assistant Tool")
#user_input = st.text_input("Enter Your Prompt")

paper_input = st.selectbox("Selecct Research paper name", ["Select", "Attention all you need", "BERT: Pre-Training of Deep Bidirectional Transformer",
                                                           "GPT-3 Language Models are few short learners", "Diffusion Models beat Gans on Image synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["short(1-2 paragraphs)", "Medium(3-5 paragraphs)", "Long(detailed explanation)"])

#Templete
templete = PromptTemplate(
    template=f'''
    Please summerize the research paper titled "{paper_input}" with the following specification:
Explanation Style" {style_input}
Explanation length: {length_input}
1. Mathematical details:
Include relevant mathematical equations if present in the paper,
Explain mathematical concepts using simple, intuitive code snippets where applicable,
2. Analogies:
Use relatable analogies to simplify complex ideas,
If certain information not available in the paper, response with: "Insufficient information available" instead of guessing
Ensure the summery is clear, accurate and aligned with the provided style and length
''',
    input_variables=[paper_input, style_input, length_input]
)

prompt = templete.invoke({'paper_input': paper_input, 'style_input': style_input, 'length_input':length_input})


if st.button("Click Here"):
  #  result = llm.invoke(user_input)
   # st.write(result.content)
  # st.write("Hello")
  result = llm.invoke(prompt)
  st.write(result.content)