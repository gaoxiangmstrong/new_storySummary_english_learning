import os
import openai
from dotenv import load_dotenv
from chat_module import Question_brain
from story import story
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
brain = Question_brain(story=story)
brain.generate_questions()

continue_loop = True
while continue_loop:
    brain.get_questions()
    response = input("my reponse is :")
    print(brain.ask_question(response))
    print(brain.messages)
