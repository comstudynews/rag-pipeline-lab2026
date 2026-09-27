# Step 12. RAG Flow Pattern과 LangGraph 입문

State, Node, Edge, Conditional Edge로 RAG Workflow의 흐름 제어를 이해합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac816bae30f3eb793623f3)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## 실행

VS Code에서 **File → Open Folder...**를 선택하고 `step12_langgraph/practice` 폴더를 엽니다. 완성 코드 확인이 필요할 때만 같은 Step의 `complete` 폴더를 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 의존성을 동기화합니다.

이 Step은 LangGraph의 흐름 제어만 확인하므로 **API Key가 필요하지 않습니다.**

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/12_langgraph_basic.py
```

## 실습 순서

Step 12는 누적형 폴더입니다. Step 00~11의 코드는 완성 상태로 제공되며, 이번 Step에서는 `practice/src/12_langgraph_basic.py`를 완성합니다.

1. **12.6~12.7** State를 갱신하는 Node 구현
2. **12.8** 일반 Edge 연결
3. **12.9** Conditional Edge와 분기 함수 구현
4. `short` / `long` 경로를 `END`에 연결하고 Graph 컴파일
5. 실행 결과의 최종 State 확인

이 Step은 LangGraph의 State/Node/Edge 구조만 다루므로 **OpenAI API Key가 필요하지 않습니다.**

## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
