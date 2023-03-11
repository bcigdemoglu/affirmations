# type: ignore
import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


async def query_openai(user_issue: str) -> str:
    prompt: str = f"Write a sentence of affirmation for me as I am dealing with \"{user_issue}\"."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer: str = "I'm sorry, can you try again?"
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']

    return answer.strip()
