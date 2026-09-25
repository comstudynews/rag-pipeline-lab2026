# RAG Pipeline Lab 2026

LangChain 기반 RAG Pipeline을 **00장 → 14장 순서로 누적 학습**하고, **15장 보충실습과 오류 해결 부록**까지 제공하는 수업용 저장소입니다.

- 교재: [RAG Pipeline 설계 및 구축 — Step by Step Cookbook](https://app.notion.com/p/3de91bd5a9ac81219435d1f41cc050df)
- Main Path: **OpenAI + FAISS**
- 선택 학습: **Upstage · Chroma · Pinecone · LangSmith · Ollama**
- 기본 환경: **Python 3.11 + uv**

## 1. 수업 진행 방식

각 Step은 앞 단계까지의 코드를 누적합니다.

- `practice/`: 현재 Step에서 수강생이 직접 완성하는 연습 예제
- `complete/`: 교재 기준 완성 코드
- 교재의 장 번호와 GitHub의 Step 번호를 맞춰 진행합니다.
- 기본 수업에서는 교재를 보면서 직접 작성하고, `complete/`는 복습·오류 비교·완성본 확인용으로 사용합니다.

## 2. 교재 ↔ GitHub 매핑

| 교재 | GitHub | 핵심 내용 |
|---|---|---|
| 00 | `step00_environment_setup` | Python, uv, API Key, Provider, 환경 점검 |
| 01 | `step01_basic_rag` | 가장 작은 RAG로 전체 흐름 확인 |
| 02 | `step02_document_loader` | TXT/PDF Loader, 선택: Document Parse |
| 03 | `step03_text_splitter` | Chunk, overlap, 검색 단위 설계 |
| 04 | `step04_embedding` | Embedding, Cosine Similarity, Provider 교체 |
| 05 | `step05_vector_store` | FAISS와 Vector Store |
| 06 | `step06_retriever` | Retriever, Top-K, 검색 결과 확인 |
| 07 | `step07_prompt_llm` | Prompt + LLM, 근거 기반 답변 |
| 08 | `step08_rag_pipeline` | `rag_core.py`, LCEL 기반 RAG Pipeline |
| 09 | `step09_evaluation` | Hit Rate, MRR, Groundedness |
| 10 | `step10_search_quality` | MMR, BM25, Hybrid, Reranker, Advanced Retriever |
| 11 | `step11_advanced_rag` | Rewrite, Expansion, Decomposition, Routing, Modular RAG |
| 12 | `step12_langgraph` | State, Node, Edge, Conditional Edge |
| 13 | `step13_agentic_rag` | Retrieve → Grade → Rewrite → Retry/Fallback |
| 14 | `final_capstone` | Baseline과 개선 Pipeline 비교 |
| 15 | `step15_huggingface_colab` | Hugging Face + Chroma + EXAONE 기반 Korean RAG Colab 보충실습 |
| 부록 | `appendix_troubleshooting` | RAG 실습 오류와 해결 방법 |

## 3. 빠른 시작

uv가 없다면 먼저 설치합니다.

- 공식 문서: https://docs.astral.sh/uv/getting-started/installation/

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

설치 후 새 터미널에서 `uv --version`으로 확인합니다.

Python 3.11 설치 여부도 확인합니다.

```bash
uv python list --only-installed 3.11
```

Python 3.11이 없다면 설치합니다.

```bash
uv python install 3.11
```

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
OPENAI_API_KEY=

# 선택 Provider
UPSTAGE_API_KEY=
PINECONE_API_KEY=
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=rag-pipeline-lab2026
# LANGSMITH_ENDPOINT=
```

### 최초 1회 의존성 동기화

현재 단계별 폴더에는 `pyproject.toml`의 직접 의존성 버전이 고정되어 있습니다. 처음 실행할 때는 다음 명령으로 환경을 만들고 `uv.lock`을 생성합니다.

```bash
uv sync
```

그 다음부터는 잠긴 환경을 기준으로 실행합니다.

```bash
uv run --locked python src/00_check_env.py
```

> 수업 배포본에서 교수자가 `uv.lock`을 함께 제공하는 경우에는 처음부터 `uv sync --locked`를 사용합니다.

## 4. 실습 환경

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

선택 Provider를 사용할 때만 추가합니다.

```bash
uv add langchain-upstage
uv add langchain-pinecone pinecone
uv add langsmith
uv add langchain-ollama
```

## 5. Provider와 Vector Store

- **OpenAI + FAISS**: 수업 Main Path
- **Ollama + FAISS/Chroma**: Local RAG 선택 실습
- **Upstage**: 한국어 문서 Parse·Embedding Provider 비교
- **Pinecone**: 관리형 Cloud Vector DB
- **LangSmith**: Trace·관찰·평가

Ollama는 Vector DB가 아니라 **Local LLM/Embedding Runtime**입니다.

```bash
ollama pull qwen3:4b
ollama pull embeddinggemma
```

## 6. Step 폴더 구조

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

`step15_huggingface_colab/`은 Colab 보충실습용 Notebook 구조이며, `appendix_troubleshooting/`은 오류 해결 문서입니다.

## 7. 종합실습

```bash
cd final_capstone/complete
cp .env.example .env
uv sync
uv run --locked python src/capstone_compare.py
```

종합실습은 **Baseline → 문제 진단 → 한 가지 개선 → 같은 질문으로 재평가** 순서로 진행합니다. 기술을 많이 넣는 것이 아니라 개선 이유와 전·후 결과를 설명하는 것이 핵심입니다.

## 8. 15장 보충실습과 부록

15장은 누적 Step과 별도로 Google Colab에서 실행하는 선택 실습입니다.

- `step15_huggingface_colab/README.md`: 15장 전체 설명과 코드
- `step15_huggingface_colab/korean_rag_colab.ipynb`: Colab 실행용 Notebook
- `step15_huggingface_colab/sample_data.md`: 업로드 테스트용 샘플 문서
- `appendix_troubleshooting/README.md`: 교재 부록의 오류 해결 가이드

Colab Notebook:

https://colab.research.google.com/github/comstudynews/rag-pipeline-lab2026/blob/main/step15_huggingface_colab/korean_rag_colab.ipynb

## 9. 보안

- 실제 `.env`와 API Key는 Git에 올리지 않습니다.
- `.env.example`에는 변수명만 둡니다.
- 내부 문서·개인정보·민감정보는 공개 저장소 실습 데이터로 사용하지 않습니다.
- LangSmith Tracing 사용 시 입력·출력이 외부 Observability 서비스로 전송될 수 있음을 확인합니다.
