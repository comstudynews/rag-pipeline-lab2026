from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    question: str
    normalized_question: str
    length: int


def normalize_question(state: GraphState):
    # 앞뒤 공백을 제거해 다음 Node에서 사용할 값을 만듭니다.
    normalized = state["question"].strip()
    return {"normalized_question": normalized}


def count_length(state: GraphState):
    # 이전 Node가 만든 normalized_question의 길이를 계산합니다.
    return {"length": len(state["normalized_question"])}


def short_question(state: GraphState):
    print("짧은 질문입니다.")
    return {}


def long_question(state: GraphState):
    print("긴 질문입니다.")
    return {}


def route_by_length(state: GraphState):
    # State의 length 값으로 다음 Node를 선택합니다.
    if state["length"] <= 20:
        return "short"
    return "long"


builder = StateGraph(GraphState)

builder.add_node("normalize", normalize_question)
builder.add_node("count_length", count_length)
builder.add_node("short", short_question)
builder.add_node("long", long_question)

builder.add_edge(START, "normalize")
builder.add_edge("normalize", "count_length")

builder.add_conditional_edges(
    "count_length",
    route_by_length,
    {
        "short": "short",
        "long": "long",
    },
)

builder.add_edge("short", END)
builder.add_edge("long", END)

graph = builder.compile()

result = graph.invoke({
    "question": "RAG는 왜 필요한가요?",
    "normalized_question": "",
    "length": 0,
})

print("최종 State:", result)
