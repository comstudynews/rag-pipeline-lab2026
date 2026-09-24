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

baseline = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)

improved = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "fetch_k": 6,
        "lambda_mult": 0.5,
    },
)

test_cases = [
    {"question": "평일 운영시간은 언제인가요?", "expected_keyword": "오전 9시부터 오후 9시"},
    {"question": "토요일에는 몇 시까지 운영하나요?", "expected_keyword": "오후 5시"},
    {"question": "일요일에도 문을 여나요?", "expected_keyword": "휴관"},
    {"question": "책은 최대 몇 권까지 빌릴 수 있나요?", "expected_keyword": "최대 5권"},
    {"question": "기본 대출기간은 며칠인가요?", "expected_keyword": "14일"},
    {"question": "책을 연장할 수 있나요?", "expected_keyword": "7일 연장"},
    {"question": "노트북은 어디에서 사용할 수 있나요?", "expected_keyword": "2층 디지털자료실"},
    {"question": "음료를 가져가도 되나요?", "expected_keyword": "뚜껑이 있는 용기"},
    {"question": "와이파이를 무료로 쓸 수 있나요?", "expected_keyword": "무료"},
    {"question": "주차요금은 얼마인가요?", "expected_keyword": ""},
]


def inspect(retriever, question: str):
    return retriever.invoke(question)


def hit(retriever, question: str, expected_keyword: str) -> int:
    retrieved = inspect(retriever, question)
    if not expected_keyword:
        return 1
    joined = "\n".join(doc.page_content for doc in retrieved)
    return 1 if expected_keyword in joined else 0


def evaluate(name: str, retriever) -> float:
    scores = []

    print(f"\n=== {name} ===")
    for case in test_cases:
        retrieved = inspect(retriever, case["question"])
        score = hit(retriever, case["question"], case["expected_keyword"])
        scores.append(score)

        print("\n질문:", case["question"])
        print("판정:", "HIT" if score else "MISS")
        for i, doc in enumerate(retrieved, start=1):
            print(f"  [{i}] {doc.page_content}")

    hit_rate = sum(scores) / len(scores)
    print("\nHit Rate:", round(hit_rate, 3))
    return hit_rate


baseline_score = evaluate("Baseline Similarity", baseline)
improved_score = evaluate("Improved MMR", improved)

print("\n=== 비교 ===")
print("Baseline Hit Rate:", round(baseline_score, 3))
print("Improved Hit Rate:", round(improved_score, 3))

question = "기본 대출기간과 연장 조건을 알려 주세요."
retrieved_docs = improved.invoke(question)

context = "\n\n".join(
    f"[문서 {i}]\n{doc.page_content}"
    for i, doc in enumerate(retrieved_docs, start=1)
)

prompt = ChatPromptTemplate.from_template("""
아래 문서만 근거로 질문에 답하세요.
문서에 없는 내용은 추측하지 마세요.

[문서]
{context}

[질문]
{question}
""")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

answer = llm.invoke(
    prompt.invoke({
        "context": context,
        "question": question,
    })
).content

print("\n=== 개선 Pipeline 최종 답변 ===")
print(answer)

print("\n※ 작은 샘플에서는 두 Hit Rate가 같을 수 있습니다.")
print("실제 종합실습에서는 고정된 8~10개 이상의 질문셋으로")
print("Baseline의 문제 → 선택한 개선 전략 → 전·후 결과를 기록하세요.")
