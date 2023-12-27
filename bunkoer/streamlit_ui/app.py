import streamlit as st  # Streamlit for creating web apps
from streamlit_chat import message  # Streamlit chat for creating chat interfaces
import tempfile  # For creating temporary files
import os  # For interacting with the operating system
from .utils import handle_file
# Secure file handling from bunkoer library
from bunkoer.utils.gpt import send_gpt_request
from bunkoer.format.text_task import anonymize_text, deanonymize_text



def main():
    
    # Sidebar uploader for CSV files
    uploaded_file = st.sidebar.file_uploader("upload")
    user_input = ""

    # Handling the uploaded file
    if uploaded_file:
        chain = handle_file(uploaded_file)
        # Initializing session state for secure file
        if 'secure_file' not in st.session_state:
            st.session_state['generated'] = ["Your file is now secure to use on any AI, Ask me anything about it " + uploaded_file.name + " 🤗"]
            
    # Function for handling conversational chat
    def conversational_chat(query):
        # Initialize result as a dictionary
        result = {}

        # Check if a file is uploaded and handle accordingly
        if uploaded_file:
            result = chain({"question": query, "chat_history": st.session_state['history']})
        else:
            output = send_gpt_request(user_input , model="gpt-4-1106-preview", temperature=0.7, max_tokens=None)
            print ("ANSWER OF GPT : ", output)
            output = deanonymize_text(output)
            result["answer"] = output

        # Append the query and the answer to the session state history
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]
    
    # Initializing various states for the conversation
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Upload a file for begin "]
    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]

    # Setting up the response container in the Streamlit app
    response_container = st.container()
    container = st.container()

    # Creating the chat interface
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:",
                                    key='input')  # Input field for user query
            submit_button = st.form_submit_button(label='Send')  # Send button
            if submit_button and user_input and uploaded_file :
                _, file_extension = os.path.splitext(uploaded_file.name)  # Extracting file extension
                output = conversational_chat(user_input)  # Handling the chat functionality
                st.session_state['past'].append(user_input)  # Updating past queries
                if file_extension == ".pdf":
                    output = deanonymize_text(output)
                    st.session_state['generated'].append(output)  # Updating generated responses
                else:
                    st.session_state['generated'].append(output)  # Updating generated responses
            elif submit_button and user_input :
                st.session_state['past'].append(user_input)  # Updating past queries
                user_input = anonymize_text(user_input)
                print ("SEND TO GPT : ", user_input)
                output = conversational_chat(user_input)  # Handling the chat functionality
                st.session_state['generated'].append(output)  # Updating generated responses

    # Displaying the conversation history
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user',
                        avatar_style="big-smile")  # Displaying user's messages
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")  # Displaying AI's responses

