from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

# TODO 1: 교재와 같은 Document 3개를 준비하세요.
pages = []

# TODO 2: text-embedding-3-small Embedding 모델을 만드세요.
embeddings = None

# TODO 3: InMemoryVectorStore.from_documents(...)로 Vector Store를 만드세요.
vectorstore = None

# TODO 4: k=2 Retriever를 만들고 질문으로 문서를 검색하세요.
question = "도서관에서 노트북은 어디에서 사용할 수 있나요?"
retrieved_docs = []

# TODO 5: 검색 결과를 Context 문자열로 합치세요.
context = ""

# TODO 6: 문서에 없는 내용은 추측하지 않는 Prompt를 만드세요.
prompt = None

# TODO 7: ChatOpenAI(model="gpt-4o-mini", temperature=0)를 호출하세요.

print("TODO: 검색 결과와 최종 답변이 순서대로 나오도록 완성하세요.")
