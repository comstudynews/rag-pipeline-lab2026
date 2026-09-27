from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

docs = TextLoader("data/sample.txt", encoding="utf-8").load()
chunks = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=20,
).split_documents(docs)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

question = "대출한 책을 연장할 수 있나요?"
retrieved_docs = retriever.invoke(question)

# TODO 1: retrieved_docs를 [문서 N] 형식의 Context 문자열로 합치세요.
context = ""

# TODO 2: 제공된 문서에 있는 정보만 사용하도록 ChatPromptTemplate을 작성하세요.
prompt = None

# TODO 3: ChatOpenAI(model="gpt-4o-mini", temperature=0)를 만드세요.
llm = None

if prompt is None or llm is None or not context:
    raise SystemExit("TODO 1~3을 모두 완성한 뒤 실행하세요.")

messages = prompt.invoke({
    "context": context,
    "question": question,
})
response = llm.invoke(messages)

print("[검색 문서]")
print(context)
print("\n[최종 답변]")
print(response.content)
