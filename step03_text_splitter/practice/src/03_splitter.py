from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/sample.txt", encoding="utf-8")
docs = loader.load()

chunk_size = 120

# TODO 1: chunk_overlap을 교재의 기본값인 20으로 수정하세요.
chunk_overlap = 0

# TODO 2: add_start_index를 True로 수정해 Chunk 시작 위치를 metadata에 남기세요.
add_start_index = False

if chunk_overlap != 20 or not add_start_index:
    raise SystemExit("TODO 1~2를 모두 완성한 뒤 실행하세요.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    add_start_index=add_start_index,
)

chunks = text_splitter.split_documents(docs)

print("원본 Document 수:", len(docs))
print("Chunk 수:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print("metadata:", chunk.metadata)
    print(chunk.page_content)
