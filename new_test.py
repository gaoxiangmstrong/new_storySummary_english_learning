from story import story
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize conversation history
conversation_history = [
    {"role": "system", "content": f"You will ask questions about the until I understand the story.\n story:{story}"},
    {"role": "user", "content": "Let's begin. you need to keep asking untill I understand the story"}
]

while True:
    # Get the last message from the conversation
    last_message = conversation_history[-1]

    if last_message['role'] == 'system':
        # If the last message was from the system, get user input
        user_input = input("You: ")
        conversation_history.append({"role": "user", "content": user_input})
    else:
        # If the last message was from the user, send a request to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.8
        )

        # Get the system message from the response
        system_message = response['choices'][0]['message']['content']
        print(f"System: {system_message}")

        # Append the system message to the conversation history
        conversation_history.append(
            {"role": "system", "content": system_message})
    print(conversation_history)