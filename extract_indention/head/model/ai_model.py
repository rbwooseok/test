from langchain_openai import ChatOpenAI


def get_ai_model():
    model = ChatOpenAI(model="gpt-4o-mini", api_key="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")
    return model
