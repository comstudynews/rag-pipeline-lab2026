from dotenv import load_dotenv
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

from rag_core import build_retriever

load_dotenv()

# 11.3 Advanced RAG 공통 코드
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)
retriever = build_retriever(
    file_path="data/sample.txt",
    k=3,
)


def show_search(title: str, query: str):
    print(f"\n=== {title} ===")
    print("Query:", query)
    docs = retriever.invoke(query)

    for i, doc in enumerate(docs, start=1):
        print(f"{i}. {doc.page_content}")


# 11.4 Query Rewrite
def rewrite_query(question: str) -> str:
    # TODO 1: 의미를 유지하면서 검색에 적합한 한 문장으로 Rewrite하세요.
    raise NotImplementedError("TODO 1: rewrite_query를 완성하세요.")


question = "책 빌리면 며칠 안에 갖다 줘야 해?"
rewritten = rewrite_query(question)

print("=== Query Rewrite ===")
print("원래 질문:", question)
print("Rewrite:", rewritten)
show_search("원래 질문", question)
show_search("Rewrite 질문", rewritten)


# 11.5 Query Expansion
def expand_query(question: str) -> str:
    # TODO 2: 관련 키워드와 유사 표현을 약 5개 추가한 한 줄 Query를 만드세요.
    raise NotImplementedError("TODO 2: expand_query를 완성하세요.")


question = "노트북은 어디에서 사용할 수 있나요?"
expanded = expand_query(question)

print("\n=== Query Expansion ===")
print("원래 질문:", question)
print("Expansion:", expanded)
show_search("원래 질문", question)
show_search("Expansion 질문", expanded)


# 11.6 Query Decomposition
def decompose_query(question: str) -> list[str]:
    # TODO 3: 복합 질문을 독립적으로 검색 가능한 하위 질문 목록으로 나누세요.
    raise NotImplementedError("TODO 3: decompose_query를 완성하세요.")


complex_question = "평일 운영시간과 대출 가능 권수, 대출기간을 한 번에 알려 주세요."
sub_questions = decompose_query(complex_question)

print("\n=== Query Decomposition ===")
all_docs = []
seen = set()

for q in sub_questions:
    print("-", q)
    docs = retriever.invoke(q)

    for doc in docs:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            all_docs.append(doc)

print("통합 검색 문서 수:", len(all_docs))


# 11.8 Query Routing
def route_query(question: str) -> str:
    # TODO 4: REGULATION / PRODUCT / WEB 중 하나로 Routing하세요.
    raise NotImplementedError("TODO 4: route_query를 완성하세요.")


print("\n=== Query Routing ===")
print(route_query("최신 AI 규제 뉴스가 궁금합니다."))


# 11.12 RAG 모듈 함수 분리
def query_module(question: str) -> str:
    return rewrite_query(question)


def retrieval_basic(query: str):
    return retriever.invoke(query)


def post_retrieval_module(docs):
    return docs


def generation_module(question: str, docs) -> str:
    # TODO 5: 검색 문서를 Context로 구성하고 원래 질문에 답하도록 구현하세요.
    raise NotImplementedError("TODO 5: generation_module을 완성하세요.")


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


print("\n=== Modular RAG: basic ===")
basic_result = run_modular_rag(
    "책 빌리면 며칠 안에 돌려줘야 하나요?",
    retrieval_basic,
)

print("검색 Query:", basic_result["query"])
print("검색 문서 수:", len(basic_result["docs"]))
print("최종 답변:", basic_result["answer"])


# 11.13 Retrieval Module 교체
# TODO 6: MultiQueryRetriever.from_llm(...)을 구성하세요.
multi_query_retriever = None


def retrieval_multi(query: str):
    if multi_query_retriever is None:
        raise NotImplementedError("TODO 6: MultiQueryRetriever를 구성하세요.")
    return multi_query_retriever.invoke(query)


print("\n=== Modular RAG: multi-query ===")
multi_result = run_modular_rag(
    "책 빌리면 언제까지 갖다 줘야 하나요?",
    retrieval_multi,
)

print("검색 Query:", multi_result["query"])
print("검색 문서 수:", len(multi_result["docs"]))
print("최종 답변:", multi_result["answer"])
