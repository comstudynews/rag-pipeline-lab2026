# Step 10. 검색 품질 고도화

Similarity, MMR, BM25, Hybrid, Reranker, Parent/MultiQuery/Ensemble/Reorder를 비교합니다.

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
uv run --locked python src/10_search_quality.py
```

## 확인
복잡한 검색은 추가 호출·지연이 생기므로 현재 실패 원인에 맞는 전략만 선택합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습 및 오류 비교용으로 사용합니다.
