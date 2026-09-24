from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

pages = [
    Document(page_content="샘플도서관 평일 운영시간은 오전 9시부터 오후 9시까지이다."),
    Document(page_content="도서는 최대 5권까지 14일 동안 대출할 수 있다."),
    Document(page_content="노트북 이용 공간은 2층 디지털자료실이다."),
]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = InMemoryVectorStore.from_documents(
    pages,
    embedding=embeddings,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

question = "도서관에서 노트북은 어디에서 사용할 수 있나요?"
retrieved_docs = retriever.invoke(question)

print("[검색 결과]")
for i, doc in enumerate(retrieved_docs, start=1):
    print(f"{i}. {doc.page_content}")

context = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt = ChatPromptTemplate.from_template("""
당신은 제공된 문서를 근거로 답하는 질문-답변 도우미입니다.
문서에 없는 내용은 추측하지 말고 "제공된 문서에서 확인할 수 없습니다."라고 답하세요.

[문서]
{context}

[질문]
{question}

[답변]
""")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = prompt.invoke({"context": context, "question": question})
response = llm.invoke(messages)

print("\n[최종 답변]")
print(response.content)
