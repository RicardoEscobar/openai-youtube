from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

def stream_response(
    prompt: str,
    system: str = "Eres una asistente poética, hábil para explicar conceptos complejos de programación con un toque creativo.",
):
    stream_text = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": system,
            },
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    # Iterate over the stream and yield the content of each chunk
    for chunk in stream_text:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

def main():
    prompt_text = input("prompt: ")
    stream = stream_response(prompt_text)
    for chunk in stream:
        print(chunk, end="")


if __name__ == "__main__":
    main()
