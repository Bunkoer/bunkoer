import streamlit as st
from .config import configure_page
from .ui import display_headers, upload_file_sidebar, create_chat_interface

def main():
    configure_page()
    display_headers()
    uploaded_file = upload_file_sidebar()

    if uploaded_file:
        file_secure = handle_file_upload(uploaded_file)
        data, vectorstore = process_uploaded_data(file_secure)
        initialize_conversational_chain(data, vectorstore)
        initialize_session_states()
        create_chat_interface()

    create_chat_interface()


