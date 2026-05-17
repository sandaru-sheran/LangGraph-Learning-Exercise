from asyncio import graph
from typing import List, Dict, TypedDict
import langgraph
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name : str


def complement(name : AgentState) -> AgentState:
    name["name"] = name["name"]+" You are Good"
    return name

graph = StateGraph(AgentState)

graph.add_node("complement",complement)

graph.set_entry_point("complement")
graph.set_finish_point("complement")

app=graph.compile()

result=app.invoke({ "name" : "sandaru"})

print(result["name"])