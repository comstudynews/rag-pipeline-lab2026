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

# TODO 3: ChatOpenAI(model="gpt-4o-mini", temperature=0)를 만들고 호출하세요.
llm = None

print("TODO: 검색 Context와 최종 답변을 출력하도록 완성하세요.")
