# Step 14. 종합실습 및 Wrap-up

Baseline과 개선 Retriever를 같은 질문셋으로 비교하고 근거를 기록합니다.

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
uv run --locked python src/capstone_compare.py
```

## 확인
유료 Provider를 많이 쓰는 것은 평가 목표가 아닙니다. 선택 이유와 전·후 결과를 설명합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습 및 오류 비교용으로 사용합니다.
