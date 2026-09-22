# Step 00. Environment Setup

RAG 실습 전체에서 사용할 Python 환경과 핵심 패키지를 먼저 확인합니다.

## 폴더
- `practice/`: 환경 확인 코드를 직접 완성합니다.
- `complete/`: 환경 확인이 완성된 기준 코드입니다.

## 실행

1. `practice/` 또는 `complete/`로 이동합니다.
2. `.env.example`을 `.env`로 복사하고 OpenAI API Key를 입력합니다.
3. 의존성을 설치합니다.

```bash
uv sync
```

4. 환경 확인 코드를 실행합니다.

```bash
uv run python src/00_check_env.py
```

## 확인

- Python 3.11.x
- `OPENAI_API_KEY: 설정됨`
- 주요 패키지 버전
- `핵심 패키지 import: OK`

정상 동작한 뒤 Step 01로 이동합니다.
