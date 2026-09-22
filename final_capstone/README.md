# Final Capstone. RAG Pipeline 개선 전·후 비교

Step 01~13에서 익힌 내용을 하나의 종합실습으로 연결합니다.

## 폴더
- `practice/`: 자신의 문서와 개선 전략을 적용하는 시작 코드입니다.
- `complete/`: 샘플 문서에서 Baseline Similarity와 MMR을 비교하는 참고 구현입니다.

## 진행 순서
1. Baseline RAG를 먼저 실행합니다.
2. 테스트 질문을 고정합니다.
3. 검색 문제를 관찰합니다.
4. MMR, Hybrid, Ensemble, Query Rewrite, Agentic RAG 중 필요한 전략을 선택합니다.
5. 같은 질문으로 개선 전·후를 다시 측정합니다.
6. 어떤 문제가 어떻게 달라졌는지 기록합니다.

## 참고 완성본 실행
`cd final_capstone/complete`

`.env.example`을 `.env`로 복사한 뒤 API Key를 입력합니다.

`uv sync`

`uv run python src/capstone_compare.py`

작은 샘플에서는 Baseline과 개선 버전의 Hit Rate가 같을 수도 있습니다. 종합실습의 핵심은 기술을 추가하는 것이 아니라 **같은 평가셋으로 개선 근거를 설명하는 것**입니다.
