from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodal=ChatOpenAI(model='gpt-4',temperature=0,max_completion_tokens=20)
result=chatmodal.invoke("What is the weakest bone in our body")
print(result.content)