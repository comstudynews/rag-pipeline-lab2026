# Step 11. Advanced RAG

Query Rewrite, Expansion, Decomposition, Routing과 Modular RAG를 실습합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac811a8cb0e2f6f9a36dfb)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## 실행

VS Code에서 **File → Open Folder...**를 선택하고 `step11_advanced_rag/practice` 폴더를 엽니다. 완성 코드 확인이 필요할 때만 같은 Step의 `complete` 폴더를 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 다음 순서로 진행합니다.

1. `.env.example`을 `.env`로 복사합니다.
2. 기본 실습은 `OPENAI_API_KEY`를 설정합니다.
3. 최초 1회 의존성을 동기화합니다.

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/11_advanced_rag.py
```

## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
