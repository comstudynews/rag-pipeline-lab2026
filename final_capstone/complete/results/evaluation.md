# Evaluation Result - Example

실행 결과는 Embedding과 LLM 응답에 따라 달라질 수 있습니다.

## 비교 기준
- 동일한 문서
- 동일한 Chunk 설정
- 동일한 Top-K
- 동일한 평가 질문
- Baseline: Similarity Search
- Improved: MMR

## 해석
작은 샘플 문서에서는 두 방식의 Hit Rate가 같을 수 있습니다.
이 경우에도 검색 결과의 중복, 순서, 다양성을 직접 비교해 개선 효과를 판단합니다.
