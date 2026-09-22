from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path("data/sample.pdf")
if not pdf_path.exists():
    raise SystemExit(
        "data/sample.pdf가 없습니다. 텍스트를 선택·복사할 수 있는 PDF를 "
        "data/sample.pdf 이름으로 준비한 뒤 다시 실행하세요."
    )

pages = PyPDFLoader(str(pdf_path)).load()

print("PDF 페이지 수:", len(pages))
for i, page in enumerate(pages[:3], start=1):
    print(f"\n--- Page {i} ---")
    print("metadata:", page.metadata)
    print(page.page_content[:500])
