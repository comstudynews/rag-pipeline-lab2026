# Step 14. 종합실습 및 Wrap-up Quiz

교재: [14. 종합실습 및 Wrap-up Quiz](https://app.notion.com/p/3e391bd5a9ac81009f9dd93ed6f78b1f)

## GitHub 실습 폴더

- `practice/`: 수강생이 직접 완성하는 종합실습
- `complete/`: 교재 기준 예시 완성 코드
- `results/evaluation.md`: Baseline과 개선 결과 기록
- `results/design.md`: 설계 산출물 기록

실행 예시:

```bash
cd final_capstone/complete
cp .env.example .env
uv sync
uv run --locked python src/capstone_compare.py
```

Windows PowerShell:

```powershell
cd final_capstone/complete
Copy-Item .env.example .env
uv sync
uv run --locked python src/capstone_compare.py
```

---

**종합실습 목표**
**기본 RAG → 문제 확인 → 한 가지 개선 → 동일 질문 재평가**를 수행하고 개선 근거를 설명합니다.
## 14.1 종합실습에서 만들 것
*그림: 여러 검색·필터링·생성 모듈을 조합하는 Modular RAG 흐름 — 출처: *[*IBM RAG Techniques*](https://www.ibm.com/think/topics/rag-techniques)
최종 결과물은 다음 흐름을 갖는 작은 RAG 서비스입니다.
기본 기능을 먼저 완성한 뒤 아래 고도화 항목 중 **최소 1개 이상**을 적용합니다.
- MMR
- BM25 / Hybrid Search
- ParentDocumentRetriever
- MultiQueryRetriever
- EnsembleRetriever
- Reranker
- Query Rewrite / Expansion / Decomposition
- LongContextReorder
- LangGraph 기반 Agentic RAG
위 항목은 **구현 선택지**입니다. 별도의 평가 기준이나 배점이 안내되면 해당 기준을 우선합니다.
## 14.2 Step 1 — 문제와 문서 범위 정하기
먼저 RAG가 답해야 할 질문 범위를 한 문장으로 정의합니다.
예시:
```plain text
규정 문서를 근거로 휴가·출장·복리후생 질문에 답하는 RAG
제품 매뉴얼을 근거로 설치·설정·오류 해결 질문에 답하는 RAG
교육 자료를 근거로 수강생의 과정 관련 질문에 답하는 RAG
```
다음을 기록합니다.
① 어떤 사용자가 질문하는가  
② 어떤 문서를 검색하는가  
③ 어떤 질문까지 답해야 하는가  
④ 문서에 근거가 없을 때 어떻게 답할 것인가
## 14.3 Step 2 — Baseline RAG 먼저 완성하기
먼저 아래 Baseline RAG가 실행되는지 확인합니다.
```plain text
Loader
  ↓
RecursiveCharacterTextSplitter
  ↓
Embedding
  ↓
Vector Store
  ↓
Retriever
  ↓
Prompt
  ↓
LLM
```
확인 항목:
- [ ] 문서를 정상적으로 읽는다.
- [ ] Chunk 개수와 metadata를 확인했다.
- [ ] 질문으로 관련 문서를 검색할 수 있다.
- [ ] 검색된 문서를 화면에 출력해 확인했다.
- [ ] 최종 답변이 검색 문서의 근거를 사용한다.
- [ ] 근거가 없을 때 임의로 단정하지 않는다.
Provider 선택 자체는 평가 대상이 아닙니다. **선택 이유와 같은 질문에서의 검색·답변 품질 변화**를 확인합니다.
## 14.4 Step 3 — 테스트 질문 만들기
최소 8\~10개의 테스트 질문을 준비합니다.
<table fit-page-width="true" header-row="true">
<tr>
<td>유형</td>
<td>예시</td>
<td>확인 목적</td>
</tr>
<tr>
<td>정답이 명확한 질문</td>
<td>기본 대출기간은 며칠인가?</td>
<td>기본 검색 성능</td>
</tr>
<tr>
<td>표현이 다른 질문</td>
<td>책은 언제까지 돌려줘야 하나?</td>
<td>의미 검색</td>
</tr>
<tr>
<td>정확한 키워드 질문</td>
<td>DEMO-2026-R7은 무엇인가?</td>
<td>키워드 / Hybrid 검색</td>
</tr>
<tr>
<td>복합 질문</td>
<td>운영시간과 대출권수, 대출기간을 함께 알려줘.</td>
<td>Decomposition 필요성</td>
</tr>
<tr>
<td>문서에 없는 질문</td>
<td>주차요금은 얼마인가?</td>
<td>근거 없음 처리</td>
</tr>
</table>
## 14.5 Step 4 — Baseline 결과 기록하기
고도화 전에 기준선을 남깁니다.
```plain text
질문
검색 Top-K 문서
정답 문서 포함 여부
최종 답변
문서 근거 여부
문제점
```
RAG 개선은 **수정 전과 수정 후를 비교**해야 의미가 있습니다.
## 14.6 Step 5 — 검색 품질 한 단계 개선하기
현재 문제를 먼저 진단한 뒤 방법을 선택합니다.
<table fit-page-width="true" header-row="true">
<colgroup>
<col width="386">
<col width="294.15625">
</colgroup>
<tr>
<td>관찰된 문제</td>
<td>우선 검토할 방법</td>
</tr>
<tr>
<td>비슷한 Chunk만 반복 검색됨</td>
<td>MMR</td>
</tr>
<tr>
<td>코드·약어·제품명이 잘 검색되지 않음</td>
<td>BM25 / Hybrid / Ensemble</td>
</tr>
<tr>
<td>작은 Chunk는 잘 찾지만 문맥이 부족함</td>
<td>ParentDocumentRetriever</td>
</tr>
<tr>
<td>질문 표현에 따라 검색 결과가 크게 달라짐</td>
<td>MultiQuery / Query Rewrite</td>
</tr>
<tr>
<td>후보 문서는 찾지만 순서가 좋지 않음</td>
<td>Reranker</td>
</tr>
<tr>
<td>Context가 길어 중요한 문서가 묻힘</td>
<td>LongContextReorder</td>
</tr>
<tr>
<td>검색 실패 시 다시 판단·검색해야 함</td>
<td>Agentic RAG</td>
</tr>
</table>
## 14.7 Step 6 — 개선 전·후 비교하기
같은 질문 집합으로 Baseline과 개선 Pipeline을 비교합니다.
<table fit-page-width="true" header-row="true">
<colgroup>
<col width="58">
<col width="148.984375">
<col width="145">
<col width="165.390625">
<col width="150">
</colgroup>
<tr>
<td>질문</td>
<td>Baseline 검색</td>
<td>개선 검색</td>
<td>답변 변화</td>
<td>판단</td>
</tr>
<tr>
<td>Q1</td>
<td>Top-K 결과 기록</td>
<td>개선 결과 기록</td>
<td>좋아짐 / 동일 / 나빠짐</td>
<td>근거 작성</td>
</tr>
</table>
## 14.8 Step 7 — 간단한 평가 넣기
평가는 최소한 검색과 생성 두 부분으로 나누어 봅니다.
### Retrieval 확인
- 정답 문서가 Top-K 안에 들어왔는가?
- 관련 문서가 상위에 배치되는가?
- 중복·무관 문서가 지나치게 많지 않은가?
### Generation 확인
- 답변이 검색 Context의 근거와 일치하는가?
- 질문에 직접 답하는가?
- 근거가 없는데 내용을 만들어내지 않는가?
09장의 평가 방법을 사용해 동일한 테스트 질문으로 반복 측정합니다.
## 14.9 Step 8 — 설계 산출물 작성하기
설계 문서에는 다음 내용을 포함합니다.
1. 해결하려는 문제
2. 대상 사용자
3. 사용할 문서와 데이터 범위
4. Baseline RAG 구조
5. 선택한 검색 개선 전략과 선택 이유
6. 평가 질문과 평가 방법
7. 예상되는 한계와 보완 방법
구조는 한 장의 그림으로 정리해도 좋습니다.
```plain text
Document
  ↓
Loader → Splitter → Embedding → Vector Store
                                  ↓
Question → Query Strategy → Retriever → Rerank
                                  ↓
                             Context
                                  ↓
                              LLM
                                  ↓
                              Answer
```
## 14.10 Step 9 — 개발 산출물 정리하기

> 아래 `rag-project/` 구조는 별도 종합실습 제출물 예시입니다. 이 저장소의 예제는 `final_capstone/practice/`와 `final_capstone/complete/`에서 제공합니다.
프로젝트 폴더 예시:
```plain text
rag-project/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
├── data/
│   └── ...
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   ├── rag.py
│   └── evaluate.py
└── results/
    └── evaluation.md
```
API Key가 들어 있는 실제 `.env`는 제출하거나 Git에 올리지 않습니다. 사용하는 Provider가 있다면 `.env.example`에는 **변수명만** 남깁니다. Ollama Local만 사용하는 경우 API Key가 없어도 되지만, 실행에 필요한 Ollama 설치와 Model 이름은 README에 적습니다.
## 14.11 Step 10 — README에 반드시 적을 것
```markdown
# 프로젝트명

## 1. 문제 정의
## 2. 사용 데이터
## 3. RAG 구조
## 4. 설치 방법
## 5. 실행 방법
## 6. 테스트 질문
## 7. Baseline 결과
## 8. 개선 방법과 결과
## 9. 한계와 추가 개선 방향
```
다른 사람이 저장소를 받아 **바로 환경을 구성하고 실행할 수 있게** 작성합니다.
## 14.12 발표할 때 설명할 핵심
발표에서는 다음 흐름을 설명합니다.
① 어떤 문제를 해결하려 했는가  
② Baseline에서 어떤 문제가 발견되었는가  
③ 그 문제 때문에 어떤 RAG 전략을 선택했는가  
④ 검색 결과가 실제로 어떻게 달라졌는가  
⑤ 최종 답변이 어떻게 개선되었는가  
⑥ 아직 남아 있는 한계는 무엇인가
## 14.13 최종 점검
- [ ] 질문 → 검색 → Context → 답변 흐름을 설명할 수 있다.
- [ ] 검색된 문서를 직접 확인하는 코드가 있다.
- [ ] Baseline과 개선 버전을 비교했다.
- [ ] 선택한 전략이 해결하려는 문제와 연결된다.
- [ ] 문서에 없는 정보에 대한 처리 방식을 정했다.
- [ ] API Key와 내부 정보가 소스에 포함되지 않았다.
- [ ] 실행 방법이 README에 정리되어 있다.
## 14.14 Wrap-up Quiz
아래 문제는 **학습 내용을 스스로 확인하기 위한 복습용 퀴즈**이며, 별도의 평가 문항이 아닙니다.
1. RAG에서 Retrieval은 어떤 역할을 하는가?
2. PREPROCESSING과 RUNTIME의 가장 큰 차이는 무엇인가?
3. Token과 Chunk는 어떻게 다른가?
4. Embedding Model과 Chat Model의 역할은 각각 무엇인가?
5. Vector Store와 Retriever는 어떤 관계인가?
6. Top-K를 무조건 크게 설정하면 안 되는 이유는 무엇인가?
7. MMR은 일반 Similarity Search와 무엇이 다른가?
8. Hybrid Search가 Dense Search와 Sparse Search를 함께 사용하는 이유는 무엇인가?
9. Advanced RAG의 네 개선 구간은 무엇인가?
10. Agentic RAG에서 Loop를 만들 때 종료 조건이 반드시 필요한 이유는 무엇인가?
<details>
<summary>정답과 해설 보기</summary>
1. 질문과 관련된 외부 문서나 Chunk를 찾아 Context 후보를 제공한다.
2. PREPROCESSING은 문서를 읽고 나누고 Embedding하여 검색 가능한 상태로 준비하는 과정이고, RUNTIME은 사용자의 질문이 들어온 뒤 검색하고 답변을 생성하는 과정이다.
3. Token은 모델이 텍스트를 처리하는 내부 단위이고, Chunk는 RAG 검색을 위해 개발자가 정한 문서 분할 단위이다.
4. Embedding Model은 텍스트를 벡터로 변환하고, Chat Model은 Context와 질문을 바탕으로 자연어 답변을 생성한다.
5. Vector Store는 벡터와 문서를 저장·검색하고, Retriever는 질문을 받아 관련 Document를 반환하는 공통 검색 인터페이스 역할을 한다.
6. 불필요한 문서가 Context에 많이 들어가 비용과 지연이 늘고 답변 품질도 떨어질 수 있기 때문이다.
7. MMR은 질문과의 관련성뿐 아니라 검색 결과끼리의 다양성도 고려한다.
8. Dense Search는 의미 검색에 강하고 Sparse Search는 정확한 키워드·코드·고유명사 검색에 강하므로 서로의 약점을 보완할 수 있다.
9. Indexing, Pre-Retrieval, Retrieval, Post-Retrieval이다.
10. 검색 실패 시 Rewrite와 재검색이 무한히 반복되는 것을 막고 비용·지연시간을 제한하기 위해서다.
</details>
## 14.15 다음 학습으로 이어가기
RAG Pipeline을 이해했다면 이후 AI Agent 과정에서는 다음 개념이 자연스럽게 이어집니다.
```plain text
RAG
→ 검색 결과를 근거로 답변

Agentic RAG
→ 검색 결과를 판단하고 흐름을 조정

AI Agent
→ 상황에 따라 Tool을 선택하고 여러 작업을 수행
```
AI Agent는 **State → 판단 → 분기 → Tool 선택 → 종료 조건** 순서로 확장합니다.
### 이후 살펴볼 확장 기술
<table fit-page-width="true" header-row="true">
<tr>
<td>주제</td>
<td>무엇을 확장하는가</td>
<td>설명</td>
</tr>
<tr>
<td>GraphRAG</td>
<td>문서 안의 관계와 연결 구조 활용</td>
<td>문서 조각뿐 아니라 “누가 누구와 어떤 관계인가”까지 검색에 활용</td>
</tr>
<tr>
<td>Multimodal RAG</td>
<td>텍스트 외 이미지·표·음성 등 활용</td>
<td>문서의 글자뿐 아니라 여러 형태의 정보를 함께 검색</td>
</tr>
<tr>
<td>MCP</td>
<td>Agent와 외부 Tool·데이터 소스 연결</td>
<td>AI가 표준화된 방식으로 외부 기능을 사용할 수 있게 연결</td>
</tr>
</table>
이 기술들은 이번 RAG 과정의 필수 구현 범위가 아닙니다. 기본 RAG와 Agentic RAG의 흐름을 충분히 이해한 뒤 다음 학습 단계에서 확장합니다.
---
[첫 화면으로 돌아가기](https://app.notion.com/p/3de91bd5a9ac81219435d1f41cc050df)
