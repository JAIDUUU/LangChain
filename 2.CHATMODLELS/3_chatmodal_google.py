from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

chat_modal=ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.4)
result=chat_modal.invoke("roadmap of aiml")
print(result.content)