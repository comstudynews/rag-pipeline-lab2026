from langchain_community.document_loaders import TextLoader

# TODO: data/sample.txt를 UTF-8로 읽는 TextLoader를 만드세요.
loader = None

# TODO: loader.load() 결과를 docs에 저장하세요.
docs = []

print("문서 개수:", len(docs))

if docs:
    print("\n[page_content]")
    print(docs[0].page_content)
    print("\n[metadata]")
    print(docs[0].metadata)
else:
    print("TODO: TextLoader를 완성하세요.")
