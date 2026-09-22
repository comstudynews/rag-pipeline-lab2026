from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag_core import build_retriever

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

# TODO 1: retrieve Node
# TODO 2: grade Node
# TODO 3: rewrite Node
# TODO 4: generate / fallback Node
# TODO 5: Conditional Edge와 rewrite → retrieve Loop
# TODO 6: retry_count >= 2 종료 조건

print("TODO: Step 13 Agentic RAG를 완성하세요.")
