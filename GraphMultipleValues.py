from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph
import math

class AgentState(TypedDict):
    name : str
    valuess : List[int]
    operation : str


def operate(name : AgentState) -> AgentState:
    if name["operation"] == "+":
        name["name"]="Hi "+name["name"]+" "+str(sum(name["valuess"]))
    else:
        name["name"]="hi "+name["name"]+" "+str(math.prod(name["valuess"]))
    return name


graph = StateGraph(AgentState)

graph.add_node("operate",operate)

graph.set_entry_point("operate")
graph.set_finish_point("operate")

app=graph.compile()

result=app.invoke({ "name" : "sandaru","valuess":[5,2,3],"operation": "*"})

print(result["name"])