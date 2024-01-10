import streamlit as st
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from persona import akira
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


# load the story from st.session_state.story_content
# if st.session_state.story_content is not None:
#     st.write(st.session_state.story_content)


def chat_page():
    load_dotenv()
    st.set_page_config(
        page_title="Your story understanding helper",
        page_icon="🤖"
    )


def main():
    chat_page()

    chat_model = ChatOpenAI()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content=akira), HumanMessage(
                content=st.session_state.story_content[0])
        ]

    # get the story content from session_state
    # get the akira

    with st.sidebar:
        # clear button
        clear_button = st.button(label="Rest", type="primary")
        if clear_button:
            st.session_state.messages = [
                SystemMessage(content=akira), HumanMessage(
                    content=st.session_state.story_content[0])
            ]

        user_input = st.text_input("User Input:", key="user_input")
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))

    response = chat_model(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    print(st.session_state.messages)

    messages = st.session_state.get('messages', [])
    # show all messages
    for i, msg in enumerate(messages[2:]):
        if i % 2 == 0:
            # ai message first
            message(msg.content, is_user=False, key=str(i) + '_ai')
        else:
            # human response
            message(msg.content, is_user=True, key=str(i) + '_user')

    print(messages)


main()
