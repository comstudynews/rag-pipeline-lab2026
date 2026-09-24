from langchain_community.document_loaders import PyPDFLoader

# data 폴더의 텍스트 기반 PDF를 페이지 단위로 읽습니다.
loader = PyPDFLoader("data/sample.pdf")
docs = loader.load()

print("페이지 단위 Document 개수:", len(docs))

for i, doc in enumerate(docs[:3], start=1):
    print(f"\n--- Document {i} ---")
    print("metadata:", doc.metadata)
    print(doc.page_content[:500])
