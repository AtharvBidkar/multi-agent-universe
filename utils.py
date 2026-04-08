import anthropic
from config import ANTHROPIC_API_KEY, MODEL_NAME

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def call_claude(prompt):
    try:
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=800,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text

    except Exception as e:
        return f"Error: {str(e)}"