import openai
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from story import story
from dotenv import load_dotenv
from langchain.schema import HumanMessage
import os


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
# choose the character.

def choose_main_character(story):
  response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": f"read the {story} and give me the prompt for AI picture generation"
    }
  ],)
  print(response['choices'][0]['message']['content'])
  return response['choices'][0]['message']['content']


# create a image out the the main character
response = openai.Image.create(
    prompt=choose_main_character(story=story),
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
