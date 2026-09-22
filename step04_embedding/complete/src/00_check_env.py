import os
import sys
from importlib.metadata import version

from dotenv import load_dotenv

load_dotenv()

print("Python:", sys.version.split()[0])
print(
    "OPENAI_API_KEY:",
    "설정됨" if os.getenv("OPENAI_API_KEY") else "없음",
)

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

for package in packages:
    print(f"{package}: {version(package)}")

print("핵심 패키지 import: OK")
