# Step 07. Prompt + LLM

앞 Step의 완성 코드에 이번 단계의 기능을 추가합니다.

## 폴더
- `practice/`: 이번 Step의 핵심 부분에 `TODO`가 있습니다.
- `complete/`: 이번 Step까지 누적된 완성 코드입니다.

## 실행
1. `practice/` 또는 `complete/`로 이동합니다.
2. `.env.example`을 `.env`로 복사하고 OpenAI API Key를 입력합니다.
3. `uv sync`를 실행합니다.
4. `uv run python src/07_prompt_llm.py`을 실행합니다.

## 확인
검색 Context가 출력되고, 그 근거를 사용한 최종 답변이 이어서 출력되는지 확인합니다.
