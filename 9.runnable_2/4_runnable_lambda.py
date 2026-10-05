from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
def word_count(text):
    return len(text.split())

promt=PromptTemplate(
    template="write a joke on a {topic}",
    input_variables=["topic"]

)

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

joke_chain=RunnableSequence(promt,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_chain,parallel_chain)

result=final_chain.invoke({"topic":"boyefriend"})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])
print(final_result)