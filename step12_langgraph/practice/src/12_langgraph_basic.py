from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    question: str
    normalized_question: str
    length: int


# 12.6~12.7 Node와 State 업데이트
def normalize_question(state: GraphState):
    # TODO 1: question의 앞뒤 공백을 제거해 normalized_question을 반환하세요.
    raise NotImplementedError("TODO 1: normalize_question을 완성하세요.")


def count_length(state: GraphState):
    # TODO 2: normalized_question의 길이를 계산해 length를 반환하세요.
    raise NotImplementedError("TODO 2: count_length를 완성하세요.")


# 12.9 Conditional Edge
def short_question(state: GraphState):
    print("짧은 질문입니다.")
    return {}


def long_question(state: GraphState):
    print("긴 질문입니다.")
    return {}


def route_by_length(state: GraphState):
    # TODO 3: length <= 20이면 "short", 아니면 "long"을 반환하세요.
    raise NotImplementedError("TODO 3: route_by_length를 완성하세요.")


# TODO 4: StateGraph를 만들고 normalize/count_length/short/long Node를 등록하세요.
builder = StateGraph(GraphState)

# 아래 TODO를 교재 12.8~12.9 순서에 따라 완성합니다.
# TODO 4-1: builder.add_node(...)로 네 Node를 등록하세요.
# TODO 4-2: START → normalize → count_length까지 일반 Edge를 연결하세요.
# TODO 5: count_length 뒤에 route_by_length를 이용한 Conditional Edge를 연결하세요.
# TODO 6: short / long을 END에 연결하고 graph = builder.compile()로 컴파일하세요.

# TODO를 완성한 뒤 아래 코드를 주석 해제해 실행합니다.
# result = graph.invoke({
#     "question": "RAG는 왜 필요한가요?",
#     "normalized_question": "",
#     "length": 0,
# })
#
# print("최종 State:", result)
