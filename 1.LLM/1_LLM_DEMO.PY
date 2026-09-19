from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-6-astra")
result=llm.invoke("give me some best places in delhi ")
print(result)

