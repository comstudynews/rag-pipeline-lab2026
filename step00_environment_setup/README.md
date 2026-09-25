# Step 00. 개발환경·API Key 준비

Python 3.11, uv, API Key, 핵심 패키지, Provider 통합 패키지와 Ollama Runtime을 미리 점검합니다.

Step 00은 RAG 기능 구현이 아니라 **사전 환경 점검(Preflight Check)** 단계입니다. 수업 중간에 설치·인증 문제로 흐름이 끊기지 않도록 이후 실습에 필요한 환경을 먼저 준비하고 확인합니다.

완료 기준:
- Python 3.11과 uv가 정상 동작
- `.env`의 필요한 환경변수를 읽을 수 있음
- 핵심 패키지 설치 및 버전 확인
- Upstage, Pinecone, LangSmith, Ollama 통합 패키지 설치 확인
- Ollama를 사용할 경우 Runtime과 Model 준비
- `src/00_check_env.py` 실행 후 `핵심 환경 확인: OK`

> `OK`는 현재 PC의 설치·환경변수·패키지 상태가 준비되었다는 뜻입니다. API Key의 실제 유효성, Credit·Quota, Provider 응답은 해당 기능을 사용하는 Step에서 다시 확인합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac8171bf44dd42fb7ad357)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## VS Code에서 실습 폴더 열기

VS Code에서 **File → Open Folder...**를 선택하고 수업에서는 `step00_environment_setup/practice` 폴더를 엽니다. 완성 코드를 확인할 때만 같은 Step의 `complete` 폴더를 엽니다.

터미널에서 폴더를 연 경우에는 다음과 같이 VS Code를 실행할 수도 있습니다.

```bash
cd rag-pipeline-lab2026/step00_environment_setup/practice
code .
```

이 방법은 Step 00에서만 안내합니다. 이후 장에서는 VS Code에서 해당 Step의 `practice/` 폴더를 직접 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 아래 명령을 실행합니다.

## uv와 venv의 차이

`venv`는 프로젝트마다 독립된 가상환경을 만드는 Python 표준 도구입니다. 패키지 설치와 버전 관리는 보통 `pip` 등으로 별도 처리합니다.

`uv`는 가상환경뿐 아니라 **Python 버전, 패키지 설치, 의존성 잠금, 실행**까지 함께 관리합니다.

이 과정에서는 LangChain, LangGraph, FAISS 등 여러 패키지를 함께 사용하므로 수강생마다 같은 환경을 쉽게 구성하고 버전 차이를 줄이기 위해 uv를 사용합니다.

주요 명령:

- Python 준비: `uv python install`
- 의존성 동기화: `uv sync`
- 패키지 추가: `uv add`
- 실행: `uv run --locked python ...`

## uv 설치 및 확인

```bash
uv --version
```

설치되어 있지 않다면 공식 설치 가이드를 참고합니다.

- 공식 문서: https://docs.astral.sh/uv/getting-started/installation/

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

설치 후 VS Code 터미널을 다시 열고 `uv --version`으로 확인합니다.

## Python 3.11 확인

```bash
uv python list --only-installed 3.11
```

Python 3.11이 표시되면 그대로 진행합니다. 없다면 설치합니다.

```bash
uv python install 3.11
```

## 가상환경과 의존성 구성

`.env.example`을 `.env`로 복사하고 기본 실습에서는 `OPENAI_API_KEY`를 설정합니다.

처음에는 다음 명령을 실행합니다.

```bash
uv sync
```

처음 실행하면 uv가 `pyproject.toml`을 기준으로 다음 작업을 수행합니다.

1. 사용할 Python 버전 확인
2. 현재 폴더에 `.venv` 생성
3. 필요한 패키지 설치
4. 의존성 버전을 `uv.lock`에 기록

`.venv`는 실제 패키지가 설치되는 가상환경이고, `uv.lock`은 같은 의존성 버전을 다시 설치할 수 있도록 기록한 파일입니다.

환경 구성이 끝나면 Python 버전을 확인합니다.

```bash
uv run --locked python --version
```

예상 결과:

```text
Python 3.11.x
```

> `uv sync` 전에 `uv run python --version`을 먼저 실행하면 uv가 필요한 환경을 자동으로 구성할 수 있습니다. 이 경우 `.venv` 생성과 패키지 설치 로그가 함께 출력될 수 있습니다. 교재에서는 흐름을 명확히 하기 위해 `uv sync`를 먼저 실행합니다.

Windows에서 다음 경고가 표시될 수 있습니다.

```text
warning: Failed to hardlink files; falling back to full copy.
```

uv 캐시와 프로젝트가 서로 다른 드라이브에 있을 때 나타날 수 있으며, 파일 복사 방식으로 자동 전환됩니다. 설치가 완료되었다면 실습 진행에는 문제가 없습니다.

실제 환경 확인 실습은 교재의 **0.11 환경 확인 프로그램**에서 진행합니다.

`practice/src/00_check_env.py`는 TODO가 포함된 연습용 파일이고, `complete/src/00_check_env.py`는 완성 코드입니다. 연습용 파일의 TODO를 완성한 뒤 실행합니다.

```bash
uv run --locked python src/00_check_env.py
```

## Provider 통합 패키지 사전 점검

Step 00에서는 뒤의 장에서 사용할 가능성이 있는 통합 패키지까지 미리 설치해 설치 가능 여부를 확인합니다.

```bash
uv add langchain-upstage
uv add langchain-pinecone pinecone
uv add langsmith
uv add langchain-ollama
```

설치 후 다시 실행합니다.

```bash
uv run --locked python src/00_check_env.py
```

예상 확인 항목:

```text
[선택 Provider 통합]
Upstage: 설치됨
Pinecone: 설치됨
Ollama: 설치됨

핵심 환경 확인: OK
```

Ollama는 Python 패키지와 별도로 Runtime과 Model도 확인합니다.

```bash
ollama --version
ollama list
```

각 Step은 별도의 `practice/` 환경을 사용하므로 이후 장에서는 해당 Step 폴더에서 `uv sync`로 다시 환경을 구성합니다. Step 00의 목적은 모든 패키지를 한 환경에서 계속 쓰는 것이 아니라, **현재 PC에서 이후 실습 도구를 설치하고 사용할 준비가 되는지 미리 검증하는 것**입니다.

## 확인 원칙

최종 출력만 보지 말고 **Python 버전 → 환경변수 → 핵심 패키지 → Provider 통합 → Runtime** 순서로 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
