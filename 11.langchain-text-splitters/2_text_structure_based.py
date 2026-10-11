from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Machine Learning is a branch of Artificial Intelligence.
It allows computers to learn patterns from data.

Supervised Learning uses labeled datasets.
Examples include Linear Regression and Decision Trees.

Unsupervised Learning finds hidden patterns in data.
Examples include K-Means Clustering and PCA.

Deep Learning uses neural networks with multiple layers.
It is widely used in image recognition and NLP.
"""

spliter=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
)

chunks=spliter.split_text(text)
print(chunks)
print(len(chunks))