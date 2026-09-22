from dotenv import load_dotenv
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

load_dotenv()

pages = [
    Document(page_content="RAG는 외부 문서를 검색한 뒤 검색 결과를 LLM의 Context에 추가하여 답변을 생성한다."),
    Document(page_content="MMR은 관련성이 높은 문서를 찾으면서도 검색 결과의 중복을 줄인다."),
    Document(page_content="BM25는 키워드 기반 검색 방식이다."),
    Document(page_content="Hybrid Search는 Dense Retrieval과 Sparse Retrieval을 결합한다."),
    Document(page_content="DEMO-2026-R7은 검색 실습에서 사용하는 예시 식별자이다."),
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(pages, embeddings)

# TODO 1: Similarity Retriever와 MMR Retriever를 비교하세요.
# TODO 2: BM25Retriever를 만드세요.
# TODO 3: Dense + Sparse 결과를 EnsembleRetriever로 결합하세요.
# TODO 4: 선택 실습으로 Parent / MultiQuery / LongContextReorder를 추가하세요.

print("TODO: Step 10 검색 품질 고도화를 완성하세요.")
