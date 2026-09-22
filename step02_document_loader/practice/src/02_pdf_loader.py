from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path("data/sample.pdf")

if not pdf_path.exists():
    raise SystemExit("선택 실습: data/sample.pdf를 준비한 뒤 다시 실행하세요.")

# TODO: PyPDFLoader로 PDF를 읽어 pages에 저장하세요.
pages = []

print("PDF 페이지 수:", len(pages))
