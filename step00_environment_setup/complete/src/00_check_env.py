import os
import sys
from importlib.metadata import version
from importlib.util import find_spec

from dotenv import load_dotenv

load_dotenv()

print("Python:", sys.version.split()[0])

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
    value = os.getenv(name)
    status = "설정됨" if value else "없음"
    label = "필수" if required else "선택"
    print(f"{name}: {status} ({label})")

legacy_vars = [
    "LANGCHAIN_API_KEY",
    "LANGCHAIN_TRACING_V2",
    "LANGCHAIN_PROJECT",
]
legacy_found = [name for name in legacy_vars if os.getenv(name)]
if legacy_found:
    print("\n[참고] 예전 LangChain/LangSmith 환경변수가 감지되었습니다:")
    for name in legacy_found:
        print("-", name)
    print("현재 실습은 LANGSMITH_* 표기를 기본으로 사용합니다.")

import faiss
import langchain
import langchain_classic
import langchain_community
import langchain_openai
import langchain_text_splitters
import langgraph
import pypdf
import rank_bm25

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
    print(f"{package}: {version(package)}")

optional_modules = {
    "langchain_upstage": "Upstage (langchain-upstage)",
    "langchain_pinecone": "Pinecone (langchain-pinecone)",
    "langsmith": "LangSmith (langsmith)",
    "langchain_ollama": "Ollama (langchain-ollama)",
}

print("\n[Provider 통합 패키지]")
for module, label in optional_modules.items():
    print(label + ":", "설치됨" if find_spec(module) else "미설치")

print("\n핵심 환경 확인: OK")
