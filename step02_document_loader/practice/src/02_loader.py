from langchain_community.document_loaders import TextLoader

# TODO 1: data/sample.txt를 UTF-8로 읽는 TextLoader를 만드세요.
loader = None

# TODO 2: loader.load() 결과를 docs에 저장하세요.
docs = []

if loader is None or not docs:
    raise SystemExit("TODO 1~2를 모두 완성한 뒤 실행하세요.")

print("문서 개수:", len(docs))
print("\n[page_content]")
print(docs[0].page_content)
print("\n[metadata]")
print(docs[0].metadata)
