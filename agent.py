from llm import build_agent

agent = build_agent()

while True:
    user_input = input("Ask something: ")

    if user_input.casefold() in ["exit", "quit"]:
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}
    )

    print("AI:", response["messages"][-1].content)
