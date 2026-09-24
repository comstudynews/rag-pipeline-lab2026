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


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
retriever = build_retriever(file_path="data/sample.txt", k=3)

# TODO 1: retrieve Node — 현재 question으로 검색하고 context를 저장하세요.
# TODO 2: grade Node — original_question 기준으로 GOOD/BAD를 판단하세요.
# TODO 3: rewrite Node — 검색용 question을 다시 쓰고 retry_count를 1 증가시키세요.
# TODO 4: generate Node — original_question에 답하세요.
# TODO 5: fallback Node — 충분한 근거를 찾지 못했다는 답변을 저장하세요.
# TODO 6: decide_after_grade — GOOD / rewrite / fallback 경로를 결정하세요.
# TODO 7: rewrite → retrieve Loop를 만들고 retry_count >= 2에서 종료하세요.

print("TODO: Step 13 Agentic RAG를 완성하세요.")
