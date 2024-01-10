from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from story import story
# 1. import openai chat
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

# simply using llm to input a prompt return a result


def generate_one_story(character_name, background, story_type):
    # selected openai as LLM and made a template for it also indicate animal_type as input
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=['character_name', "background", "story_type"],
        template="generate of a story of a {character_name} and the background is {background}. The story type is {story_type}"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({'character_name': character_name,
                          'background': background, 'story_type': story_type})
    return response

# def generate_story_summary(story):
#   llm = OpenAI(temperature = 0.7)
#   prompt_template_name = PromptTemplate(
#     input_variables=["story"],
#     template= "write a summary of the {story}"
#   )
#   name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
#   response =name_chain({"story": story})
#   return response
first_question = "ask your first question to start the conversation"

# 2. use the openai chat and ask one question about the generated story.
def chat_response(story_summary):
    chat = ChatOpenAI(temperature=0)
    # persona
    template = (
        "You are Akira. Your task is to assist me in understanding the {story} by asking interactive and step-by-step questions. Your role is to be an enthusiastic and empathetic friend who helps me comprehend the story at a deeper level. Please adapt your questions based on my English proficiency level and encourage me to answer in full sentences. If I make a mistake or misunderstand a question, kindly correct me by referencing back to the story and explaining briefly why I was wrong. Once I have answered all the questions, please share your enthusiasm with me."
    )
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    response = chat(
        chat_prompt.format_prompt(
            story=f"{story_summary}", text=f"{first_question}"
        ).to_messages()
    )
    return response


# 3. get the answer.
if __name__ == "__main__":
    generate_one_story(character_name="steve",
                       background="midage", story_type="adventure")
