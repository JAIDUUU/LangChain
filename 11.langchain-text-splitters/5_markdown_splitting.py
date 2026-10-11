from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Machine Learning

Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data.

## Supervised Learning

Supervised learning uses labeled datasets to train models. Common algorithms include Linear Regression, Logistic Regression, and Decision Trees.

### Applications
- House price prediction
- Spam email detection
- Medical diagnosis

## Unsupervised Learning

Unsupervised learning discovers hidden patterns in unlabeled data. Common techniques include K-Means Clustering and Principal Component Analysis.

### Applications
- Customer segmentation
- Anomaly detection
- Data exploration

## Deep Learning

Deep Learning uses neural networks with multiple layers to learn complex patterns. It is widely used in image recognition, natural language processing, and speech recognition.

### Popular Frameworks
- TensorFlow
- PyTorch
- Keras
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0,
)


chunks=splitter.split_text(text)

print(len(chunks))

for i in range(len(chunks)):
    print(chunks[i])