# Step 01. RAG를 먼저 한 번 완성해 보기

가장 작은 RAG 예제로 검색 → Context → Prompt → LLM 흐름을 먼저 확인합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac81acac24ef71f0c80bc3)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## 실행

VS Code에서 **File → Open Folder...**를 선택하고 `step01_basic_rag/practice` 폴더를 엽니다. 완성 코드 확인이 필요할 때만 같은 Step의 `complete` 폴더를 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 다음 순서로 진행합니다.

1. `.env.example`을 `.env`로 복사합니다.
2. 기본 실습은 `OPENAI_API_KEY`를 설정합니다.
3. 최초 1회 의존성을 동기화합니다.

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/01_basic_rag.py
```



## 실습 순서

교재의 **1.8 최소 RAG 구현 예제**와 `practice/src/01_basic_rag.py`의 TODO 번호는 다음과 같이 1:1로 대응합니다.

1. `Document` 3개 준비
2. `OpenAIEmbeddings` 생성
3. `InMemoryVectorStore` 생성
4. `Retriever` 생성
5. 관련 문서 검색
6. 검색 결과를 `Context` 문자열로 구성
7. `Prompt` 구성
8. `ChatOpenAI` 생성

TODO를 모두 완성한 뒤 실행하면 **검색 결과 → 최종 답변** 순서로 출력됩니다.

## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
