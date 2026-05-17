from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph
import math

class user(TypedDict):
    name : str
    age : str
    skill : List[str]
    results : str


def first_node(obj : user) -> user:
    obj["results"]=obj["name"]+" Welcome To The System!"
    return obj

def secend_node(obj : user) -> user:
    obj["results"]=obj["results"]+" You Are "+obj["age"]+" Years Old"
    return obj

def third_node(obj : user) -> user:
    skills=""
    for skill in obj["skill"]:
        skills=skills+skill+" "

    obj["results"]=obj["results"]+" Your Skills Are "+skills
    return obj



graph = StateGraph(user)

graph.add_node("first_node",first_node)
graph.add_node("secend_node",secend_node)
graph.add_node("third_node",third_node)

graph.add_edge("first_node","secend_node")
graph.add_edge("secend_node","third_node")

graph.set_entry_point("first_node")
graph.set_finish_point("third_node")

app=graph.compile()

result=app.invoke({ "name" : "sandaru","age":"25","skill":["python","java","c++"]})

print(result["results"])