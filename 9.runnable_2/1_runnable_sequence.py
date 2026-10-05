from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="give a poem on this {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="summarise the poem {text} in beautiful way",
    input_variables=["text"]
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result=chain.invoke({"topic":"old father"})
print(result)