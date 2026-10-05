from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="write a joke topic {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain the following joke- {text}",
    input_variables=["text"]
)
parser=StrOutputParser()
joke_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "Explanation":RunnableSequence(prompt2,model,parser)
})

result=RunnableSequence(joke_chain,parallel_chain)

print(result.invoke({"topic":"bad boy"}))

