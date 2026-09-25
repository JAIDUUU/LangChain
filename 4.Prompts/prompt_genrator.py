from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please write a paragraph about "{topic_input}"
with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

Focus on the importance, benefits, and challenges
of the topic in the gaming community.
""",
    input_variables=[
        "topic_input",
        "style_input",
        "length_input"
    ],
    validate_template=True
)

template.save("template.json")