from typing import TypedDict


class State(TypedDict):
    my_var: str
    customer_name: str # customer name

# Define nodes (Each node is like an Agent-like a Graph)


def node_1(state: State) -> State:
    state["my_var"] = "Hello!"
    state["customer_name"] = "Jorge"
    return state

def node_2(state: State) -> State:
    customer_name = state["customer_name"]
    state["my_var"] = f"Hello {customer_name}!" 
    return state

def node_3(state: State) -> State:
    return state

# Now its time to install langgraph
"""
poetry add langgraph  # pip install langgraph

poetry add langchain-openai  # pip install langchain-openai

poetry add python-dotenv  # pip install python-dotenv

"""

from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)

builder.add_node("node_1", node_1)    #"node_1" is the name of the node (unique for each node)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()

"""
poetry add "langgraph-cli[inmen]"
"""