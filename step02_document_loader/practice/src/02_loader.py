from langchain_community.document_loaders import TextLoader

# TODO: data/sample.txt를 TextLoader로 읽어 docs에 저장하세요.
docs = []

print("Document 수:", len(docs))
for i, doc in enumerate(docs, start=1):
    print(f"\n--- Document {i} ---")
    print(doc.page_content)
