from head.graph.state.chatstates import AIStates, UserIntention
from langchain_core.messages import AIMessage

from head.prompts.prompts import *
from head.model.ai_model import get_ai_model
from langchain_core.documents import Document

# 사용자의 의도 추출하기!
def get_intention(state: AIStates):
    
    question = state.get("question")
    prompt = get_indent_prompt()
    llm = get_ai_model()
    llm.with_structured_output(UserIntention)
    
    extract_model = prompt | llm
    output = extract_model.invoke(question)
    print("사용자 의도: ", output.content)
    return { "intent": output.content }

# 사용자의 의도대로 상품 문의일 경우 진행할 내용
def product_qa(state: AIStates):
    """상품 문의 분기 노드

    Args:
        state (AIStates): _description_
    """
    
    print("상품 문의 분기 진입") # 이 부분은 log로 전환이 필요
    # 질문을 얻고
    question = state.get("question")
    prompt = get_product_info_prompt()
    llm = get_ai_model()
    model = prompt | llm
    products_info = ["""상품의 특이사항 및 보험가입자격요건
Ⅰ. 상품의 특이사항
Q1: VIP변액저축보험(무배당)의 특이사항은 무엇인가요?
 A1: VIP변액저축보험(무배당)은 계약자가 납입한 보험료의 일부로 펀드를 구성하고 그 운용실적에 
따라 계약자에게 투자이익을 배분함으로써 보험기간 중에 보험금 및 해지환급금 등이 변동하
는 변액보험입니다. 변액보험은 다음과 같은 특징이 있습니다.
 ① 이 상품은 실적배당형 상품이므로 사망보험금 및 해지환급금이 특별계정의 운용실적에 따
라 변동됩니다.
 ② 이 상품은 중도해지시 해지환급금은 펀드의 운용실적에 따라 변동되므로 최저보증이 이루
어지지 않으며 원금손실이 발생할 수 있습니다. 다만, 특별계정의 운용실적이 악화될 경우
에도 최저사망보험금은 보장됩니다.
 ③ “최저사망보험금”은 특별계정 운용실적과 관계없이 보장하는 최저한도의 사망보험금으로서 
사망시점의 “이미 납입한 보험료”를 말합니다. 다만, 보험료 감액 또는 계약자적립금(다만, 
보험계약대출의 원금과 이자를 차감한 금액)의 중도인출이 있었을 경우 이미 납입한 보험
료는 주계약 약관에서 정하는 방법에 따라 계산합니다. 최저사망보험금 보증을 위해 매월 
최저사망보험금 보증비용이 계약자적립금에서 공제됩니다. 다만, 일반계정으로 전환된 경
우에는 더 이상 최저사망보험금을 보증하지 않습니다.
 A1: 1종(장기강화형)은 장기환급률이 높은 반면 해지공제가 있고, 2종(단기강화형)은 해지공제가 
없어 단기환급률이 높은 반면 장기환급률이 낮으므로, 고객의 가입목적에 따라 합리적으로 비
교 선택하여야 합니다. 또한, 보험계약 체결 시 1종(장기강화형) 및 2종(단기강화형) 중 하나
만 선택할 수 있으며, 보험기간 중에 변경할 수 없습니다""", ]
    output = model.invoke(input={"question": question, "products_info": products_info})
    
    return {"messages": AIMessage(content=output.content), "products_info": products_info}


def product_select(state: AIStates):
    """상품 선택 분기 노드
    Args:
        state (AIStates): _description_
    """
    print("상품 선택 분기 진입") # 이 부분은 log로 전환이 필요
    # 질문을 얻고
    question = state.get("question")
    prompt = get_product_select_prompt()
    llm = get_ai_model()
    model = prompt | llm
    products = ["무배당 오렌지단체상해보험","오렌지 퍼펙트 유니버셜종신보험", "VIP변액저축보험 무배당"]
    output = model.invoke(input={"question": question, "products": products})
    
    return {"messages": AIMessage(content=output.content), "products": products}

def document_select(state: AIStates):
    """문서 선택 분기 노드

    Args:
        state (AIStates): 
    """
    print("문서 선택 분기 진입") # 이 부분은 log로 전환이 필요
    
    question = state.get("question")
    prompt = get_document_select_prompt()
    llm = get_ai_model()
    model = prompt | llm
    documents = [Document(page_content="""3.2 보험료에 관한 사항 
가. 기본보험료 
(1) 거치형: 계약자가 보험계약 체결 시 납입하는 일시납 보험료를 말한다.  
일시납 기본보험료는 1,000만원 이상으로 한다. 
(2) 적립형: 계약자가 보험계약 체결 시 매월 납입하기로 한 월납 보험료를 말한다. 
월납 기본보험료는 2,3년납은 매월 50만원 이상, 5년납 이상은 매월 20만원 이상으로 한다. 
나. 추가납입보험료의 최저한도 
(1) 거치형 
계약자는 회사가 별도로 정한 추가납입보험료의 최저한도(2021년 1월 1일 기준 10만원) 이상으로 납
1 
입해야 하며, 최저한도가 변경되었을 경우에는 변경된 시점부터 납입하는 추가납입보험료에 대하여 변
경된 최저한도를 적용한다."""), Document(page_content="""무배당 오렌지단체상해보험(갱신형) 판매방침 
1. 변경판매일자: 2008년 4월 1일 - 현재 판매중인 상품(보종코드:96520)은 2008년 4월 1일부터 2009년 3월 31일까지  
기존 계약단체의 추가계약만 판매하고 2009년 4월 1일자로 판매중지함 
2. 주요 변경내용 
1) 약관 변경 - 한국표준질병사인 분류 개정에 따른 변경 및 약관 문구(용어) 정비 - 금융감독원의 “불합리한 보험약관의 개선 요청”에 의거 약관의 지급사유 조사,
확인시 회사지정의사 진단 요구 개선 - 가족관계등록에 관한 법률시행으로 인한 문구 변경 : 호적 → 가족관계등록부 
2) 무배당 단체수술특약을 무배당 단체수술Ⅱ특약(갱신형)으로 변경 판매 개시
                            """)]
    output = model.invoke(input={"documents": documents, "question": question})
    
    return {"messages": AIMessage(content=output.content)}

def question_select(state: AIStates):
    """질문 선택 분기 노드

    Args:
        state (AIStates): _description_
    """
    print("질문 선택 분기 진입")
    
    question = state.get("question")
    prompt = get_question_select_prompt()
    llm = get_ai_model()
    model = prompt | llm
    before_questions = ["생명보험을 선택하는 기준을 알려줘", "저축보험을 선택하는 기준을 알려줘"]
    output = model.invoke(input={"before_questions": before_questions, "question": question})
    
    return {"messages": AIMessage(content=output.content), "before_questions": before_questions}

def common_question(state: AIStates):
    """일반 질문 선택 분기 노드

    Args:
        state (AIStates): _description_
    """
    print("일반 질문 분기 진입")
    
    question = state.get("question")
    prompt = get_common_question_prompt()
    llm = get_ai_model()
    model = prompt | llm
    output = model.invoke(input=question)
    
    return {"messages": AIMessage(content=output.content)}
