from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

modal=ChatAnthropic(modal='claude-sonnet-4-20250514')
result=modal.invoke("discovry of uranium ")
print(result.content)