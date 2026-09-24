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

# TODO 1: 문서에 없는 내용은 추측하지 않는 Prompt를 만드세요.
prompt = None

# TODO 2: ChatOpenAI(model="gpt-4o-mini", temperature=0)를 만드세요.
llm = None

# TODO 3: 다음 LCEL 구조를 완성하세요.
# {"context": retriever | format_docs, "question": RunnablePassthrough()}
#   | prompt | llm | StrOutputParser()
chain = None

question = "도서관에서 노트북은 어디에서 사용할 수 있나요?"

if chain is None:
    raise SystemExit("TODO: LCEL RAG Chain을 완성하세요.")

print(chain.invoke(question))
