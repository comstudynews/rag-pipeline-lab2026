# RAG Pipeline Lab 2026

LangChain 기반 RAG Pipeline을 **00장 → 14장 순서로 누적 학습**하는 수업용 저장소입니다.

- 교재: [RAG Pipeline 설계 및 구축 — Step by Step Cookbook](https://app.notion.com/p/3de91bd5a9ac81219435d1f41cc050df)
- 수업용 소스: 이 저장소의 `practice/`와 `complete/`
- Main Path: **OpenAI + FAISS**
- 선택 학습: **Upstage · Chroma · Pinecone · LangSmith · Ollama**

## 학습 방식

각 Step은 앞 단계까지의 코드를 누적합니다.

- `practice/`: 현재 Step에서 직접 완성할 부분을 `TODO`로 남긴 연습 예제
- `complete/`: 해당 Step까지 완성된 기준 코드
- 기본 실행 환경: Python 3.11 + uv
- 의존성은 `uv.lock`을 기준으로 고정합니다.
- 교재와 GitHub의 장 번호 / 파일 번호를 맞춰 진행합니다.

## 교재 ↔ GitHub 매핑

| 교재 | GitHub | 핵심 내용 |
|---|---|---|
| 00 | `step00_environment_setup` | Python, uv, API Key, 선택 Provider, 환경 점검 |
| 01 | `step01_basic_rag` | 가장 작은 RAG로 전체 흐름 확인 |
| 02 | `step02_document_loader` | TXT/PDF Loader, 선택: Document Parse |
| 03 | `step03_text_splitter` | Chunk, overlap, 검색 단위 설계 |
| 04 | `step04_embedding` | Embedding, Cosine Similarity, Provider 교체 개념 |
| 05 | `step05_vector_store` | FAISS와 Vector Store 개념 |
| 06 | `step06_retriever` | Retriever, Top-K, 검색 결과 확인 |
| 07 | `step07_prompt_llm` | Prompt + LLM, 검색 근거 기반 답변 |
| 08 | `step08_rag_pipeline` | `rag_core.py`, LCEL 기반 RAG Pipeline 완성 |
| 09 | `step09_evaluation` | Hit Rate, MRR, Groundedness |
| 10 | `step10_search_quality` | MMR, BM25, Hybrid, Reranker, Advanced Retriever |
| 11 | `step11_advanced_rag` | Rewrite, Expansion, Decomposition, Routing, Modular RAG |
| 12 | `step12_langgraph` | State, Node, Edge, Conditional Edge |
| 13 | `step13_agentic_rag` | Retrieve → Grade → Rewrite → Retry/Fallback |
| 14 | `final_capstone` | Baseline과 개선 Pipeline 비교 종합실습 |

## 빠른 시작

```bash
git clone https://github.com/comstudynews/rag-pipeline-lab2026.git
cd rag-pipeline-lab2026
cd step00_environment_setup/complete
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

기본 실습은 `OPENAI_API_KEY`가 필요합니다.

```text
OPENAI_API_KEY=본인의_OPENAI_API_KEY

# 선택
UPSTAGE_API_KEY=
PINECONE_API_KEY=
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=rag-pipeline-lab2026
```

설치 및 실행:

```bash
uv sync --locked
uv run --locked python src/00_check_env.py
```

## 실습 환경

교재 기준 고정 버전:

```text
Python 3.11
langchain==1.4.2
langchain-openai==1.6.3
langchain-community==0.4.2
langchain-classic==1.0.8
langchain-text-splitters==1.1.2
langgraph==1.2.11
faiss-cpu==1.15.1
pypdf==6.19.0
python-dotenv==1.2.3
rank-bm25==0.2.2
```

선택 Provider를 사용할 때만 추가 패키지를 설치합니다.

```bash
uv add langchain-upstage
uv add langchain-pinecone pinecone
uv add langsmith
uv add langchain-ollama
```

선택 패키지를 추가했다면 `uv.lock`이 바뀌므로 수업에서는 검증된 Lock 파일을 사용합니다.

## Ollama 선택 실습

Ollama는 Vector DB가 아니라 **Local LLM / Embedding Runtime**입니다.

```bash
ollama pull qwen3:4b
ollama pull embeddinggemma
```

LangChain에서는 `ChatOllama`, `OllamaEmbeddings`로 OpenAI 부분을 교체할 수 있습니다. Local 실행은 API Key가 필요 없지만 CPU/GPU/RAM 성능에 따라 속도가 크게 달라질 수 있으므로 Main Path에는 포함하지 않습니다.

## Vector Store 선택 기준

- FAISS: 가장 가볍게 Vector Search 원리 학습
- Chroma: Local In-Memory / Persistent / Server / Cloud
- Pinecone: 관리형 Cloud Vector DB

LLM/Embedding Provider와 Vector Store는 별개 선택입니다. 예: `Ollama + FAISS`, `OpenAI + Chroma`, `Upstage + Pinecone`.

## Step 폴더 구조

```text
stepXX_topic/
├── README.md
├── practice/
│   ├── .env.example
│   ├── .python-version
│   ├── pyproject.toml
│   ├── data/
│   └── src/
└── complete/
    ├── .env.example
    ├── .python-version
    ├── pyproject.toml
    ├── data/
    └── src/
```

교재의 코드를 직접 작성하는 것을 기본으로 하고, `complete/`는 복습·오류 비교·완성본 확인용으로 사용합니다.

## 종합실습

```bash
cd final_capstone/complete
cp .env.example .env
uv sync --locked
uv run --locked python src/capstone_compare.py
```

종합실습은 기술을 많이 넣는 것이 목적이 아닙니다. 같은 평가 질문을 사용해 **Baseline → 문제 진단 → 개선 전략 적용 → 전·후 비교** 순서로 근거를 남기는 것이 핵심입니다.

## 보안

- 실제 `.env`와 API Key는 Git에 올리지 않습니다.
- `.env.example`에는 변수명만 둡니다.
- 내부 문서·개인정보·민감정보는 공개 저장소의 실습 데이터로 사용하지 않습니다.
- LangSmith Tracing을 사용할 때는 입력·출력이 외부 Observability 서비스로 전송될 수 있음을 확인합니다.
