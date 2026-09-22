from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def build_retriever(file_path: str = "data/sample.txt", k: int = 3):
    # TODO: Loader → Splitter → Embedding → FAISS → Retriever 순서로 완성하세요.
    raise NotImplementedError("TODO: build_retriever를 완성하세요.")


def format_docs(docs) -> str:
    # TODO: Document 목록을 하나의 Context 문자열로 합치세요.
    raise NotImplementedError("TODO: format_docs를 완성하세요.")
