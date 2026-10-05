from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 


load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b"
)


prompt=PromptTemplate(
    template="answer the following qustions \n {qustions} from the following text -\n{text}",
    input_variables=["qustions","text"]

)

parser=StrOutputParser()

url="https://www.nytimes.com/wirecutter/reviews/best-laptops/"
loader=WebBaseLoader(url)

docs=loader.load()

chain= prompt | model | parser

result=chain.invoke({"qustions":"mere liyei ismei sei best laptop konsa hoga for ai ml ","text":docs[0].page_content[:2000]})
print(result)