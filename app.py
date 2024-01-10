import langchain_helper as lch
import streamlit as st


st.title("story generator")

character_name = st.sidebar.selectbox("What is the main character of the story", ("steve", "mark", "david", "xiang"))

background = st.sidebar.selectbox("what is the background of the story", ("midage", "futuristic", "7BC", "after distinction of human civilization", "The last human on earth", "universe"))

story_type = st.sidebar.selectbox("what is the story type", ("adventure", "romance", "evil", "fight", "success"))


# generate story according to parameters(通过参数生成故事)
one_story = lch.generate_one_story(character_name=character_name, background=background, story_type=story_type)

print(lch.response)


process_btn= st.sidebar.button("Process")
if process_btn:
  with st.spinner("Processing"):
    st.write(one_story["text"])


