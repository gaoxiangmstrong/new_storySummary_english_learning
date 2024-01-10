# import streamlit dotenv openai
import string
from nltk.corpus import stopwords
import streamlit as st
from langchain.llms.openai import OpenAI
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain_helper import chat_response, first_question
from dotenv import load_dotenv
import openai
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')


# get text from .txt file
def get_text(files):
    text = ""
    for file in files:
        text += file.getvalue().decode('utf-8')
    return [text]

# get summary of the text data


# def get_summary(text_datas):
#     # create prompt to receive text data as prompt
#     llm = OpenAI(max_tokens=1000, model="text-davinci-003", temperature=1.0)
#     prompt = f"write a summary of the text below\n{text_datas}"
#     summary = llm(prompt=prompt)
#     # return result
#     return summary


# def get_shorter_version_summary(text):
    llm = OpenAI(max_tokens=1000, model="text-davinci-003", temperature=1.0)
    prompt = f"Turning the text below into a better version and it should less than 150 words easy to understand and friendly for english second language speaker.\n{text}"
    shorter_summary = llm(prompt=prompt)
    return [shorter_summary]

# write a def to get the response from openai. let the Ai to ask the question first


# use openai embedding turn summary into vectors


def get_vectorstore(text):
    # openai embedding: story to vector
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text, embedding=embeddings)
    return vectorstore


# conversation_chain 包含历史记录的列表里面有object

def get_conversation_chain(vectorstore):
    """return a chain that contain chat_history and vector data"""
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    print(memory.load_memory_variables({}))  # 这里拿到是chathistory
    # 拿到chat_history和vector数据
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain


def handle_userinput(user_question):
    # {chathistory: [{"question":.. }, "response":...]}
    # 1. first answer the first question 2. ask the one questio
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

#


def translate_word(word, target_language):
    """explain the word in english then translate it into chinese"""
    prompt = "explain the word in english then translate it into chinese"
    translations = {"happy": {
        "meaning": "It's a human emotion to show they are cheerfull", "zh-cn": "高兴"}
    }
    return translations.get(word, {}).get(target_language, "Unknown")


# create a dropbox where i can upload a story
def main():
    load_dotenv()

    st.set_page_config(
        page_title="learn english from story", page_icon=":book:")
    st.header("upload your story .txt/PDF")
    # external css
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    user_question = st.text_input("Ask any question you want bro:")
    if "story_content" not in st.session_state:
        st.session_state.story_content = None

    # size bar
    with st.sidebar:
        st.subheader("Your Stories")
        text_files = st.file_uploader(
            "Upload your story in text/PDFs here and click one 'Process' button", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get text data拿到数据
                text_data = get_text(files=text_files)
                words = word_tokenize(text_data[0])
                # send openai request to translate each word. {happy: {meaning: "It's a human emotion to show they are cheerfull", "zh-cn": "高兴"}}
                # remove repeat punctuation, am is are 去掉多余的词汇
                filtered_words = set(word for word in words if word.lower(
                ) not in stopwords.words('english') and word not in string.punctuation)
                with open("output.txt", "w", encoding="utf-8") as file:
                    for word in filtered_words:
                        file.write(word + "\n")

                st.session_state.story_content = text_data
                # get summary of the text_data

                # summary = get_summary(text_data)
                # # turn the summary into a shorter version and it should less than 150 words easy to understand and friendly for english second language speaker
                # shorter_summary = get_shorter_version_summary(summary)
                # get_vectorstore will be stored in vector db
                vectorstore = get_vectorstore(text_data)
                # 保存summary
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)
    # set the story on main
    if st.session_state.story_content is not None:
        st.header("Read the story below")
        st.write(st.session_state.story_content[0])
    if user_question:
        handle_userinput(user_question=user_question)


# compress summary make it more compact
# compressed_summary
# chatbot use the compressed_summary to chat with human

# start
# image generation


# get the text


# create the variations of the main character in different scenes
# def select_four_scenes(story):
#     llm = OpenAI(max_tokens=1000, model="text-davinci-003", temperature=0)
if __name__ == "__main__":
    main()
