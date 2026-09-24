from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split(file_path: str):
    # TODO 1: Path로 파일 존재 여부를 확인하세요.
    # TODO 2: TextLoader로 읽고 chunk_size=120, overlap=20으로 분할하세요.
    raise NotImplementedError("TODO: load_and_split을 완성하세요.")


def build_vectorstore(file_path: str = "data/sample.txt"):
    # TODO 3: OpenAIEmbeddings와 FAISS.from_documents(...)를 연결하세요.
    raise NotImplementedError("TODO: build_vectorstore를 완성하세요.")


def build_retriever(file_path: str = "data/sample.txt", k: int = 3):
    # TODO 4: similarity Retriever를 만들고 k를 전달하세요.
    raise NotImplementedError("TODO: build_retriever를 완성하세요.")


def format_docs(docs):
    # TODO 5: [문서 N] 형식의 Context 문자열을 반환하세요.
    raise NotImplementedError("TODO: format_docs를 완성하세요.")
