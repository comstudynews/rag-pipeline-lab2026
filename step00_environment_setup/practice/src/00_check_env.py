import os
import sys
from importlib.metadata import version
from importlib.util import find_spec

from dotenv import load_dotenv

load_dotenv()

# TODO 1: Python 버전을 출력하세요.
print("Python:", sys.version.split()[0])

# TODO 2: 필수/선택 환경변수의 설정 여부를 출력하세요.
env_vars = [
    ("OPENAI_API_KEY", True),
    ("UPSTAGE_API_KEY", False),
    ("PINECONE_API_KEY", False),
    ("LANGSMITH_API_KEY", False),
    ("LANGSMITH_TRACING", False),
    ("LANGSMITH_PROJECT", False),
]

print("\n[환경변수]")
for name, required in env_vars:
    # TODO: 설정됨/없음과 필수/선택을 출력하세요.
    print(name, "TODO", "(필수)" if required else "(선택)")

# TODO 3: 핵심 패키지를 import하고 설치 버전을 출력하세요.
packages = [
    "langchain",
    "langchain-openai",
    "langchain-community",
    "langchain-classic",
    "langchain-text-splitters",
    "langgraph",
    "faiss-cpu",
    "pypdf",
    "python-dotenv",
    "rank-bm25",
]

print("\n[핵심 패키지]")
for package in packages:
    # TODO: version(package)를 사용하세요.
    print(package, "TODO")

# TODO 4: 선택 Provider 통합이 설치되어 있는지 find_spec()으로 확인하세요.
optional_modules = {
    "langchain_upstage": "Upstage",
    "langchain_pinecone": "Pinecone",
    "langchain_ollama": "Ollama",
}

print("\n[선택 Provider 통합]")
for module, label in optional_modules.items():
    print(label, "TODO")

print("\nTODO: Step 00 환경 확인 코드를 완성하세요.")
