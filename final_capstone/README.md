# Step 14. 종합실습 및 Wrap-up Quiz

교재: [14. 종합실습 및 Wrap-up Quiz](https://app.notion.com/p/3e391bd5a9ac81009f9dd93ed6f78b1f)

## 실습 폴더

- `practice/`: 수강생이 직접 완성하는 종합실습
- `complete/`: 교재 기준 예시 완성 코드
- `results/design.md`: 설계 산출물 기록
- `results/evaluation.md`: Baseline과 개선 결과 기록

VS Code에서 `final_capstone/practice` 폴더를 열어 진행합니다. 예시 완성 코드를 확인할 때만 `complete/`를 사용합니다.

## 실행

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

`practice/src/capstone_compare.py`의 TODO 1~7은 교재의 14.2~14.13 흐름과 대응합니다.

1. **14.2** 해결할 문제와 문서 범위 정의
2. **14.3** Baseline RAG 구성
3. **14.4** 8~10개의 고정 테스트 질문셋 작성
4. **14.5 / 14.8** Baseline Retrieval 평가
5. **14.6** 관찰된 문제에 맞는 개선 전략 적용
6. **14.7 / 14.8** 동일 질문셋으로 Baseline과 개선 Pipeline 비교 및 Generation 확인
7. **14.9~14.13** 설계·평가·실행 방법과 한계 정리

예시 `complete/src/capstone_compare.py`는 **Similarity Baseline과 MMR 개선안**을 비교합니다. 다른 전략을 선택해도 되지만, 반드시 동일한 질문셋으로 전·후 결과를 비교하고 선택 이유를 설명해야 합니다.

## 완료 기준

- 문서 로드 → Chunk → Embedding → Vector Store → Retriever → Prompt → Chat Model 흐름이 실행됩니다.
- 검색된 문서를 직접 확인할 수 있습니다.
- Baseline 결과를 먼저 기록합니다.
- 문제에 맞는 개선 전략을 최소 1개 적용합니다.
- 동일 질문셋으로 개선 전·후를 비교합니다.
- 문서에 없는 질문은 Retrieval Hit Rate에서 제외하고, Generation 단계에서 근거 없는 답변을 만들지 않는지 확인합니다.
- `results/design.md`, `results/evaluation.md`, 프로젝트 README를 정리합니다.

상세 개념, 평가 기준, Wrap-up Quiz는 Notion 교재의 14장을 기준으로 확인합니다.
