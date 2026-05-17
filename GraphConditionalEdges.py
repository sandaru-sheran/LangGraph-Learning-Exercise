from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph,START,END
import math

class calculate(TypedDict):
    number1 : int
    number2 : int
    number3 : int
    number4 : int
    operation1 : str
    operation2 : str
    final_result1 : int
    final_result2 : int

def add_node(obj : calculate) -> calculate:
    obj["final_result1"]=obj["number1"]+obj["number2"]
    return obj

def add_node2(obj : calculate) -> calculate:
    obj["final_result2"]=obj["number3"]+obj["number4"]
    return obj

def subtract_node(obj : calculate) -> calculate:
    obj["final_result1"]=obj["number1"]-obj["number2"]
    return obj

def subtract_node2(obj : calculate) -> calculate:
    obj["final_result2"]=obj["number3"]-obj["number4"]
    return obj

def router1(obj : calculate) -> calculate:
    if obj["operation1"] == "+":
        return "addtion-operation"
    else:
        return "subtraction-operation"

def router2(obj : calculate) -> calculate:
    if obj["operation2"] == "+":
        return "addtion-operation2"
    else:
        return "subtraction-operation2"

graph = StateGraph(calculate)

graph.add_node("router1",lambda obj : obj)
graph.add_node("router2",lambda obj : obj)
graph.add_node("add1",add_node)
graph.add_node("add2",add_node2)
graph.add_node("sub1",subtract_node)
graph.add_node("sub2",subtract_node2)

graph.add_conditional_edges("router1",router1,
                            {"addtion-operation":"add1","subtraction-operation":"sub1"})

graph.add_conditional_edges("router2",router2,{"addtion-operation2":"add2","subtraction-operation2":"sub2"})

graph.add_edge("add1","router2")
graph.add_edge("sub1","router2")

graph.add_edge(START,"router1")
graph.add_edge("add2",END)
graph.add_edge("sub2",END)

app=graph.compile()

compute = calculate(number1=5,number2=2,number3=3,number4=2,operation1="+",operation2="+")

result=app.invoke(compute)

print(result["final_result1"])
print(result["final_result2"])