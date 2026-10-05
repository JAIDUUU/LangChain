from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough,RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt2=PromptTemplate(
    template="summarize the following text \n {text}",
    input_variables=["text"]
)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

report_chain=RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_chain,branch_chain)

print(final_chain.invoke({'topic':'usa vs iran'}))
