from typing import *
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    message : str


llm = ChatOpenAI(
    temperature=0.9,
    model_name="Your Model Name",
    base_url="Your Base URL",
    api_key="lm-studio"
)


def agent(obj : AgentState) -> AgentState:
    obj["message"]=llm.invoke(obj["message"]).content
    return obj

graph = StateGraph(AgentState)

graph.add_node("agent",agent)
graph.add_edge(START,"agent")
graph.add_edge("agent",END)

app = graph.compile()

message = input("Enter Your Message :")

while message != "exit":
    message = input("Enter Your Message :")
    result = app.invoke({"message": message})
    print(result["message"])

