# Evaluation Result - Example

예제는 동일한 문서와 질문셋으로 **Similarity Search → MMR**을 비교합니다. 실제 순위와 점수는 Embedding 결과에 따라 달라질 수 있습니다.

## 비교 조건

- 문서: `data/sample.txt`
- Chunk: `chunk_size=120`, `chunk_overlap=20`
- Embedding: `text-embedding-3-small`
- Vector Store: FAISS
- Top-K: 3
- Baseline: Similarity Search
- Improved: MMR (`fetch_k=6`, `lambda_mult=0.5`)

## 확인 항목

1. 같은 10개 질문으로 Baseline과 MMR을 실행합니다.
2. 각 질문의 Top-K 문서를 직접 확인합니다.
3. Hit Rate를 비교합니다.
4. Hit Rate가 같아도 중복, 순서, 다양성이 달라졌는지 확인합니다.
5. 개선 Retriever로 최종 답변을 생성하고 문서 근거를 확인합니다.

## 해석

작은 샘플에서는 Similarity와 MMR의 Hit Rate가 같을 수 있습니다. 이 경우에도 검색 결과의 중복·순서·다양성을 비교해 개선 효과를 판단합니다.

실제 종합실습에서는 자신의 문서와 8~10개 이상의 고정 질문셋을 사용하고, 문제에 따라 BM25/Hybrid, ParentDocumentRetriever, MultiQuery, Reranker, Query Rewrite, Agentic RAG 등을 선택합니다.
