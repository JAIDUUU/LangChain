from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser   

llm=HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

promttemplate=PromptTemplate(
    template='give me 5 fact about {topic} \n {formet_instruction}',
    input_variables=['topic'],
    partial_variables={'formet_instruction':parser.get_format_instructions()}
)

chain = promttemplate | model | parser
result=chain.invoke({'topic':"god"})
print(result)