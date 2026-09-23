from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents={
    "rohan is boy ",
    "rohan age is 14",
    "rohan go to chine for study about aiml"
}

vector = embedding.embed_documents(documents)

print(str(vector))
