from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# 1) 문서를 읽습니다.
docs = TextLoader("data/sample.txt", encoding="utf-8").load()

# 2) 검색 단위인 Chunk로 나눕니다.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
    add_start_index=True,
)
chunks = splitter.split_documents(docs)

# 3) Chunk를 Embedding해 FAISS에 저장합니다.
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(chunks, embeddings)

# 4) 사용자 질문과 가까운 Chunk를 검색합니다.
query = "책은 며칠 동안 빌릴 수 있나요?"
results = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(results, start=1):
    print(f"\n[{i}]")
    print(doc.page_content)
    print(doc.metadata)
