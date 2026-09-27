# Step 02. Document Loader

TXT를 LangChain Document로 읽고, 선택 실습으로 PDF Loader를 확인합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac81c384d1dba9d557789f)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## 실행

VS Code에서 **File → Open Folder...**를 선택하고 `step02_document_loader/practice` 폴더를 엽니다. 완성 코드 확인이 필요할 때만 같은 Step의 `complete` 폴더를 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 의존성을 동기화합니다.

이 Step의 TXT/PDF Loader 실습은 로컬 파일만 읽으므로 **API Key가 필요하지 않습니다.**

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/02_loader.py
```

PDF 선택 실습:

```bash
uv run --locked python src/02_pdf_loader.py
```

`data/sample.pdf`는 텍스트 추출을 확인할 수 있는 예제 PDF로 함께 제공됩니다.

## 실습 파일과 순서

Step 02는 누적형 폴더입니다. `src/00_check_env.py`와 `src/01_basic_rag.py`는 앞 Step의 완성 상태로 제공되고, 이번 Step에서는 Loader 파일을 완성합니다.

### TXT 기본 실습 — `src/02_loader.py`

1. `TextLoader` 생성
2. `loader.load()`로 `Document` 목록 생성

### PDF 선택 실습 — `src/02_pdf_loader.py`

1. `PyPDFLoader` 생성
2. `loader.load()`로 페이지 단위 `Document` 목록 생성

`practice/data/`와 `complete/data/`에는 모두 `sample.txt`와 `sample.pdf`가 포함되어 있습니다.

## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
