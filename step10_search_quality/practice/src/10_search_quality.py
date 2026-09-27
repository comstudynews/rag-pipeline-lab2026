import re

from dotenv import load_dotenv
from langchain_classic.retrievers.ensemble import EnsembleRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_classic.retrievers.parent_document_retriever import ParentDocumentRetriever
from langchain_community.document_loaders import TextLoader
from langchain_community.document_transformers import LongContextReorder
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.stores import InMemoryStore
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# 10.2 검색 방식 비교를 위한 문서 준비
pages = [
    Document(page_content="RAG는 외부 문서를 검색한 뒤 검색 결과를 LLM의 Context에 추가하여 답변을 생성한다."),
    Document(page_content="RAG의 Retriever는 사용자 질문과 관련된 문서를 Vector Store에서 검색한다."),
    Document(page_content="MMR은 관련성이 높은 문서를 찾으면서도 서로 너무 비슷한 검색 결과의 중복을 줄인다."),
    Document(page_content="BM25는 단어의 등장 빈도와 문서 내 중요도를 이용하는 키워드 기반 검색 방식이다."),
    Document(page_content="Hybrid Search는 Dense Retrieval과 Sparse Retrieval을 결합하여 검색 Recall과 정확도를 보완한다."),
    Document(page_content="Reranker는 1차 검색으로 가져온 후보 문서를 질문과 다시 비교하여 순서를 재정렬한다."),
    Document(page_content="DEMO-2026-R7은 검색 실습에서 사용하는 예시 식별자이다."),
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(pages, embeddings)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 10.3 Top-K Similarity Search
question = "RAG 검색 결과의 중복을 줄이는 방법은 무엇인가요?"

# TODO 1-1: search_type="similarity", k=3인 Retriever를 만드세요.
similarity_retriever = None

if similarity_retriever is None:
    raise SystemExit("TODO 1-1: Similarity Retriever를 완성하세요.")

similarity_docs = similarity_retriever.invoke(question)

print("\n=== Similarity Top-3 ===")
for i, doc in enumerate(similarity_docs, start=1):
    print(i, doc.page_content)

# 10.4 MMR 기반 다양성 검색
# TODO 1-2: k=3, fetch_k=6, lambda_mult=0.5인 MMR Retriever를 만드세요.
mmr_retriever = None

if mmr_retriever is None:
    raise SystemExit("TODO 1-2: MMR Retriever를 완성하세요.")

mmr_docs = mmr_retriever.invoke(question)

print("\n=== MMR Top-3 ===")
for i, doc in enumerate(mmr_docs, start=1):
    print(i, doc.page_content)

# 10.6 BM25 기반 키워드 검색
# TODO 2: BM25Retriever를 만들고 k=3으로 설정하세요.
bm25 = None

if bm25 is None:
    raise SystemExit("TODO 2: BM25 Retriever를 완성하세요.")

keyword_question = "DEMO-2026-R7이 무엇인가요?"
bm25_docs = bm25.invoke(keyword_question)

print("\n=== BM25 Top-3 ===")
for i, doc in enumerate(bm25_docs, start=1):
    print(i, doc.page_content)

# 10.7 Hybrid Search
def unique_merge(*doc_lists):
    merged = []
    seen = set()

    for docs in doc_lists:
        for doc in docs:
            key = doc.page_content
            if key not in seen:
                seen.add(key)
                merged.append(doc)
    return merged


# TODO 3: Dense와 BM25 Retriever를 각각 k=3으로 만들고 결과를 합치세요.
dense = None
sparse = None
query = "DEMO-2026-R7 검색 시스템 식별자"

if dense is None or sparse is None:
    raise SystemExit("TODO 3: Dense/BM25 Retriever를 완성하세요.")

dense_docs = dense.invoke(query)
sparse_docs = sparse.invoke(query)
hybrid_candidates = unique_merge(dense_docs, sparse_docs)

print("\n=== Hybrid Candidates ===")
for i, doc in enumerate(hybrid_candidates, start=1):
    print(i, doc.page_content)

# 10.9 LLM 기반 Reranking
def relevance_score(question: str, document: str) -> int:
    # TODO 4-1: 질문과 문서의 관련성을 0~100 정수로 평가하도록 구현하세요.
    raise NotImplementedError("TODO 4-1: relevance_score를 완성하세요.")


def rerank(question: str, docs, top_n: int = 3):
    # TODO 4-2: 각 문서의 관련성 점수를 계산해 높은 순서로 top_n개를 반환하세요.
    raise NotImplementedError("TODO 4-2: rerank를 완성하세요.")


reranked = rerank(query, hybrid_candidates, top_n=3)

print("\n=== Reranked Top-3 ===")
for rank, (score, doc) in enumerate(reranked, start=1):
    print(f"{rank}. score={score}")
    print(doc.page_content)

# 10.13 ParentDocumentRetriever
parent_docs = TextLoader("data/sample.txt", encoding="utf-8").load()

# TODO 5: ParentDocumentRetriever를 구성하고 원본 문서를 추가하세요.
parent_retriever = None

if parent_retriever is None:
    raise SystemExit("TODO 5: ParentDocumentRetriever를 완성하세요.")

parent_docs_result = parent_retriever.invoke(
    "대출기간과 연장 조건을 알려 주세요."
)

print("\n=== ParentDocumentRetriever ===")
for i, doc in enumerate(parent_docs_result, start=1):
    print(i, doc.page_content)

# 10.14 MultiQueryRetriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# TODO 6: MultiQueryRetriever.from_llm(...)을 구성하세요.
multi_query = None

if multi_query is None:
    raise SystemExit("TODO 6: MultiQueryRetriever를 완성하세요.")

multi_docs = multi_query.invoke(
    "검색 결과에 비슷한 문서가 반복될 때 어떻게 줄일 수 있나요?"
)

print("\n=== MultiQueryRetriever ===")
for i, doc in enumerate(multi_docs, start=1):
    print(i, doc.page_content)

# 10.15 EnsembleRetriever
# TODO 7: Dense와 BM25 Retriever를 결합한 EnsembleRetriever를 구성하세요.
ensemble = None

if ensemble is None:
    raise SystemExit("TODO 7: EnsembleRetriever를 완성하세요.")

ensemble_docs = ensemble.invoke(
    "DEMO-2026-R7 검색 시스템 식별자"
)

print("\n=== EnsembleRetriever ===")
for i, doc in enumerate(ensemble_docs, start=1):
    print(i, doc.page_content)

# 10.16 LongContextReorder
reorder_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
candidates = reorder_retriever.invoke(
    "RAG 검색 품질을 높이는 방법을 설명해 주세요."
)

# TODO 8: LongContextReorder로 candidates의 순서를 재배치하세요.
reordered_docs = []

if not reordered_docs:
    raise SystemExit("TODO 8: LongContextReorder를 완성하세요.")

print("\n=== 원래 순서 ===")
for i, doc in enumerate(candidates, start=1):
    print(i, doc.page_content)

print("\n=== 재배치 후 ===")
for i, doc in enumerate(reordered_docs, start=1):
    print(i, doc.page_content)
