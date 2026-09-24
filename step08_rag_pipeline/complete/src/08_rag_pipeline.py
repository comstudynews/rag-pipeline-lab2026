from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from rag_core import build_retriever, format_docs

load_dotenv()

retriever = build_retriever(
    file_path="data/sample.txt",
    k=3,
)

prompt = ChatPromptTemplate.from_template("""
당신은 제공된 문서를 근거로 답하는 질문-답변 도우미입니다.

규칙:
1. 아래 [문서]에 있는 내용만 근거로 답하세요.
2. 문서에 없는 내용은 추측하지 마세요.
3. 확인할 수 없는 경우 "제공된 문서에서 확인할 수 없습니다."라고 답하세요.
4. 답변은 간결하고 명확하게 작성하세요.

[문서]
{context}

[질문]
{question}

[답변]
""")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

question = "도서관에서 노트북은 어디에서 사용할 수 있나요?"
answer = chain.invoke(question)

print("[질문]")
print(question)
print("\n[답변]")
print(answer)

print("\n[검색 문서 확인]")
for i, doc in enumerate(retriever.invoke(question), start=1):
    print(f"\n[{i}번 검색 문서]")
    print(doc.page_content)
    print("metadata:", doc.metadata)
