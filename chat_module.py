from story import story
from persona import akira
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class Chat:
    def __init__(self, story):
        self.conversation_history = [
            {"role": "system", "content": f"{akira}"},
            {"role": "user", "content": f"Let's begin with the {story}. you need to keep asking untill I understand the story"}
        ]
    # get the last message content
    def get_last_message_content(self):
        return self.conversation_history[-1]["content"]

    # check the last message
    def is_last_message_from_AI(self):
        last_message = self.conversation_history[-1]
        if last_message["role"] == "assistant":
            return True
        return False

    # send request to Openai to add system_message
    def add_system_message(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation_history,
            temperature=0.8
        )
        system_message = response['choices'][0]['message']['content']
        self.conversation_history.append(
            {"role": "assistant", "content": system_message})
        
    # get message from ai 
    def get_system_message(self):
        # if last message role in list if role
        if self.is_last_message_from_AI():
            message_from_ai = self.conversation_history[-1]["content"]
            return message_from_ai
        
    # get user message 
    def get_user_message(self):
        if self.is_last_message_from_AI() == False:
            user_message = self.get_last_message_content()
            return user_message

    # add user_input
    def add_user_message(self, user_message):
        self.conversation_history.append(
            {"role": "user", "content": user_message})

    # get conversation history
    def get_conversation_history(self):
        return self.conversation_history


# chat = Chat(story)
# while True:
#     # if last message_is system message
#     if chat.is_last_message_system():
#         user_message = input("your answer: ")
#         chat.add_user_message(user_message)
#     else:
#         chat.add_system_message()
#     # no matter what print conversation history
#     print(chat.get_conversation_history())
