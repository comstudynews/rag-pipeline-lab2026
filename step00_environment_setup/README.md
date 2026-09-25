# Step 00. 개발환경·API Key 준비

Step 00은 RAG 기능을 구현하는 장이 아니라 **이후 실습을 시작하기 전에 현재 PC와 개발환경이 준비되었는지 확인하는 사전 점검(Preflight Check)** 단계입니다.

수업 중간에 Python 버전, 패키지 설치, API Key, Ollama 실행 문제로 흐름이 끊기지 않도록 필요한 환경을 먼저 준비하고 확인합니다.

- 교재: [00. 개발환경·API Key 준비 | LangChain RAG 실습환경 만들기](https://app.notion.com/p/3de91bd5a9ac8171bf44dd42fb7ad357)
- `practice/`: 수강생이 TODO를 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## Step 00에서 확인하는 것

| 확인 항목 | 확인 내용 |
| --- | --- |
| Git / VS Code | 저장소 Clone, 실습 폴더 열기, 터미널 실행 |
| Python 3.11 | 실제 실행 중인 Python 버전 |
| uv / `.venv` | 가상환경 생성과 의존성 설치 |
| `.env` / API Key | OpenAI, Upstage, Pinecone, LangSmith 환경변수 로드 |
| 핵심 패키지 | LangChain, LangGraph, FAISS, PyPDF, BM25 등 설치 버전 |
| Provider 통합 패키지 | Upstage, Pinecone, LangSmith, Ollama 패키지 설치 여부 |
| Ollama Runtime / Model | Ollama 프로그램과 Local Model 준비 여부 |

> `00_check_env.py`의 `핵심 환경 확인: OK`는 현재 PC의 Python 환경, 환경변수 로드, 패키지 설치 상태가 정상이라는 뜻입니다. API Key의 실제 유효성, Credit·Quota, Provider 응답 성공까지 보장하는 것은 아닙니다.

## 1. 저장소와 실습 폴더 준비

저장소를 내려받습니다.

```bash
git clone https://github.com/comstudynews/rag-pipeline-lab2026.git
```

VS Code에서 **File → Open Folder...**를 선택하고 다음 폴더를 엽니다.

```text
rag-pipeline-lab2026/step00_environment_setup/practice
```

수업은 `practice/`에서 진행하고, 완성 코드 확인이나 오류 비교가 필요할 때만 `complete/`를 사용합니다.

터미널에서 열 경우 Step 00에서만 다음 방법을 사용할 수 있습니다.

```bash
cd rag-pipeline-lab2026/step00_environment_setup/practice
code .
```

## 2. uv와 Python 3.11 준비

uv 설치 여부를 확인합니다.

```bash
uv --version
```

설치되어 있지 않다면:

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Python 3.11 설치 여부를 확인합니다.

```bash
uv python list --only-installed 3.11
```

없으면 설치합니다.

```bash
uv python install 3.11
```

## 3. 가상환경과 의존성 구성

Step 00의 `pyproject.toml`에는 핵심 RAG 패키지와 Provider 통합 패키지가 함께 등록되어 있습니다.

핵심 패키지:

- `langchain`
- `langchain-openai`
- `langchain-community`
- `langchain-classic`
- `langchain-text-splitters`
- `langgraph`
- `faiss-cpu`
- `pypdf`
- `python-dotenv`
- `rank-bm25`

Provider 통합 패키지:

- `langchain-upstage`
- `langchain-pinecone`
- `pinecone`
- `langsmith`
- `langchain-ollama`

따라서 Step 00에서는 별도의 `uv add` 없이 다음 명령으로 모두 설치합니다.

```bash
uv sync
```

처음 실행하면 현재 폴더에 `.venv`가 만들어지고 `uv.lock`이 생성됩니다.

Python 버전을 확인합니다.

```bash
uv run --locked python --version
```

예상 결과:

```text
Python 3.11.x
```

Windows에서 다음 경고가 나와도 설치가 완료되었다면 진행할 수 있습니다.

```text
warning: Failed to hardlink files; falling back to full copy.
```

## 4. .env와 API Key 준비

`.env.example`을 `.env`로 복사합니다.

macOS / Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

현재 `.env.example`:

```text
OPENAI_API_KEY=
UPSTAGE_API_KEY=
PINECONE_API_KEY=
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=rag-pipeline-lab2026
# LANGSMITH_ENDPOINT=
```

기본 RAG 실습에는 `OPENAI_API_KEY`가 필요합니다. Upstage, Pinecone, LangSmith는 해당 기능을 사용할 때 사용합니다.

실제 Key가 들어 있는 `.env`는 GitHub에 올리지 않습니다.

## 5. Ollama 선택 환경 준비

Ollama를 사용할 경우 Runtime과 실습용 Model을 미리 준비합니다.

설치 확인:

```bash
ollama --version
ollama list
```

실습용 Chat Model:

```bash
ollama pull qwen3:4b
```

실습용 Embedding Model:

```bash
ollama pull embeddinggemma
```

필요한 경우 Local Server를 직접 시작합니다.

```bash
ollama serve
```

기본 Local API 주소는 `http://localhost:11434`입니다.

## 6. 환경 확인 프로그램

`practice/src/00_check_env.py`는 TODO가 포함된 연습용 파일입니다.

확인하는 항목:

1. Python 버전
2. `.env` 환경변수 설정 여부
3. 핵심 패키지 설치 버전
4. Provider 통합 패키지 설치 여부

TODO를 완성한 뒤 실행합니다.

```bash
uv run --locked python src/00_check_env.py
```

정상적인 최종 확인 예:

```text
Python: 3.11.x

[환경변수]
OPENAI_API_KEY: 설정됨 (필수)
UPSTAGE_API_KEY: 설정됨 (선택)
PINECONE_API_KEY: 설정됨 (선택)
LANGSMITH_API_KEY: 설정됨 (선택)
LANGSMITH_TRACING: 설정됨 (선택)
LANGSMITH_PROJECT: 설정됨 (선택)

[핵심 패키지]
langchain: 1.4.2
langchain-openai: 1.6.3
langchain-community: 0.4.2
langchain-classic: 1.0.8
langchain-text-splitters: 1.1.2
langgraph: 1.2.11
faiss-cpu: 1.15.1
pypdf: 6.19.0
python-dotenv: 1.2.3
rank-bm25: 0.2.2

[Provider 통합 패키지]
Upstage (langchain-upstage): 설치됨
Pinecone (langchain-pinecone): 설치됨
LangSmith (langsmith): 설치됨
Ollama (langchain-ollama): 설치됨

핵심 환경 확인: OK
```

환경에 따라 `langchain-community` import 시 DeprecationWarning이 표시될 수 있습니다. 패키지 버전이 출력되고 마지막까지 실행되어 `핵심 환경 확인: OK`가 나오면 Step 00 점검 자체는 완료된 것입니다.

## Step 00 완료 기준

다음을 모두 확인한 뒤 Step 01로 진행합니다.

- Python 3.11 사용
- `uv --version` 정상
- `uv sync` 성공
- `.env` 생성 및 필요한 API Key 설정
- 핵심 패키지 설치 및 버전 출력
- Upstage, Pinecone, LangSmith, Ollama 통합 패키지 설치 확인
- Ollama 사용 시 Runtime과 Model 확인
- `uv run --locked python src/00_check_env.py` 실행 성공
- 마지막에 `핵심 환경 확인: OK` 출력

각 Step은 별도의 `practice/` 환경을 사용합니다. Step 00에서 확인한 `.venv`를 모든 장이 공유하는 구조가 아니므로 이후 장에서는 해당 Step 폴더에서 `uv sync`로 다시 환경을 구성합니다.
