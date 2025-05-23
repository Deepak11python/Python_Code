# Import the OpenAI package to interact with the GPT models
import openai

# Set your OpenAI API key to authenticate requests
openai.api_key = "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"


# Initialize a conversation history list
# Each message is a dictionary with "role" ('system', 'user', or 'assistant') and "content"
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def ask_gpt(prompt, model="gpt-4.1", temperature=0.7):
    # Add the user's question to the conversation log, preserving full chat context
    conversation.append({"role": "user", "content": prompt})
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation,
            temperature=temperature
        )
        reply = response['choices'][0]['message']['content']
        conversation.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main loop for interactive conversation with the GPT assistant via the console.
    
    """
    # Continuously ask for user input until they type 'exit' or 'quit'
    print("🤖 GPT-4.1 Chatbot - Type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = ask_gpt(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
