from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from rag_core import build_retriever, format_docs

load_dotenv()

# 공통 모듈에서 Retriever를 생성합니다.
retriever = build_retriever(file_path="data/sample.txt", k=3)

prompt = ChatPromptTemplate.from_template("""
아래 문서만 근거로 질문에 답하세요.
문서에서 확인할 수 없는 내용은 추측하지 마세요.

[문서]
{context}

[질문]
{question}
""")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

question = "기본 대출기간과 연장 조건을 알려 주세요."

# 1) 질문으로 관련 문서를 검색합니다.
docs = retriever.invoke(question)

# 2) 검색 결과를 하나의 Context로 합칩니다.
context = format_docs(docs)

# 3) Context와 질문을 Prompt에 넣어 답변을 생성합니다.
messages = prompt.invoke({"context": context, "question": question})
answer = llm.invoke(messages).content

print("[검색 문서]")
print(context)
print("\n[최종 답변]")
print(answer)
