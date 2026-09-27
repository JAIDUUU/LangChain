from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "temperature":0.5,
        "return_full_text": False
    }
)

model=ChatHuggingFace(llm=llm)

#1st prompt ->detailed report
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


#2st prompt ->summary
template2=PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['topic']
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'control mind'})
print(result)