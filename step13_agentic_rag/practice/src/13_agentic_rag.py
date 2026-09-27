from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph

from rag_core import build_retriever, format_docs

load_dotenv()


class RAGState(TypedDict):
    original_question: str
    question: str
    context: str
    answer: str
    relevance: str
    retry_count: int


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)
retriever = build_retriever(
    file_path="data/sample.txt",
    k=3,
)


def retrieve(state: RAGState):
    # TODO 1 (13.5~13.6): 현재 question으로 검색하고 context를 저장하세요.
    raise NotImplementedError


grade_prompt = ChatPromptTemplate.from_template("""
다음 질문에 답하는 데 아래 검색 문서가 충분히 관련 있는지 판단하세요.

GOOD: 질문에 답하는 데 필요한 핵심 정보가 문서에 있음
BAD: 질문과 무관하거나 핵심 정보가 부족함

GOOD 또는 BAD 중 하나만 출력하세요.

[질문]
{question}

[검색 문서]
{context}
""")


def grade(state: RAGState):
    # TODO 2 (13.5~13.6): original_question과 context를 이용해 GOOD/BAD를 판단하세요.
    raise NotImplementedError


rewrite_prompt = ChatPromptTemplate.from_template("""
다음 질문을 문서 검색에 더 적합한 표현으로 다시 작성하세요.
원래 의미는 유지하세요.
검색 질의 한 문장만 출력하세요.

[원래 질문]
{question}
""")


def rewrite(state: RAGState):
    # TODO 3 (13.5~13.7): 검색용 question을 다시 쓰고 retry_count를 1 증가시키세요.
    raise NotImplementedError


generate_prompt = ChatPromptTemplate.from_template("""
당신은 제공된 문서를 근거로 답하는 질문-답변 도우미입니다.

규칙:
1. 아래 문서에 있는 내용만 근거로 답하세요.
2. 문서에 없는 내용은 추측하지 마세요.
3. 간결하고 명확하게 답하세요.

[문서]
{context}

[사용자 원래 질문]
{question}

[답변]
""")


def generate(state: RAGState):
    # TODO 4 (13.5~13.6): context를 근거로 original_question에 답하세요.
    raise NotImplementedError


def fallback(state: RAGState):
    # TODO 5 (13.5~13.7): 충분한 근거를 찾지 못했다는 답변을 저장하세요.
    raise NotImplementedError


def decide_after_grade(state: RAGState):
    # TODO 6 (13.7~13.8): GOOD / rewrite / fallback 경로를 결정하세요.
    raise NotImplementedError


builder = StateGraph(RAGState)

builder.add_node("retrieve", retrieve)
builder.add_node("grade", grade)
builder.add_node("rewrite", rewrite)
builder.add_node("generate", generate)
builder.add_node("fallback", fallback)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "grade")

# TODO 7 (13.7~13.8):
# grade 결과에 따라 generate / rewrite / fallback으로 분기하고,
# rewrite → retrieve Loop와 generate/fallback → END를 연결하세요.

graph = builder.compile()

question = "책 빌리면 며칠 안에 돌려줘야 하나요?"

initial_state = {
    "original_question": question,
    "question": question,
    "context": "",
    "answer": "",
    "relevance": "",
    "retry_count": 0,
}

print("TODO 1~7을 교재 순서에 따라 완성한 뒤 실행하세요.")
