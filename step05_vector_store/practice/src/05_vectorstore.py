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

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# TODO: chunks와 embeddings로 FAISS Vector Store를 만드세요.
vectorstore = None

if vectorstore is None:
    raise SystemExit("TODO: FAISS.from_documents(...)를 완성하세요.")
