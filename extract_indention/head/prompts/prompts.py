from langchain.prompts import ChatPromptTemplate


def get_indent_prompt() -> ChatPromptTemplate:
    """사용자 의도 추출 프롬프트 획득

    Returns:
        ChatPromptTemplate: Prompt template을 돌려줌
    """
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "사용자의 질문을 받아 사용자의 질문의 의도를 구분하여 사용자의 질문이 보험과 관련된 질문일 경우 상품정보, 상품선택, 문서선택, 질문선택 중의 넷 중의 하나로 판단하고, 그렇지 않을 경우 일반질문으로 판단할 것"),
            ("user", "{question}")
        ]
    )
    return prompt

def get_product_info_prompt() -> ChatPromptTemplate:
    """
    상품 정보 프롬프트 획득
    Returns:
        ChatPromptTemplate: _description_
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "사용자의 질문을 받아 사용자의 질문에 가장 적합한 상품의 정보를 돌려줄 것, 상품의 정보는 products쪽에 있음, 해당 상품의 내용과 사용자의 질문을 확인하여 응답하기 가장 적합한 내용을 돌려줄 것"),
            ("user", "products: {products_info}\n question: {question}")
        ]
    )
    return prompt

def get_product_select_prompt() -> ChatPromptTemplate:
    """
    상품 선택 프롬프트 획득
    Returns:
        ChatPromptTemplate: _description_
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "사용자의 질문을 받아 사용자의 질문에 가장 적합한 상품 이름을 댈 것, 상품들은 products라는 곳에 상품 이름 목록이 들어있음, 해당 상품의 이름을 보고, 추천할 상품의 이름을 돌려줄 것"),
            ("user", "products: {products}\n question: {question}")
        ]
    )
    return prompt

def get_document_select_prompt() -> ChatPromptTemplate:
    """문서 선택 프롬프트 획득

    Returns:
        ChatPromptTemplate: _description_
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "문서의 목록을 확인하고, 사용자 질문과 가장 유사한 문서의 목록을 보여주기, 문서 목록은 documents라는 곳에 들어있고, documents의 이름, 내용을 보고, 사용자의 질문에 가장 적합한 문서를 돌려줄 것"),
            ("user", "documents: {documents}\n question: {question}")
        ]
    )
    return prompt



def get_question_select_prompt() -> ChatPromptTemplate:
    """질문 선택 프롬프트 획득

    Returns:
        ChatPromptTemplate: _description_
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "사용자의 질문에 이전에 있던 질문, 응답 내역을 불러와서 사용자의 질문과 가장 유사한 질문 목록을 보여줄 것 이전 질문 목록은 before_questions 쪽에 들어있고, 사용자의 질문과 가장 가까운 질문을 최대 3개를 돌려줄 것"),
            ("user", "before_questions: {before_questions}\n question: {question}")
        ]
    )
    return prompt


def get_common_question_prompt() -> ChatPromptTemplate:
    """일반 질문 프롬프트 획득

    Returns:
        ChatPromptTemplate: _description_
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "사용자의 질문을 받아 사용자의 질문에 대한 응답을 하기, 아는 한도 내에서만 응답하고, 그에 대한 정보가 없을 경우 해당되는 정보는 제공된 곳에 없다고 할 것"),
            ("user", "{question}")
        ]
    )
    return prompt


