from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()
embadding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents={
    "rohan is boy ",
    "rohan age is 14",
    "rohan go to chine for study about aiml"
}
result=embadding.embed_documents(documents)
print(str(result))