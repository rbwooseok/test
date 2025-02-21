
from pydantic import BaseModel, Field

from langgraph.graph import MessagesState
from langchain_core.documents import Document

# 갖고 있어야 할 상태들 - 질문내용, 그리고 질문의 내용이 해당되는 내용을 판별하는 내용, 질문 - 응답 내역, 참조한 링크

class AIStates(MessagesState):
    question: str # 사용자가 최초로 한 질문 > 가공되지 않은 사용자의 질문
    intent: str # 사용자의 질문 의도
    products: list[str] # 상품 목록
    products_info: list[str] # 상품 설명 목록
    documents: list[Document] # 문서 선택 목록
    before_questions: list[str] # 질문 목록


# 사용자의 의도를 한 단어로 추출한 것 > 의도 추출에 사용
class UserIntention(BaseModel):
    intent: str = Field(description="사용자의 의도를 한 단어로 답할 것. [상품정보, 상품선택, 문서선택, 질문선택, 일반질문] 중의 하나로만 답할 것")
