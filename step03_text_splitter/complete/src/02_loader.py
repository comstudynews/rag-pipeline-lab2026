from langchain_community.document_loaders import TextLoader

# data/sample.txt를 LangChain Document 형식으로 읽습니다.
loader = TextLoader("data/sample.txt", encoding="utf-8")
docs = loader.load()

print("Document 수:", len(docs))

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Document {i} ---")
    print("metadata:", doc.metadata)
    print(doc.page_content)
