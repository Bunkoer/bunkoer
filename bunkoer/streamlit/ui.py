import streamlit as st
from streamlit_chat import message

def display_headers():
    st.markdown("<div style='text-align: center;'><h1>Bunkoer Secure Your Data</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><h4>AI Conversations With Trust</h4></div>", unsafe_allow_html=True)

def upload_file_sidebar():
    return st.sidebar.file_uploader("Upload", type="csv")

def create_chat_interface():
    container = st.container()
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:",
                                       key='input')
            submit_button = st.form_submit_button(label='Send')
            if submit_button and user_input:
                output = conversational_chat(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

def display_conversation_history(response_container):
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user',
                        avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")

