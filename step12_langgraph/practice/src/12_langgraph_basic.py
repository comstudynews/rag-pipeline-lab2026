from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    question: str
    normalized_question: str
    length: int


def normalize_question(state: GraphState):
    # TODO: question의 앞뒤 공백을 제거해 normalized_question을 반환하세요.
    raise NotImplementedError


def count_length(state: GraphState):
    # TODO: normalized_question의 길이를 계산해 length를 반환하세요.
    raise NotImplementedError


# TODO: StateGraph에 Node, Edge, Conditional Edge를 연결하세요.
print("TODO: Step 12 LangGraph를 완성하세요.")
