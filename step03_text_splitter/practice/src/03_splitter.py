from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = TextLoader("data/sample.txt", encoding="utf-8").load()

# TODO: chunk_size=120, chunk_overlap=20으로 수정하세요.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=0,
)

chunks = splitter.split_documents(docs)

print("Chunk 수:", len(chunks))
for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)
