from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# 1) 원본 문서를 읽습니다.
loader = TextLoader("data/sample.txt", encoding="utf-8")
docs = loader.load()

# 2) 검색하기 좋은 크기의 Chunk로 나눕니다.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
)
chunks = splitter.split_documents(docs)

# 3) Chunk를 벡터로 변환해 FAISS에 저장합니다.
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(chunks, embeddings)

# TODO 4: Vector Store를 k=3인 Retriever로 변환하세요.
retriever = None

if retriever is None:
    raise SystemExit("TODO 4: vectorstore.as_retriever(...)를 완성하세요.")

# 5) 질문을 넣고 실제 검색 결과를 확인합니다.
question = "토요일에는 몇 시까지 운영하나요?"
results = retriever.invoke(question)

for i, doc in enumerate(results, start=1):
    print(f"\n[{i}] {doc.page_content}")
