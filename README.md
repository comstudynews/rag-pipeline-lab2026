# RAG Pipeline Lab 2026

RAG Pipeline을 **Step by Step**으로 구현하는 누적형 실습 저장소입니다.

각 Step은 앞 단계의 완성 코드를 그대로 포함하고, 현재 단계의 핵심 기능만 추가합니다.  
구조는 AIOps 실습 저장소와 동일하게 각 Step 아래를 **practice / complete**로 나눴습니다.

## 실습 방식

- `practice/`: 현재 Step에서 직접 완성할 핵심 부분에 `TODO`가 있습니다.
- `complete/`: 현재 Step까지 누적된 완성 코드입니다.
- 처음 학습할 때는 Step 00부터 순서대로 진행합니다.
- 이전 Step에서 완성한 파일은 다음 Step에도 그대로 누적됩니다.
- 각 Step은 별도 폴더에서 독립적으로 실행할 수 있습니다.

## 전체 흐름

| Step | 주제 | 핵심 내용 |
|---|---|---|
| 00 | Environment Setup | Python, API Key, 핵심 패키지 확인 |
| 01 | Basic RAG | 가장 작은 RAG로 전체 흐름 확인 |
| 02 | Document Loader | Text/PDF 문서 로딩 |
| 03 | Text Splitter | Chunk 분할과 overlap |
| 04 | Embedding | Embedding과 Cosine Similarity |
| 05 | Vector Store | FAISS 저장과 검색 |
| 06 | Retriever | Top-K 검색과 결과 확인 |
| 07 | Prompt + LLM | 검색 Context로 답변 생성 |
| 08 | RAG Pipeline | 공통 `rag_core.py`로 Pipeline 완성 |
| 09 | Evaluation | Hit Rate, MRR, Groundedness |
| 10 | Search Quality | MMR, BM25, Ensemble, Reranker, Advanced Retriever |
| 11 | Advanced RAG | Query Rewrite, Expansion, Decomposition, Modular RAG |
| 12 | LangGraph | State, Node, Edge, Conditional Edge |
| 13 | Agentic RAG | Retrieve → Grade → Rewrite → Retry |
| Final | Capstone | Baseline과 개선 Pipeline의 동일 평가셋 비교 |

## 빠른 시작

```bash
git clone https://github.com/comstudynews/rag-pipeline-lab2026.git
cd rag-pipeline-lab2026
```

처음에는 Step 00 완성본에서 환경부터 확인합니다.

```bash
cd step00_environment_setup/complete
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
uv run python src/00_check_env.py
```

환경 확인이 끝나면 Step 01부터 순서대로 진행합니다.

> `uv`가 없다면 Astral uv 공식 설치 방법으로 먼저 설치하세요.

## Step 폴더 구조

각 Step은 다음 구조를 가집니다.

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

`practice/`에도 앞 Step의 완성 파일은 그대로 들어 있습니다. **현재 Step에서 새로 배우는 파일 또는 핵심 부분만 TODO 상태**이므로 이전 단계를 다시 만들 필요가 없습니다.

예를 들어 Step 06에서는 `01_basic_rag.py`부터 `05_vectorstore.py`까지 이미 누적되어 있고, `06_retriever.py`의 현재 학습 부분만 practice에서 직접 완성합니다.

## 실습 환경

- Python 3.11
- LangChain / LangGraph
- OpenAI Chat / Embedding
- FAISS
- BM25

각 Step의 `pyproject.toml`에는 동일한 고정 버전 의존성이 들어 있습니다.

## Final Capstone

Step 13까지 진행한 뒤 종합실습 참고 구현을 실행할 수 있습니다.

```bash
cd final_capstone/complete
cp .env.example .env
uv sync
uv run python src/capstone_compare.py
```

Windows PowerShell에서는 `cp` 대신 다음을 사용합니다.

```powershell
Copy-Item .env.example .env
```

Capstone에서는 같은 테스트 질문으로 Baseline Similarity Search와 개선 Pipeline을 비교합니다. 작은 샘플에서는 Hit Rate가 동일할 수 있으므로, **점수 자체보다 같은 평가셋에서 검색 결과와 답변이 어떻게 달라졌는지 설명하는 것**이 핵심입니다.

## 보안

- 실제 API Key가 들어 있는 `.env`는 Git에 올리지 않습니다.
- 저장소에는 `.env.example`만 포함합니다.
- 실습 데이터는 공개 가능한 가상 샘플 문서만 사용합니다.
