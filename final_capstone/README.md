# Step 14. 종합실습 및 Wrap-up

교재 14장의 목표에 맞춰 **기본 RAG → 문제 확인 → 한 가지 개선 → 같은 질문으로 재평가**를 수행합니다.

교재: [14. 종합실습 및 Wrap-up Quiz](https://app.notion.com/p/3e391bd5a9ac81009f9dd93ed6f78b1f)

## 1. 문제 정의

샘플도서관 안내 문서를 근거로 사용자의 운영시간, 대출, 시설 이용 질문에 답하는 RAG를 구현합니다.

## 2. 사용 데이터

- `data/sample.txt`
- 문서에 없는 질문도 포함해 근거 없음 처리를 확인합니다.

## 3. RAG 구조

```text
Document
  ↓
Loader → Splitter → Embedding → FAISS
                               ↓
Question → Retriever → Context → LLM → Answer
```

Baseline은 Similarity Search를 사용하고, 예제 개선안은 MMR을 사용합니다.

## 4. 설치 방법

```bash
cd final_capstone/complete
cp .env.example .env
uv sync
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
uv sync
```

`.env`에 `OPENAI_API_KEY`를 설정합니다.

## 5. 실행 방법

```bash
uv run --locked python src/capstone_compare.py
```

## 6. 테스트 질문

예제는 10개의 고정 질문을 사용합니다.

- 평일/토요일 운영시간
- 휴관일
- 대출 가능 권수
- 기본 대출기간
- 연장 조건
- 노트북 이용 장소
- 음료 반입 조건
- 와이파이
- 문서에 없는 주차요금

## 7. Baseline 결과

`capstone_compare.py`가 Similarity Retriever의 Top-K 문서와 Hit Rate를 출력합니다. 실제 결과값은 Embedding 결과와 환경에 따라 달라질 수 있으므로 숫자 자체보다 검색 문서를 직접 확인합니다.

## 8. 개선 방법과 결과

예제에서는 MMR을 적용해 Baseline과 같은 질문셋으로 다시 측정합니다.

```text
Baseline Similarity
        ↓
같은 질문셋 평가
        ↓
MMR 적용
        ↓
같은 질문셋 재평가
        ↓
검색 결과와 답변 비교
```

기술을 많이 넣는 것이 목적이 아닙니다. **어떤 문제를 발견했고 왜 이 전략을 선택했는지**를 설명합니다.

## 9. 한계와 추가 개선 방향

작은 샘플에서는 Similarity와 MMR의 Hit Rate가 같을 수 있습니다. 실제 종합실습에서는 자신의 문서와 8~10개 이상의 고정 질문셋을 사용하고, 필요에 따라 BM25/Hybrid, ParentDocumentRetriever, MultiQuery, Reranker, Query Rewrite, Agentic RAG 등을 선택합니다.

## 폴더

- `practice/`: 종합실습을 직접 완성하는 연습용
- `complete/`: 교재 기준 예시 완성 코드

## 보안

실제 `.env`, API Key, 내부 문서, 개인정보는 저장소에 올리지 않습니다.
