from dotenv import load_dotenv
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

from rag_core import build_retriever

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)
retriever = build_retriever(
    file_path="data/sample.txt",
    k=3,
)


def rewrite_query(question: str) -> str:
    # TODO 1 (11.4): 의미를 유지하면서 검색에 적합한 한 문장으로 Rewrite하세요.
    raise NotImplementedError


def show_search(title: str, query: str):
    print(f"\n=== {title} ===")
    print("Query:", query)
    docs = retriever.invoke(query)
    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc.page_content}")


def expand_query(question: str) -> str:
    # TODO 2 (11.5): 관련 키워드와 유사 표현 약 5개를 추가한 한 줄 Query를 만드세요.
    raise NotImplementedError


def decompose_query(question: str) -> list[str]:
    # TODO 3 (11.6): 복합 질문을 독립적인 하위 질문 목록으로 나누세요.
    raise NotImplementedError


def route_query(question: str) -> str:
    # TODO 4 (11.8): REGULATION / PRODUCT / WEB 중 하나로 Routing하세요.
    raise NotImplementedError


def query_module(question: str) -> str:
    return rewrite_query(question)


def retrieval_basic(query: str):
    return retriever.invoke(query)


def post_retrieval_module(docs):
    return docs


def generation_module(question: str, docs) -> str:
    # TODO 5 (11.12): 검색 문서를 Context로 구성하고 원래 질문에 답하도록 구현하세요.
    raise NotImplementedError


def run_modular_rag(question: str, retrieval_module) -> dict:
    query = query_module(question)
    docs = retrieval_module(query)
    docs = post_retrieval_module(docs)
    answer = generation_module(question, docs)

    return {
        "question": question,
        "query": query,
        "docs": docs,
        "answer": answer,
    }


# TODO 6 (11.13): MultiQueryRetriever를 만들고 retrieval_multi()로 연결하세요.
multi_query_retriever = None


def retrieval_multi(query: str):
    if multi_query_retriever is None:
        raise NotImplementedError("TODO 6: MultiQueryRetriever를 구성하세요.")
    return multi_query_retriever.invoke(query)


print("TODO 1~6을 교재 순서에 따라 완성한 뒤 실행하세요.")
