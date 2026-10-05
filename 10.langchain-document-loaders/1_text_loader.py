from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write a summary for the following poem - \n{poem}",
    input_variables=['poem']
)


loader = TextLoader("poem.txt", encoding="utf-8")

docs=loader.load()
# print(docs[0].page_content)
# print(docs[0].metadata)

chain=prompt|model|parser

result=chain.invoke({"poem":docs[0].page_content})