from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    question: str
    normalized_question: str
    length: int


def normalize_question(state: GraphState):
    # TODO 1: question의 앞뒤 공백을 제거해 normalized_question을 반환하세요.
    raise NotImplementedError


def count_length(state: GraphState):
    # TODO 2: normalized_question의 길이를 계산해 length를 반환하세요.
    raise NotImplementedError


def short_question(state: GraphState):
    print("짧은 질문입니다.")
    return {}


def long_question(state: GraphState):
    print("긴 질문입니다.")
    return {}


def route_by_length(state: GraphState):
    # TODO 3: length <= 20이면 short, 아니면 long을 반환하세요.
    raise NotImplementedError


# TODO 4: StateGraph에 Node와 Edge를 등록하세요.
# TODO 5: count_length 뒤에 Conditional Edge를 연결하세요.
# TODO 6: short / long을 END에 연결하고 compile/invoke하세요.

print("TODO: Step 12 LangGraph를 완성하세요.")
