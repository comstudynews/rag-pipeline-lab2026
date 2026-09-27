# Step 03. Text Splitter

문서를 검색하기 좋은 Chunk로 나누고 chunk_size와 overlap을 비교합니다.

- 교재: [해당 장 바로가기](https://app.notion.com/p/3de91bd5a9ac818e9ebac91c98427c50)
- `practice/`: 현재 Step을 직접 완성하는 연습용
- `complete/`: 교재 기준 완성 코드

## 실행

VS Code에서 **File → Open Folder...**를 선택하고 `step03_text_splitter/practice` 폴더를 엽니다. 완성 코드 확인이 필요할 때만 같은 Step의 `complete` 폴더를 엽니다.

VS Code에서 **Terminal → New Terminal**을 연 뒤 의존성을 동기화합니다.

이 Step은 로컬 문서를 분할하는 실습이므로 **API Key가 필요하지 않습니다.**

```bash
uv sync
```

`uv.lock`이 생성된 뒤에는 잠긴 환경으로 실행합니다.

```bash
uv run --locked python src/03_splitter.py
```

## 실습 순서

Step 03은 누적형 폴더입니다. Step 00~02의 코드는 완성 상태로 제공되며, 이번 Step에서는 `practice/src/03_splitter.py`의 TODO를 완성합니다.

1. `chunk_overlap`을 `20`으로 설정
2. `add_start_index`를 `True`로 설정
3. 실행 결과에서 Chunk 수와 `metadata`의 `start_index` 확인

기본 설정은 교재와 동일한 `chunk_size=120`, `chunk_overlap=20`입니다. 교재 3.6의 비교 실습에서는 값을 바꾸어 다시 실행하면서 Chunk 경계와 개수를 비교합니다.



## 확인 원칙

최종 출력만 보지 말고 **입력 → 현재 단계의 처리 → 출력**을 확인합니다. 검색이 포함된 Step에서는 LLM 답변보다 검색된 Document를 먼저 확인합니다.

> 교재의 설명과 코드 순서를 기준으로 진행하고, `complete/`는 복습·오류 비교용으로 사용합니다.
