from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.prompts import PromptTemplate

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

prompt1=template1.invoke({'topic':'black hole'})
result1=model.invoke(prompt1)

prompt2=template2.invoke({'text':result1.content})
result2=model.invoke(prompt2)

print(result2.content)