from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


# Load environment variables
load_dotenv()


# Models
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# Prompt for notes
prompt1 = PromptTemplate(template="Generate short and simple notes from the following text:{text}",input_variables=["text"])


# Prompt for quiz
prompt2 = PromptTemplate(
    template="Generate 5 short question-answer pairs from the following text:{text}",
    input_variables=["text"]
    )


# Prompt for merging notes and quiz
prompt3 = PromptTemplate(
    template="Merge the following notes and quiz into a single document.Notes:{notes}Quiz:{quiz}",
    input_variables=["notes", "quiz"]
)


# Output parser
parser = StrOutputParser()


# Parallel Chain
parallel_chain = RunnableParallel(
    {"notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser}
)


# Merge Chain
merge_chain = prompt3 | model1 | parser


# Complete Chain
chain = parallel_chain | merge_chain


# Input text
text = """
Support vector machines (SVMs) are a set of supervised learning methods
used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater
than the number of samples.

Uses a subset of training points in the decision function
(called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the
decision function. Common kernels are provided, but it is also
possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples,
avoid over-fitting in choosing Kernel functions and regularization
term is crucial.

SVMs do not directly provide probability estimates. These are
calculated using an expensive five-fold cross-validation.

The support vector machines in scikit-learn support both dense
(numpy.ndarray) and sparse (scipy.sparse) sample vectors as input.
"""


# Run chain
result = chain.invoke({"text": text})


# Print final result
print(result)


# Print chain graph
chain.get_graph().print_ascii()