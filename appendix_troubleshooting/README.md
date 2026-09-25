# 부록. RAG 실습에서 자주 발생하는 오류와 해결 방법

교재: [부록 원문](https://app.notion.com/p/3de91bd5a9ac81b0a7f6d1a437da0373)

각 Step의 `practice/` 또는 `complete/` 폴더에서 실행하는 현재 저장소 구조를 기준으로 정리했습니다.

---

## A.1 먼저 확인할 기본 원칙
*그림: 문제를 순서대로 좁혀 가는 문제 해결 흐름 예시 — 출처: *[*Wikimedia Commons*](https://commons.wikimedia.org/wiki/File:Problem-Solving.svg)*, Public Domain*
RAG 실습 오류는 코드 자체보다 **실행 위치, 가상환경, API Key, 패키지 설치 상태**에서 발생하는 경우가 많습니다.
오류가 발생하면 다음 순서로 확인합니다.
① VS Code에서 해당 Step의 `practice/` 또는 `complete/` 폴더를 열었는가?  
② VS Code 터미널에서 처음 실행할 때 `uv sync`를 실행했는가?  
③ 이후 실행은 `uv run --locked python ...` 형식인가?  
④ 현재 작업 폴더의 `.env`에 필요한 API Key가 있는가?  
⑤ 파일 경로가 현재 작업 폴더의 `data/`, `src/` 구조와 일치하는가?
각 Step은 다음 구조를 사용합니다.
```plain text
stepXX_topic/
├── README.md
├── practice/
│   ├── .env
│   ├── .env.example
│   ├── pyproject.toml
│   ├── data/
│   └── src/
└── complete/
    └── ...
```
## A.2 `uv: command not found`
### 원인
`uv`가 설치되지 않았거나 설치 후 현재 터미널이 새 PATH를 읽지 못한 경우입니다.
### 확인
```bash
uv --version
```
### 해결
`uv`를 설치한 뒤 터미널을 완전히 닫고 다시 엽니다. VS Code를 사용한다면 새 Terminal을 생성합니다.
## A.3 `No module named ...`
예:
```plain text
ModuleNotFoundError: No module named 'langchain_openai'
```
### 원인
- 현재 Step에서 `uv sync`를 실행하지 않음
- 시스템 Python으로 실행함
- 다른 Step의 가상환경을 사용함
### 해결
VS Code에서 **File → Open Folder...**로 `step01_basic_rag/practice` 폴더를 열고 새 터미널에서 실행합니다.
```bash
uv sync
uv run --locked python src/01_basic_rag.py
```
필요한 패키지가 `pyproject.toml`에 없다면 그때 추가합니다.
```bash
uv add langchain-openai
```
## A.4 `OPENAI_API_KEY` 오류
예:
```plain text
The api_key client option must be set
```
또는 인증 관련 오류가 발생할 수 있습니다.
### 확인할 것
① 현재 Step 폴더에 `.env`가 있는가?  
② 환경 변수명이 정확히 `OPENAI_API_KEY`인가?  
③ 코드에서 `load_dotenv()`를 호출했는가?  
④ Key 앞뒤에 불필요한 공백이 없는가?
`.env` 예시:
```plain text
OPENAI_API_KEY=본인의_API_KEY
```
API Key를 Python 소스에 직접 적거나 GitHub에 업로드하지 않습니다. `.env`는 `.gitignore`에 포함합니다.
## A.5 `FileNotFoundError: data/sample.txt`
### 원인
상대경로는 **VS Code에서 연 작업 폴더**를 기준으로 해석됩니다. 저장소 루트를 열어 둔 상태에서 하위 Step의 파일만 실행하면 `data/sample.txt` 경로가 맞지 않을 수 있습니다.

### 권장 실행
VS Code에서 **File → Open Folder...**로 `step08_rag_pipeline/practice` 폴더를 열고 새 터미널에서 실행합니다.

```bash
uv run --locked python src/08_rag_pipeline.py
```

VS Code Explorer의 최상위 폴더가 현재 Step의 `practice/` 또는 `complete/`인지 확인합니다.
## A.6 한글이 깨지거나 `UnicodeDecodeError`가 발생하는 경우
TXT Loader를 사용할 때 인코딩을 명시합니다.
```python
loader = TextLoader(
    "data/sample.txt",
    encoding="utf-8",
)
```
원본 파일 자체가 UTF-8이 아니라면 VS Code에서 파일 인코딩을 확인한 뒤 UTF-8로 저장합니다.
## A.7 PDF를 읽었는데 `page_content`가 비어 있는 경우
### 가능한 원인
PDF 안에 실제 텍스트가 없고 페이지가 스캔 이미지로만 구성되어 있을 수 있습니다.
### 확인
```python
print(docs[0].page_content)
```
거의 빈 문자열이라면 일반 PDF Loader만으로 텍스트를 가져오기 어려울 수 있습니다.
### 대응
- 텍스트 기반 PDF인지 확인
- OCR이 필요한 문서인지 확인
- 표·레이아웃 보존이 중요한 경우 별도의 문서 파싱 도구 검토
단순히 Loader를 바꾸기 전에 **원본 PDF가 어떤 형태인지** 먼저 확인합니다.
## A.8 FAISS 설치 또는 import 오류
예:
```plain text
No module named 'faiss'
```
### 확인
```bash
uv add faiss-cpu
uv sync
```
그 다음 Python에서 확인합니다.
```bash
uv run --locked python -c "import faiss; print('FAISS OK')"
```
환경에 따라 바이너리 패키지 설치 문제가 발생할 수 있습니다. 이 경우 Python 버전과 운영체제 아키텍처를 먼저 확인합니다.
```bash
uv run --locked python --version
uv run --locked python -c "import platform; print(platform.machine())"
```
## A.9 Embedding API 호출에서 오류가 발생하는 경우
### 확인할 것
- API Key가 유효한가
- 네트워크 연결이 가능한가
- 모델 이름이 현재 계정에서 사용 가능한가
- 호출 한도나 결제 한도를 초과하지 않았는가
기본 예시는 다음 모델명을 사용합니다.
```python
OpenAIEmbeddings(model="text-embedding-3-small")
```
모델 관련 오류가 발생하면 별도로 안내된 모델명이 있는지 먼저 확인합니다.
## A.10 `429` 또는 Rate Limit 오류
많은 Embedding 또는 LLM 요청을 짧은 시간에 반복하면 호출 제한 관련 오류가 발생할 수 있습니다.
### 실습에서 줄이는 방법
- 같은 문서를 매번 다시 Embedding하지 않기
- 테스트할 문서 수를 줄이기
- 반복문 안에서 불필요한 LLM 호출 제거
- Reranker 실습에서 후보 문서 수를 너무 크게 잡지 않기
예를 들어 교육용 LLM Reranker에서 후보를 50개씩 평가하면 API 호출이 크게 늘어납니다. 처음에는 5개 내외로 확인하는 것이 좋습니다.
## A.11 검색 결과가 엉뚱한 경우
오류 메시지는 없지만 결과가 이상할 수 있습니다. 이 경우는 실행 오류가 아니라 **검색 품질 문제**입니다.
다음 순서로 확인합니다.
```plain text
1. 원본 문서에 정답이 있는가?
2. Loader가 정답을 정상적으로 읽었는가?
3. Splitter가 정답 문장을 잘라 버리지 않았는가?
4. Retriever가 어떤 Chunk를 가져왔는가?
5. Top-K가 적절한가?
6. 키워드 검색이 필요한 질문인가?
```
반드시 Retriever 결과부터 출력합니다.
```python
docs = retriever.invoke(question)

for doc in docs:
    print(doc.page_content)
```
## A.12 답변이 문서에 없는 내용을 만들어 내는 경우
먼저 검색 결과를 확인합니다.
정답 근거가 검색되지 않았다면 Prompt만 고쳐서는 해결하기 어렵습니다.
Prompt에는 최소한 다음 규칙을 넣습니다.
```plain text
제공된 문서에 있는 내용만 근거로 답하세요.
문서에서 확인할 수 없는 내용은 추측하지 마세요.
확인할 수 없으면 확인할 수 없다고 답하세요.
```
그 다음에도 문제가 지속되면 검색 품질, Context 양, Prompt 구성, 모델 출력을 차례로 확인합니다.
## A.13 BM25 사용 시 `rank_bm25` 관련 오류
예:
```plain text
ImportError: Could not import rank_bm25
```
### 해결
```bash
uv add rank-bm25
uv sync
```
그 다음 다시 실행합니다.
```bash
uv run --locked python src/10_search_quality.py
```
## A.14 LangGraph에서 State Key 오류가 발생하는 경우
예:
```plain text
KeyError: 'retry_count'
```
### 원인
Node에서 사용하는 State Key가 초기 State에 없거나 이름이 다를 수 있습니다.
초기값을 확인합니다.
```python
initial_state = {
    "original_question": question,
    "question": question,
    "context": "",
    "answer": "",
    "relevance": "",
    "retry_count": 0,
}
```
State 정의와 실제 Key 이름이 일치해야 합니다.
## A.15 LangGraph가 계속 반복되는 경우
Agentic RAG에서 다음 흐름이 반복될 수 있습니다.
```plain text
retrieve → grade → rewrite → retrieve → grade → rewrite → ...
```
### 원인
- 종료 조건이 없음
- 관련성 평가가 계속 BAD를 반환
- 재시도 횟수를 State에서 관리하지 않음
### 해결
반복 횟수 제한을 둡니다.
```python
if state["retry_count"] >= 2:
    return "fallback"
```
Loop를 설계할 때는 반드시 **종료 조건**도 함께 설계합니다.
## A.16 Ollama Local 연결 오류
대표 증상은 Local Server 연결 실패 또는 Model을 찾지 못하는 경우입니다.
확인 순서:
① Ollama가 설치되어 있고 실행 중인지 확인합니다.  
② 사용할 Model이 내려받아져 있는지 확인합니다.  
③ 코드의 Model 이름과 로컬 목록의 이름이 같은지 확인합니다.  
④ `langchain-ollama`가 현재 실습 환경에 포함되어 있는지 확인합니다.
```bash
ollama list
```
Ollama Local은 외부 인증 정보가 필요 없지만 **로컬 서버가 실제로 실행 중이어야** 합니다. Cloud 인증 문제와 Local Server 연결 문제를 구분하세요.
## A.17 Cloud Provider 인증 오류
Cloud Provider에서 인증 실패가 발생하면 00장에서 만든 `.env`의 변수명, 값의 앞뒤 공백, 사용 권한, Project 또는 Index 존재 여부를 확인합니다. 실제 인증 값은 화면 공유, 제출 파일, Git 저장소에 넣지 않습니다.
## A.18 Chroma Local과 Cloud 설정을 혼동한 경우
Chroma는 Local In-Memory, Local Persistent, Server, Cloud 방식이 있으므로 설정이 서로 다릅니다. Local 예제와 Cloud 예제의 연결 방식을 섞지 말고 **지금 사용하는 방식이 Local인지 Cloud인지** 먼저 확인합니다.
## A.19 Embedding Provider를 바꾼 뒤 검색 결과가 이상한 경우
Embedding Model을 바꿨다면 기존 Vector Store를 그대로 재사용하지 않습니다. Model마다 벡터 차원과 표현 공간이 다를 수 있으므로 문서를 새 Model로 다시 Embedding하고 Index를 다시 생성합니다.
## A.20 오류를 질문할 때 함께 보내면 좋은 정보
다음 정보를 함께 보내면 원인 파악이 빨라집니다.
① 전체 오류 메시지의 마지막 10\~20줄  
② 실행한 명령어  
③ 문제가 난 파일명  
④ Python 버전  
⑤ `pyproject.toml`의 관련 패키지  
⑥ 현재 폴더 구조  
⑦ 가능하면 문제가 발생한 코드 앞뒤 10줄
예:
```plain text
실행 명령:
uv run --locked python src/08_rag_pipeline.py

Python:
3.11.x

오류:
ModuleNotFoundError: ...
```
단순히 "안 됩니다"라고 전달하는 것보다 재현 가능한 정보를 함께 주는 것이 좋습니다.
---
**오류를 해결한 뒤에는 해당 장의 코드를 처음부터 다시 실행하여 중간 출력과 최종 결과를 함께 확인하세요.**
[첫 화면으로 돌아가기](https://app.notion.com/p/3de91bd5a9ac81219435d1f41cc050df)
