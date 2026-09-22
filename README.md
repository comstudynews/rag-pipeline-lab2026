# RAG Pipeline Lab 2026

RAG Pipeline을 **Step by Step**으로 구현하는 누적형 실습 저장소입니다.

각 Step은 앞 단계의 완성 코드를 그대로 포함하고, 현재 단계의 핵심 기능만 추가합니다.

## 실습 방식

- `practice/`: 현재 Step에서 직접 작성할 부분에 `TODO`가 있습니다.
- `complete/`: 현재 Step까지 누적된 완성 코드입니다.
- 처음 학습할 때는 Step 01부터 순서대로 진행합니다.
- 각 Step의 `practice/`와 `complete/`는 독립적으로 실행할 수 있습니다.

## 전체 흐름

| Step | 주제 | 핵심 내용 |
|---|---|---|
| 01 | Basic RAG | 가장 작은 RAG로 전체 흐름 확인 |
| 02 | Document Loader | Text/PDF 문서 로딩 |
| 03 | Text Splitter | Chunk 분할과 overlap |
| 04 | Embedding | Embedding과 Cosine Similarity |
| 05 | Vector Store | FAISS 저장과 검색 |
| 06 | Retriever | Top-K 검색과 결과 확인 |
| 07 | Prompt + LLM | 검색 Context로 답변 생성 |
| 08 | RAG Pipeline | 공통 `rag_core.py`로 Pipeline 완성 |
| 09 | Evaluation | Hit Rate, MRR, Groundedness |
| 10 | Search Quality | MMR, BM25, Hybrid, Reranker, Advanced Retriever |
| 11 | Advanced RAG | Query Rewrite/Expansion/Decomposition/Modular RAG |
| 12 | LangGraph | State, Node, Edge, Conditional Edge |
| 13 | Agentic RAG | Retrieve → Grade → Rewrite → Retry |

## 빠른 시작

```bash
git clone https://github.com/comstudynews/rag-pipeline-lab2026.git
cd rag-pipeline-lab2026
```

예를 들어 Step 01 완성본을 실행하려면:

```bash
cd step01_basic_rag/complete
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

`.env`에 본인의 OpenAI API Key를 입력합니다.

```text
OPENAI_API_KEY=본인의_API_KEY
```

그 다음 실행합니다.

```bash
uv sync
uv run python src/01_basic_rag.py
```

> `uv`가 없다면 먼저 https://docs.astral.sh/uv/ 의 공식 설치 방법으로 설치하세요.

## 실습 환경

- Python 3.11
- LangChain / LangGraph
- OpenAI Chat / Embedding
- FAISS
- BM25

각 Step은 동일한 `pyproject.toml` 의존성 구성을 사용합니다.

## 보안

- 실제 API Key가 들어 있는 `.env`는 Git에 올리지 않습니다.
- 저장소에는 `.env.example`만 포함합니다.
- 실습 데이터는 공개 가능한 샘플 문서만 사용합니다.

## Notion 실습 자료

이 저장소는 RAG Pipeline Step by Step 실습 흐름과 함께 사용하도록 구성되어 있습니다.
