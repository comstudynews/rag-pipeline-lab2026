from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

# TODO 1: 검색 대상으로 사용할 Document 3개를 준비하세요.
pages = []

# TODO 2: 문장의 의미를 벡터로 변환할 Embedding 모델을 만드세요.
embeddings = None

# TODO 3: InMemoryVectorStore.from_documents(...)로 Vector Store를 만드세요.
vectorstore = None

# TODO 4: k=2로 검색하는 Retriever를 만드세요.
retriever = None

question = "도서관에서 노트북은 어디에서 사용할 수 있나요?"

# TODO 5: Retriever를 사용해 질문과 관련된 문서를 검색하세요.
retrieved_docs = []

print("[검색 결과]")
for i, doc in enumerate(retrieved_docs, start=1):
    print(f"{i}. {doc.page_content}")

# TODO 6: 검색 결과를 하나의 Context 문자열로 합치세요.
context = ""

# TODO 7: 문서에 없는 내용은 추측하지 않는 Prompt를 만드세요.
prompt = None

# TODO 8: ChatOpenAI(model="gpt-4o-mini", temperature=0)를 만드세요.
llm = None

if (
    not pages
    or embeddings is None
    or vectorstore is None
    or retriever is None
    or not retrieved_docs
    or not context
    or prompt is None
    or llm is None
):
    raise SystemExit("TODO 1~8을 모두 완성한 뒤 실행하세요.")

messages = prompt.invoke({"context": context, "question": question})
response = llm.invoke(messages)

print("\n[최종 답변]")
print(response.content)
