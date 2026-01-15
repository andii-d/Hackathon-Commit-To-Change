import os
from opik import configure
from opik.integrations.langchain import OpikTracer
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from prompt import prompt

OPENAI_API_KEY="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"
OPIK_API_KEY = "jqHFYaCyiUk2YsgyBwgGHJZiU"
configure(api_key=OPIK_API_KEY)
opikTracer = OpikTracer()
os.environ["OPENAI_API_KEY"] = OPIK_API_KEY


def build_agent():
    llm = ChatOpenAI(
        callbacks=[opikTracer],
        model="xiaomi/mimo-v2-flash:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENAI_API_KEY,
        temperature=0
    )

    return create_agent(
        model=llm,
        system_prompt=prompt
    )

