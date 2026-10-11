from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

def main():
    marks = [85, 90, 78, 92, 88]
    result = calculate_average(marks)
    print("Average marks:", result)

if __name__ == "__main__":
    main()
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)
print(chunks)
# print(chunks[1])