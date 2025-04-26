def Normal_LLM(query, llm1, chat_history ,model_name="", instruction=""):

    full_query = "\n".join([f"User: {q}\nAssistance: {a}" for q, a in chat_history])
    full_query += f"\nUser: {query}"

    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm1.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content

    return result