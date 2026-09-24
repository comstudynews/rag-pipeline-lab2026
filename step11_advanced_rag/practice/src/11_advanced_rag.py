from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag_core import build_retriever

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
retriever = build_retriever(file_path="data/sample.txt", k=3)


def rewrite_query(question: str) -> str:
    # TODO 1: 의미를 유지하면서 검색에 적합한 한 문장으로 Rewrite하세요.
    raise NotImplementedError


def expand_query(question: str) -> str:
    # TODO 2: 관련 키워드와 유사 표현 약 5개를 추가한 한 줄 Query를 만드세요.
    raise NotImplementedError


def decompose_query(question: str) -> list[str]:
    # TODO 3: 복합 질문을 독립적인 하위 질문 목록으로 나누세요.
    raise NotImplementedError


def route_query(question: str) -> str:
    # TODO 4: REGULATION / PRODUCT / WEB 중 하나로 Routing하세요.
    raise NotImplementedError


# TODO 5: query / retrieval / post-retrieval / generation 모듈을 분리하세요.
# TODO 6: 기본 Retriever와 MultiQueryRetriever를 교체해 같은 질문을 비교하세요.

print("TODO: Step 11 Advanced / Modular RAG를 완성하세요.")
