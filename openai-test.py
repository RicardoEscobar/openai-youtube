from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Eres una asistente poética, hábil para explicar conceptos complejos de programación con un toque creativo.",
        },
        {
            "role": "user",
            "content": "Componer un poema que explique el concepto de recursividad en programación.",
        },
    ],
)

print(completion.choices[0].message)
