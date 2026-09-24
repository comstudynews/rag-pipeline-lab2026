from dotenv import load_dotenv
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

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

# TODO 1: Similarity와 MMR Top-3를 비교하세요.
# TODO 2: BM25로 DEMO-2026-R7을 검색하세요.
# TODO 3: Dense와 BM25 결과를 unique_merge()로 합쳐 Hybrid 후보를 만드세요.
# TODO 4: LLM 관련성 점수(0~100)로 후보를 Rerank하세요.
# TODO 5: ParentDocumentRetriever, MultiQueryRetriever,
#         EnsembleRetriever, LongContextReorder를 선택 실습으로 추가하세요.

print("TODO: Step 10 검색 품질 고도화를 완성하세요.")
