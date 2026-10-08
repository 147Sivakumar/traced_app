from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain what LangChain is in simple terms.",
    "Give me three practical uses of LangSmith for debugging an AI application.",
    "Explain why tracing is useful when building an AI application."
]

for i, prompt in enumerate(prompts, 1):
    response = llm.invoke(prompt)

    print(f"\n--- Run {i} ---")
    print(f"Prompt: {prompt}")
    print(f"Answer: {response.content}")