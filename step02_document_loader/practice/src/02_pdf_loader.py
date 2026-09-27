from langchain_community.document_loaders import PyPDFLoader

# 선택 실습
# TODO 1: data/sample.pdf를 PyPDFLoader로 읽으세요.
loader = None

# TODO 2: loader.load() 결과를 docs에 저장하세요.
docs = []

if loader is None or not docs:
    raise SystemExit("TODO 1~2를 모두 완성한 뒤 실행하세요.")

print("페이지 단위 Document 개수:", len(docs))

for i, doc in enumerate(docs[:3], start=1):
    print(f"\n--- Document {i} ---")
    print("metadata:", doc.metadata)
    print(doc.page_content[:500])
