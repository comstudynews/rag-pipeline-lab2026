import os
import sys

from dotenv import load_dotenv

load_dotenv()

# TODO 1: Python 버전을 출력하세요.
# TODO 2: OPENAI_API_KEY가 설정되어 있는지 확인하세요.
# TODO 3: LangChain, LangGraph, FAISS, PyPDF, BM25 관련 패키지를 import하세요.
# TODO 4: 설치된 주요 패키지 버전을 출력하세요.

print("Python:", sys.version.split()[0])
print(
    "OPENAI_API_KEY:",
    "설정됨" if os.getenv("OPENAI_API_KEY") else "없음",
)
print("TODO: Step 00 환경 확인 코드를 완성하세요.")
