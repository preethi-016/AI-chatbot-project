import openai

class AI_Assistant:
    def __init__(self):
        # Set API key directly in the code
        openai.api_key = "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"
        
        # Prompt
        self.full_transcript = [
            {"role": "system", "content": "You are an HR representative at HR Shop International, Mumbai. Be resourceful and efficient."},
        ]

    # Pass user input to OpenAI and generate a response
    def generate_ai_response(self, user_input):
        # Append the user input to the conversation history
        self.full_transcript.append({"role": "user", "content": user_input})

        # Generate response from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.full_transcript
        )

        # Extract AI response
        ai_response = response['choices'][0]['message']['content']
        
        # Append the AI response to the conversation history
        self.full_transcript.append({"role": "assistant", "content": ai_response})

        # Print the AI response
        print(f"HR Shop International: {ai_response}\n")

# Initialize the assistant
ai_assistant = AI_Assistant()

# Example of interacting with the chatbot
while True:
    user_input = input("Candidate: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    ai_assistant.generate_ai_response(user_input)
