from dotenv import load_dotenv

from rag_core import build_retriever

load_dotenv()
retriever = build_retriever(file_path="data/sample.txt", k=3)

test_cases = [
    {"question": "평일 운영시간은 언제인가요?", "expected_keyword": "오전 9시부터 오후 9시"},
    {"question": "한 사람이 빌릴 수 있는 책은 최대 몇 권인가요?", "expected_keyword": "최대 5권"},
    {"question": "노트북은 어디에서 사용할 수 있나요?", "expected_keyword": "2층 디지털자료실"},
]


def hit_at_k(question: str, expected_keyword: str) -> int:
    # TODO: Top-K 결과 안에 expected_keyword가 있으면 1, 없으면 0을 반환하세요.
    raise NotImplementedError


def reciprocal_rank(question: str, expected_keyword: str) -> float:
    # TODO: expected_keyword가 처음 등장한 순위의 역수를 반환하세요.
    raise NotImplementedError


print("TODO: Hit Rate와 MRR 계산을 완성하세요.")
