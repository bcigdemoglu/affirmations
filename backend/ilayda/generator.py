# type: ignore
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


async def query_openai(user_issue: str) -> str:
    prompt: str = f"Never exceed 20 words. Write a sentence of affirmation for me as I am dealing with the issue written between three backticks (```) using first person: ```{user_issue}```"
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

    if 'choices' in response and len(response['choices']) > 0:
        answer = response['choices'][0]['text']

    return answer.strip()


async def query_hugging_face(user_issue: str) -> str:
    prompt: str = f"Never exceed 20 words. Write a sentence of affirmation for me as I am dealing with the issue written between three backticks (```) using first person: ```{user_issue}```"
    headers = {
        'Authorization': f'Bearer {os.getenv("HUGGINGFACE_API_KEY")}',
        'Content-Type': 'application/json',
    }

    payload = {
        'inputs': f"<s>[INST] {prompt} [/INST]"
    }

    response = requests.post(
        'https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2',
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        ai_response = response.json()
        if ai_response and len(ai_response) > 0 and 'generated_text' in ai_response[0]:
            generated_text = ai_response[0]['generated_text']
            return generated_text.split('[/INST]')[1].trim() if '[/INST]' in generated_text else "ERROR: AI response formatting issue."
        else:
            return "ERROR: AI response is invalid."
    else:
        return f"ERROR: API call failed with status code {response.status_code}"
