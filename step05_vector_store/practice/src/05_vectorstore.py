from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = TextLoader("data/sample.txt", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
    add_start_index=True,
)
chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# TODO 1: FAISS.from_documents(documents=chunks, embedding=embeddings)를 완성하세요.
vectorstore = None

if vectorstore is None:
    raise SystemExit("TODO: FAISS Vector Store를 생성하세요.")

# TODO 2: "책은 며칠 동안 빌릴 수 있나요?"를 k=3으로 검색하세요.
results = []

for i, doc in enumerate(results, start=1):
    print(f"\n[{i}]")
    print(doc.page_content)
    print(doc.metadata)
