import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()


def get_model(model_name="groq:openai/gpt-oss-120b", temperature=0.5):
    """
    Returns a standardized Langchain model instance.
    """
    return init_chat_model(
        model_name,
        temperature=temperature,
        configurable_fields=("model", "model_provider"),
    )


model = get_model()
