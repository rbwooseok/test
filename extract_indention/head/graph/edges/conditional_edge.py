from head.graph.state.chatstates import AIStates

# 사용자의 의도대로 분기 나누기
def divide_route(state: AIStates):
    """사용자의 의도를 추출하여 분기를 나누어 실행하도록 하는 기준에 따라 노드를 선택하도록 결정해주는 함수
    사용자의 의도는 지금 현재는 다섯가지의 형태 
    처음 들어온 사용자의 질문을 다섯가지 분기로 추출하여, 추출된 의도대로 노드를 나누는 기준이 될 것
    

    Args:
        state (AIStates): chat 모두 공통, 공용으로 활용, 참조하는 상태
    
    Returns:
        str : 루트를 선택하는 기준이 되는 글귀
    """
    output = state.get("intent")
    if output.find("상품정보") != -1:
        output = "상품정보"
    elif output.find("상품선택") != -1:
        output = "상품선택"
    elif output.find("문서선택") != -1:
        output = "문서선택"
    elif output.find("질문선택") != -1:
        output = "질문선택"
    elif output.find("일반질문") != -1:
        output = "일반질문"
    print("사용자 의도 분기 처리 함수 호출 ", output)
    return output
