from langchain_core.prompts import ChatPromptTemplate

chat_tamplate=ChatPromptTemplate(
    [
        ('system','you are a helpful{domain} expert'),
        ('human','Explain in simple terms, what is {topic}')
    ]
)

prompt=chat_tamplate.invoke({'domain':'circket','topic':'Dusra'})
print(prompt)