# Step 13. Agentic RAG

Retrieve → Grade → Generate 또는 Rewrite → Retry → Fallback 흐름을 구성합니다.

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
uv run --locked python src/13_agentic_rag.py
```

## 확인
retry_count 종료 조건은 무한 Loop와 비용·지연 증가를 막는 운영 장치입니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습 및 오류 비교용으로 사용합니다.
