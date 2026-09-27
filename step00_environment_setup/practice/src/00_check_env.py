import os
import sys
from importlib.metadata import version
from importlib.util import find_spec

from dotenv import load_dotenv

load_dotenv()

# TODO 1: Python 버전 확인 코드는 제공되어 있습니다. 실행 결과가 3.11인지 확인하세요.
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
    # TODO: os.getenv()로 값을 확인하고 설정됨/없음과 필수/선택을 출력하세요.
    print(name, "TODO", "(필수)" if required else "(선택)")

# 핵심 패키지 import 코드는 제공되어 있습니다.
# import 오류가 발생하면 해당 패키지 설치 상태를 먼저 확인하세요.
import faiss
import langchain
import langchain_classic
import langchain_community
import langchain_openai
import langchain_text_splitters
import langgraph
import pypdf
import rank_bm25

# TODO 3: 핵심 패키지의 설치 버전을 출력하세요.
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

# TODO 4: Provider 통합 패키지가 설치되어 있는지 find_spec()으로 확인하세요.
provider_modules = {
    "langchain_upstage": "Upstage (langchain-upstage)",
    "langchain_pinecone": "Pinecone (langchain-pinecone)",
    "langsmith": "LangSmith (langsmith)",
    "langchain_ollama": "Ollama (langchain-ollama)",
}

print("\n[Provider 통합 패키지]")
for module, label in provider_modules.items():
    print(label, "TODO")

print("\nTODO 2~4를 완성한 뒤 출력 내용을 확인하세요.")
