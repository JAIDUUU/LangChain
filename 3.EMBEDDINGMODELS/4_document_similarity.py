from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)

documents = [
    "Lionel Messi – Argentina ke legendary footballer hain aur apni dribbling aur goal-scoring ke liye mashhoor hain.",
    "Cristiano Ronaldo – Portugal ke superstar hain aur apni speed, fitness aur goal-scoring ke liye jaane jaate hain.",
    "Neymar Jr. – Brazil ke talented forward hain jo apni skills, dribbling aur creativity ke liye famous hain.",
    "Kylian Mbappé – France ke fast forward hain jo apni speed aur finishing ke liye mashhoor hain.",
    "Erling Haaland – Norway ke powerful striker hain jo goal karne ki zabardast ability ke liye jaane jaate hain.",
    "Robert Lewandowski – Poland ke experienced striker hain aur apni finishing aur goal-scoring ke liye famous hain.",
    "Kevin De Bruyne – Belgium ke excellent midfielder hain jo passing aur chances create karne ke liye mashhoor hain.",
    "Mohamed Salah – Egypt ke star forward hain jo speed, dribbling aur goals ke liye jaane jaate hain.",
    "Vinícius Júnior – Brazil ke exciting winger hain jo apni speed, dribbling aur attacking skills ke liye famous hain.",
    "Luka Modrić – Croatia ke legendary midfielder hain jo passing, vision aur ball control ke liye mashhoor hain."
]

query = "tell me about neymar"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

index, score = sorted(
    list(enumerate(scores)),
    key=lambda x: x[1],
    reverse=True
)[0]

print(query)
print(documents[index])
print("Similarity:", score)
