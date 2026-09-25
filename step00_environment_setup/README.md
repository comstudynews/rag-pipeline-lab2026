# Step 00. 개발환경·API Key 준비

Python 3.11, uv, API Key, 선택 Provider와 실습환경을 준비합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac8171bf44dd42fb7ad357)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## uv 설치

먼저 uv 설치 여부를 확인합니다.

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

설치 후 터미널을 다시 열고 `uv --version`으로 확인합니다.

## Python 3.11 확인

실습은 Python 3.11을 사용합니다.

```bash
uv python list --only-installed 3.11
```

Python 3.11이 표시되면 그대로 진행합니다. 없다면 설치합니다.

```bash
uv python install 3.11
```

## VS Code에서 실습 폴더 열기

`practice/`와 `complete/`는 각각 `pyproject.toml`을 가진 독립 실행 폴더입니다.

VS Code에서 **File → Open Folder...**를 선택하고 수업에서는 `step00_environment_setup/practice` 폴더를 엽니다. 완성 코드를 확인할 때만 같은 Step의 `complete` 폴더를 엽니다.

터미널에서 폴더를 연 경우에는 다음과 같이 VS Code를 실행할 수도 있습니다.

```bash
cd rag-pipeline-lab2026/step00_environment_setup/practice
code .
```

이 방법은 Step 00에서만 안내합니다. 이후 장에서는 VS Code에서 해당 Step의 `practice/` 폴더를 직접 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 명령을 실행합니다.

1. `.env.example`을 `.env`로 복사합니다.
2. 기본 실습은 `OPENAI_API_KEY`를 설정합니다.
3. 최초 1회 의존성을 동기화합니다.

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/00_check_env.py
```



## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
