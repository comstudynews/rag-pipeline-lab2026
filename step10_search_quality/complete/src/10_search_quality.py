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

# 서로 다른 검색 방식을 비교하기 위한 작은 문서 집합입니다.
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

question = "RAG 검색 결과의 중복을 줄이는 방법은 무엇인가요?"

print("=== Similarity Top-3 ===")
similarity = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)
for i, doc in enumerate(similarity.invoke(question), start=1):
    print(i, doc.page_content)

print("\n=== MMR Top-3 ===")
mmr = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "fetch_k": 6, "lambda_mult": 0.5},
)
for i, doc in enumerate(mmr.invoke(question), start=1):
    print(i, doc.page_content)

print("\n=== BM25 ===")
bm25 = BM25Retriever.from_documents(pages)
bm25.k = 3
for i, doc in enumerate(bm25.invoke("DEMO-2026-R7 검색 식별자"), start=1):
    print(i, doc.page_content)

print("\n=== Hybrid / Ensemble ===")
dense = vectorstore.as_retriever(search_kwargs={"k": 4})
sparse = BM25Retriever.from_documents(pages)
sparse.k = 4

ensemble = EnsembleRetriever(
    retrievers=[dense, sparse],
    weights=[0.6, 0.4],
)
for i, doc in enumerate(
    ensemble.invoke("DEMO-2026-R7 검색 시스템 식별자"),
    start=1,
):
    print(i, doc.page_content)

print("\n=== 간단 LLM Reranker ===")
candidates = similarity.invoke("RAG 검색 품질을 높이는 방법")
scored = []

for doc in candidates:
    # 각 후보가 질문과 얼마나 관련 있는지 0~10 정수 하나로 평가합니다.
    score_prompt = f"""
질문과 문서의 관련성을 0~10 정수 하나로 평가하세요.

[질문]
RAG 검색 품질을 높이는 방법

[문서]
{doc.page_content}
"""
    raw = llm.invoke(score_prompt).content.strip()
    digits = "".join(ch for ch in raw if ch.isdigit())
    score = int(digits[:2]) if digits else 0
    score = max(0, min(score, 10))
    scored.append((score, doc))

for score, doc in sorted(scored, key=lambda item: item[0], reverse=True):
    print(score, doc.page_content)

print("\n=== ParentDocumentRetriever ===")
parent_docs = TextLoader("data/sample.txt", encoding="utf-8").load()

# 기존 vectorstore와 섞이지 않도록 별도 객체를 사용합니다.
parent_vectorstore = InMemoryVectorStore(embeddings)
parent_docstore = InMemoryStore()

parent_retriever = ParentDocumentRetriever(
    vectorstore=parent_vectorstore,
    docstore=parent_docstore,
    parent_splitter=RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
    ),
    child_splitter=RecursiveCharacterTextSplitter(
        chunk_size=80,
        chunk_overlap=20,
    ),
)

parent_retriever.add_documents(parent_docs)

for i, doc in enumerate(
    parent_retriever.invoke("대출기간과 연장 조건을 알려 주세요."),
    start=1,
):
    print(i, doc.page_content)

print("\n=== MultiQueryRetriever ===")
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

multi_query = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm,
    include_original=True,
)

for i, doc in enumerate(
    multi_query.invoke("검색 결과에 비슷한 문서가 반복될 때 어떻게 줄일 수 있나요?"),
    start=1,
):
    print(i, doc.page_content)

print("\n=== LongContextReorder ===")
reorder_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
reorder_candidates = reorder_retriever.invoke(
    "RAG 검색 품질을 높이는 방법을 설명해 주세요."
)
reordered = LongContextReorder().transform_documents(reorder_candidates)

for i, doc in enumerate(reordered, start=1):
    print(i, doc.page_content)
