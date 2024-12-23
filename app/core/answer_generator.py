import openai
import os

openai.api_key = os.getenv("OPEN_AI_KEY")

def generate_answer_from_context(question: str, context: str):
    print("OpenAI API Key:", os.getenv("OPEN_AI_KEY"))  # Ensure the key is printed for debugging
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Specify the model you'd like to use
        prompt=f"Question: {question}\nContext: {context}\nAnswer:",
        max_tokens=150
    )
    answer = response['choices'][0]['text'].strip()
    return answer