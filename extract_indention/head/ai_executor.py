
from head.graph.graph_agent import get_graph_agent
from langchain_core.messages import HumanMessage


def get_response(question):
    graph = get_graph_agent()
    result = graph.invoke(input = {"question": question, "messages": HumanMessage(content=question)})
    print(result.get("messages"))
    print(result.get("output"))
    return result.get("output")
