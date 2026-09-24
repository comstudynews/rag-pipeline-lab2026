import re

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from rag_core import build_retriever, format_docs

load_dotenv()

retriever = build_retriever(file_path="data/sample.txt", k=3)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

test_cases = [
    {"question": "평일 운영시간은 언제인가요?", "expected_keyword": "오전 9시부터 오후 9시"},
    {"question": "한 사람이 빌릴 수 있는 책은 최대 몇 권인가요?", "expected_keyword": "최대 5권"},
    {"question": "노트북은 어디에서 사용할 수 있나요?", "expected_keyword": "2층 디지털자료실"},
]


def hit_at_k(question: str, expected_keyword: str) -> int:
    # TODO 1: Top-K 결과 안에 expected_keyword가 있으면 1, 없으면 0을 반환하세요.
    raise NotImplementedError


def reciprocal_rank(question: str, expected_keyword: str) -> float:
    # TODO 2: expected_keyword가 처음 등장한 순위의 역수를 반환하세요.
    raise NotImplementedError


def judge_groundedness(question: str, context: str, answer: str) -> int:
    # TODO 3: LLM으로 답변의 문서 근거 충실도를 1~5점으로 평가하세요.
    raise NotImplementedError


# TODO 4: Hit Rate와 MRR을 계산하세요.
# TODO 5: 검색 문서로 답변을 생성한 뒤 Groundedness를 평가하세요.
print("TODO: Retrieval 평가와 Generation 평가를 완성하세요.")
