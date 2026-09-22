from dotenv import load_dotenv
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

from rag_core import build_retriever, format_docs

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
retriever = build_retriever(file_path="data/sample.txt", k=3)


def rewrite_query(question: str) -> str:
    # 질문의 의미를 유지하면서 검색하기 좋은 한 문장으로 바꿉니다.
    prompt = f"""
다음 질문의 의미를 바꾸지 말고 문서 검색에 적합한 한 문장으로 다시 작성하세요.
검색 질의만 출력하세요.

[질문]
{question}
"""
    return llm.invoke(prompt).content.strip()


def expand_query(question: str) -> list[str]:
    # 하나의 질문을 서로 다른 검색 표현 세 개로 확장합니다.
    prompt = f"""
다음 질문을 검색할 수 있는 서로 다른 표현 3개를 한 줄에 하나씩 작성하세요.
번호나 설명은 쓰지 마세요.

[질문]
{question}
"""
    lines = [
        line.strip(" -0123456789.")
        for line in llm.invoke(prompt).content.splitlines()
        if line.strip()
    ]
    return lines[:3]


def decompose_query(question: str) -> list[str]:
    # 여러 정보를 묻는 질문을 독립적인 작은 질문으로 나눕니다.
    prompt = f"""
다음 복합 질문을 검색 가능한 작은 질문들로 분해하세요.
한 줄에 질문 하나만 작성하고 번호는 쓰지 마세요.

[질문]
{question}
"""
    return [
        line.strip(" -0123456789.")
        for line in llm.invoke(prompt).content.splitlines()
        if line.strip()
    ]


def route_query(question: str) -> str:
    # 실제 서비스에서는 여러 데이터 소스 중 어디로 보낼지 결정하는 데 사용합니다.
    prompt = f"""
다음 질문을 library, policy, other 중 하나로 분류하세요.
단어 하나만 출력하세요.

[질문]
{question}
"""
    route = llm.invoke(prompt).content.strip().lower()
    return route if route in {"library", "policy", "other"} else "other"


question = "책 빌리면 며칠 안에 갖다 줘야 해?"
rewritten = rewrite_query(question)

print("=== Query Rewrite ===")
print("원래 질문:", question)
print("Rewrite:", rewritten)

print("\n=== Query Expansion ===")
for query in expand_query(question):
    print("-", query)

print("\n=== Query Decomposition ===")
complex_question = "평일 운영시간과 대출 가능 권수, 기본 대출기간을 모두 알려 주세요."
for query in decompose_query(complex_question):
    print("-", query)

print("\n=== Query Routing ===")
print(route_query("도서관 대출기간을 알려 주세요."))


# Modular RAG: 역할별 함수를 교체할 수 있게 나눕니다.
def query_module(question: str) -> str:
    return rewrite_query(question)


def retrieval_basic(query: str):
    return retriever.invoke(query)


multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm,
    include_original=True,
)


def retrieval_multi(query: str):
    return multi_query_retriever.invoke(query)


def generation_module(question: str, docs) -> str:
    context = format_docs(docs)
    prompt = f"""
제공된 문서만 근거로 질문에 답하세요.
문서에서 확인할 수 없는 내용은 추측하지 마세요.

[문서]
{context}

[질문]
{question}
"""
    return llm.invoke(prompt).content.strip()


def run_modular_rag(question: str, retrieval_module) -> dict:
    # Query → Retrieval → Generation을 모듈 단위로 연결합니다.
    query = query_module(question)
    docs = retrieval_module(query)
    answer = generation_module(question, docs)

    return {
        "question": question,
        "query": query,
        "docs": docs,
        "answer": answer,
    }


print("\n=== Modular RAG: basic ===")
basic_result = run_modular_rag(
    "책 빌리면 언제까지 갖다 줘야 하나요?",
    retrieval_basic,
)
print("검색 Query:", basic_result["query"])
print("검색 문서 수:", len(basic_result["docs"]))
print("최종 답변:", basic_result["answer"])

print("\n=== Modular RAG: multi-query ===")
multi_result = run_modular_rag(
    "책 빌리면 언제까지 갖다 줘야 하나요?",
    retrieval_multi,
)
print("검색 Query:", multi_result["query"])
print("검색 문서 수:", len(multi_result["docs"]))
print("최종 답변:", multi_result["answer"])
