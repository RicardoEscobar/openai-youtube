from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def get_response(
    prompt: str,
    system: str = "Eres una asistente poética, hábil para explicar conceptos complejos de programación con un toque creativo.",
) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return completion.choices[0].message.content


def main():
    system = input("System: ")
    print("=== Chatbot configurado ===")
    while True:
        prompt = input("Prompt: ")
        response = get_response(prompt, system)
        print(f"IA: {response}")
        continue_loop = input("Continuar? (s/n):")
        if continue_loop != "s":
            break


if __name__ == "__main__":
    main()
