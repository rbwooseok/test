from langgraph.graph import StateGraph

from head.graph.state.chatstates import AIStates

from head.graph.nodes.nodes import *
from head.graph.edges.conditional_edge import divide_route
from langgraph.graph.state import END


def get_graph_agent():
    """langgraph를 이용한 agent 작성 방식
    node 들을 구성
    edge로 node들 간 연결 관계 구성
    conditional_edge로 node간 분기 결정
    Returns:
        _type_: 
    """
    graph_builder = StateGraph(AIStates)
    
    graph_builder.add_node("extract_intention", get_intention)
    
    graph_builder.add_node("product_info", product_qa)
    
    graph_builder.add_node("product_select", product_select)
    
    graph_builder.add_node("document_select", document_select)
    
    graph_builder.add_node("question_select", question_select)
    
    graph_builder.add_node("common_question", common_question)
    
    graph_builder.set_entry_point("extract_intention")
    
    graph_builder.add_conditional_edges("extract_intention", divide_route, {
        "상품정보": "product_info",
        "상품선택": "product_select",
        "문서선택": "document_select",
        "질문선택": "question_select",
        "일반질문": "common_question"})
    
    graph_builder.add_edge("product_info", END)
    graph_builder.add_edge("product_select", END)
    graph_builder.add_edge("document_select", END)
    graph_builder.add_edge("question_select", END)
    graph_builder.add_edge("common_question", END)
    
    graph = graph_builder.compile()
    return graph
