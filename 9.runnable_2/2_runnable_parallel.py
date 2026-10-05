from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="genrate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="genrate a linkdin post about {topic}",
    input_variables=["topic"]
    
)

parser=StrOutputParser()

parrallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1 , model,parser),
    "linkedin":RunnableSequence(prompt2,model,parser)
})

result=parrallel_chain.invoke({"topic:first time start java with dsa"})

print(result)

