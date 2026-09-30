from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

promt1=PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=['topic']
)

promt2=PromptTemplate(
    template="genrate a 5 pointer summary from the following text \n {text}",
    input_variables=['text']
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

chain=promt1 | model | parser | promt2 | model | parser

result=chain.invoke({'topic':'Unemployment in india '})

print(result)
