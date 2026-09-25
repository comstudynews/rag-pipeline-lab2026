# 종합실습 설계 문서 - Example

## 1. 해결하려는 문제

샘플도서관 안내 문서를 근거로 운영시간, 대출, 시설 이용 질문에 답하는 RAG를 구성합니다.

## 2. 대상 사용자

도서관 이용자

## 3. 사용할 문서와 데이터 범위

- `data/sample.txt`
- 운영시간, 휴관일, 대출, 노트북 이용 공간, 음료, 와이파이 정보
- 문서에 없는 주차요금 질문도 테스트하여 근거 없음 처리를 확인

## 4. Baseline RAG 구조

```text
TextLoader
  ↓
RecursiveCharacterTextSplitter
  ↓
OpenAIEmbeddings
  ↓
FAISS
  ↓
Similarity Retriever
  ↓
Prompt
  ↓
ChatOpenAI
```

## 5. 검색 개선 전략과 선택 이유

예제 개선안은 MMR입니다. Similarity Search와 같은 질문셋으로 비교하여 검색 결과의 중복과 다양성 변화를 확인합니다.

## 6. 평가 질문과 평가 방법

- 운영시간, 휴관일, 대출권수, 대출기간, 연장, 시설 이용 등 10개 질문
- Retrieval: 예상 키워드가 Top-K 문서에 포함되는지 확인
- Generation: 검색된 Context를 근거로 답변하는지 확인

## 7. 예상 한계와 보완 방법

작은 샘플에서는 Similarity와 MMR의 Hit Rate가 같을 수 있습니다. 더 큰 문서에서는 BM25/Hybrid, Reranker, Query Rewrite 등도 비교할 수 있습니다.
