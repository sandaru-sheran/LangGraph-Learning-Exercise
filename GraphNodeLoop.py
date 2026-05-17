from asyncio.windows_events import NULL
from typing import List, Dict, TypedDict
from langgraph.graph import StateGraph,START,END
import random

class setup(TypedDict):
    name:str
    attempts : int
    lowerBound : int
    upperBound : int
    higher: bool
    correctNumber : int
    final_result2 : int
    guesses : List[int]

def setupgame(obj : setup) -> setup:
    obj["attempts"]=0
    obj["correctNumber"]=random.randint(obj["lowerBound"],obj["upperBound"])
    return obj

def guess(obj : setup) -> setup:
    if obj["higher"]==None:
        obj["guesses"].append(random.randint(obj["lowerBound"],obj["upperBound"]))
    elif obj["higher"]:
        obj["lowerBound"]=obj["guesses"][-1]
        obj["guesses"].append(random.randint(obj["guesses"][-1],obj["upperBound"]))

    else:
        obj["upperBound"]=obj["guesses"][-1]
        obj["guesses"].append(random.randint(obj["lowerBound"],obj["guesses"][-1]))

    obj["attempts"]+=1
    return obj

def check(obj : setup) -> setup:
    if obj["attempts"]>7:
        return END

    if obj["correctNumber"]==obj["guesses"][-1]:
        return END

    return "evaluvate"

def evaluvate(obj : setup) -> setup:
    if obj["correctNumber"]>obj["guesses"][-1]:
        obj["higher"]=True
    else:
        obj["higher"]=False

    return obj

graph = StateGraph(setup)

graph.add_node("setupgame",setupgame)
graph.add_node("guess",guess)
graph.add_node("evaluvate",evaluvate)


graph.add_edge(START,"setupgame")
graph.add_edge("setupgame","guess")
graph.add_edge("evaluvate","guess")
graph.add_conditional_edges("guess",check,{"evaluvate":"evaluvate",END:END})



app=graph.compile()

compute = setup(
    name="sandaru",
    attempts=7,
    lowerBound=1,
    upperBound=10,
    higher=None,
    correctNumber=0,
    final_result2=0,
    guesses=[]
)

result=app.invoke(compute)

print(result)