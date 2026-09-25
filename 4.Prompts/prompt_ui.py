from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

st.header("Gaming Community Research Tool")

# Gaming Topic
topic_input = st.selectbox(
    "Select Gaming Topic",
    [
        "Gaming Community",
        "Esports Community",
        "Online Gaming",
        "Gaming Culture",
        "Game Development Community"
    ]
)

# Explanation Style
style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Professional",
        "Casual"
    ]
)

# Explanation Length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed)"
    ]
)

# Hugging Face Model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-32B",
    task="text-generation",
    temperature=0.7
)

model = ChatHuggingFace(llm=llm)

# Load saved prompt template
template = load_prompt("template.json")

# Chain
chain = template | model

# Button
if st.button("Summarize"):

    result = chain.invoke({
        "topic_input": topic_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)