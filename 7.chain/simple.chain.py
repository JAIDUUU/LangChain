from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

promt_tempplate=PromptTemplate(
    template="genrate 5 intresting facts about {topic}",
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI()


parser=StrOutputParser()

chain=promt_tempplate | model | parser

result=chain.revoke({'topic':'footbal'})