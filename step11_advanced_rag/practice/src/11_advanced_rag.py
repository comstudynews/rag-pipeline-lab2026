from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag_core import build_retriever

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
retriever = build_retriever(file_path="data/sample.txt", k=3)


def rewrite_query(question: str) -> str:
    # TODO: 질문 의미를 유지하면서 검색하기 좋은 Query로 다시 작성하세요.
    raise NotImplementedError


def expand_query(question: str) -> list[str]:
    # TODO: 서로 다른 검색 표현 3개를 생성하세요.
    raise NotImplementedError


def decompose_query(question: str) -> list[str]:
    # TODO: 복합 질문을 작은 질문으로 분해하세요.
    raise NotImplementedError


# TODO: Query Routing과 Modular RAG의 retrieval module 교체를 구현하세요.
print("TODO: Step 11 Advanced / Modular RAG를 완성하세요.")
