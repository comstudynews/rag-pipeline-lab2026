from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

docs = [
    Document(page_content="기본 대출기간은 14일이며, 예약자가 없으면 1회에 한해 7일 연장할 수 있다."),
    Document(page_content="평일 운영시간은 오전 9시부터 오후 9시까지이다."),
    Document(page_content="노트북 이용 공간은 2층 디지털자료실이다."),
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = InMemoryVectorStore.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

question = "책을 빌리면 며칠 안에 반납해야 하나요?"
retrieved_docs = retriever.invoke(question)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt = ChatPromptTemplate.from_template("""
아래 문서만 근거로 질문에 답하세요.
문서에서 확인할 수 없는 내용은 추측하지 마세요.

[문서]
{context}

[질문]
{question}
""")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
messages = prompt.invoke({"context": context, "question": question})
answer = llm.invoke(messages).content

print("[검색 문서]")
print(context)
print("\n[최종 답변]")
print(answer)
