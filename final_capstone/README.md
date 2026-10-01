# Step 14. 종합실습

교재: [14. 종합실습 | RAG Pipeline 설계·개발·평가](https://app.notion.com/p/3e391bd5a9ac81009f9dd93ed6f78b1f)

## 실습 폴더

- `practice/`: 수강생이 직접 작성하는 종합실습
- `complete/`: 오류 확인과 코드 비교를 위한 참고용 예제
- `practice/results/design.md`: 문제 정의와 설계 기록
- `practice/results/evaluation.md`: Baseline과 개선 결과 기록

종합실습 결과는 `practice/`에서 작성한 코드와 `results/`의 기록을 기준으로 확인합니다.

## 실행

VS Code에서 `final_capstone/practice` 폴더를 엽니다.

macOS / Linux:

```bash
cp .env.example .env
uv sync
uv run --locked python src/capstone_compare.py
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
uv sync
uv run --locked python src/capstone_compare.py
```

기본 예시는 OpenAI Embedding과 Chat Model을 사용하므로 `.env`에 `OPENAI_API_KEY`를 설정합니다. 실제 API Key가 들어 있는 `.env`는 Git에 올리지 않습니다.

## 교재와 실습 코드 대응

`practice/src/capstone_compare.py`의 TODO 1~7은 현재 교재의 다음 흐름과 대응합니다.

1. **14.3** 문제와 문서 범위 정의
2. **14.4** Baseline RAG 구현
3. **14.5** 8~10개의 고정 테스트 질문 작성
4. **14.6 / 14.8** Baseline Retrieval 결과 확인
5. **14.7** 관찰된 문제에 맞는 개선 전략 적용
6. **14.8** 동일 질문셋으로 Baseline과 개선 Pipeline 비교 및 Generation 확인
7. **14.9~14.10** 설계·평가 결과와 한계 정리, 제출 전 점검

`complete/src/capstone_compare.py`는 Similarity Baseline과 MMR 개선안을 비교하는 참고 예제입니다. 다른 전략을 선택해도 되지만, 반드시 동일한 질문셋으로 전·후 결과를 비교하고 선택 이유를 설명해야 합니다.

## 제출물

다음 세 파일을 완성합니다.

- `practice/src/capstone_compare.py`
- `practice/results/design.md`
- `practice/results/evaluation.md`

## 완료 기준

- 문서 로드 → Chunk → Embedding → Vector Store → Retriever → Prompt → Chat Model 흐름이 실행됩니다.
- 검색된 문서를 직접 확인할 수 있습니다.
- 8~10개의 테스트 질문으로 Baseline 결과를 먼저 기록합니다.
- 문제에 맞는 개선 전략을 최소 1개 적용합니다.
- 동일 질문셋으로 개선 전·후를 비교합니다.
- 문서에 없는 질문은 Retrieval Hit Rate에서 제외하고, Generation 단계에서 근거 없는 답변을 만들지 않는지 확인합니다.
- 개선되지 않은 결과가 있다면 원인이나 한계를 기록합니다.
- `results/design.md`와 `results/evaluation.md`를 완성합니다.

상세 진행 일정과 제출 기준은 Notion 교재의 14장을 확인합니다. Wrap-up Quiz는 수업 중 별도 Google Form으로 안내합니다.
