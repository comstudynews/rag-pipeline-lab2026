from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

docs = TextLoader("data/sample.txt", encoding="utf-8").load()
chunks = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
).split_documents(docs)
vectorstore = FAISS.from_documents(
    chunks,
    OpenAIEmbeddings(model="text-embedding-3-small"),
)

# TODO: k=3인 Retriever를 만드세요.
retriever = None

if retriever is None:
    raise SystemExit("TODO: vectorstore.as_retriever(...)를 완성하세요.")
