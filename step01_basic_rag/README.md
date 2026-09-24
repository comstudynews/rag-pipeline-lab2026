# Step 01. RAG 전체 흐름 잡기

InMemoryVectorStore로 검색 → Context → Prompt → LLM까지 가장 작은 RAG를 완성합니다.

## 폴더
- `practice/`: 현재 Step의 핵심 부분을 직접 완성합니다.
- `complete/`: 교재 기준 완성 코드입니다.

## 실행
1. `practice/` 또는 `complete/`로 이동합니다.
2. `.env.example`을 `.env`로 복사합니다.
3. 기본 실습은 `OPENAI_API_KEY`를 설정합니다.
4. 잠긴 의존성을 설치합니다.

```bash
uv sync --locked
```

5. 실행합니다.

```bash
uv run --locked python src/01_basic_rag.py
```

## 확인
최종 답변보다 검색 결과를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습 및 오류 비교용으로 사용합니다.
