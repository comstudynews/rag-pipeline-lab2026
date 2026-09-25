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

## 실행

1. `practice/` 또는 `complete/`로 이동합니다.
2. `.env.example`을 `.env`로 복사합니다.
3. 기본 실습은 `OPENAI_API_KEY`를 설정합니다.
4. 최초 1회 의존성을 동기화합니다.

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
