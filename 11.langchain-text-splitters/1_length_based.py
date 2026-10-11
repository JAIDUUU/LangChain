from  langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("dl-curriculum.pdf")
docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=""
)

result=splitter.split_documents(docs)

print(result[1].page_content)


# Separator	Kahan split hoga
# " "	Space par
# "\n"	New line par
# "\n\n"	Empty line / paragraph ke beech
# "."	Full stop par
# ","	Comma par
# ":"	Colon par
# " "	Words ke beech