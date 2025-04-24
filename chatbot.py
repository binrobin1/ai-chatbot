import openai

# Replace 'your-api-key-here' with your actual OpenAI API key
openai.api_key = 'your-api-key-here'

def ask(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        reply = ask(user_input)
        print("Bot:", reply)
