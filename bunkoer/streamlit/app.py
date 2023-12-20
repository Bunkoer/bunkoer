import streamlit as st  # Streamlit for creating web apps
from streamlit_chat import message  # Streamlit chat for creating chat interfaces
from langchain.embeddings.openai import OpenAIEmbeddings  # OpenAI embeddings for NLP tasks
from langchain.chat_models import ChatOpenAI  # Chat model from Langchain for OpenAI-based chat
from langchain.chains import ConversationalRetrievalChain  # A chain for conversational retrieval
from langchain.document_loaders.csv_loader import CSVLoader  # Loader for CSV documents
from langchain.vectorstores import FAISS  # FAISS for efficient similarity search
import tempfile  # For creating temporary files
import os  # For interacting with the operating system
# Secure file handling from bunkoer library
from bunkoer.security import SecureFile
from bunkoer.utils.gpt import send_gpt_request
from bunkoer.txt.text_task import anonymize_text, deanonymize_text


def main():
    
    # Sidebar uploader for CSV files
    uploaded_file = st.sidebar.file_uploader("upload", type="csv")
    user_input = ""

    # Handling the uploaded file
    if uploaded_file:
        input_folder = 'file/input'
        output_folder = 'file/output'
        _, file_extension = os.path.splitext(uploaded_file.name)  # Extracting file extension
        input_file_path = os.path.join(input_folder, uploaded_file.name)
        output_file_path = ""

        with open(input_file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
            original_cwd = os.getcwd()
            try:
                os.chdir(output_folder)
                safe_output = SecureFile(f"../input/{uploaded_file.name}")
                output_file_path = os.path.join(output_folder, safe_output)
            finally:
                os.chdir(original_cwd)        
    
            try:
                loader = CSVLoader(file_path=output_file_path, encoding="utf-8")  # Trying to load the file with utf-8 encoding
                data = loader.load()
            except:
                loader = CSVLoader(file_path=output_file_path, encoding="cp1252")  # Fallback to cp1252 encoding if utf-8 fails
                data = loader.load()

        loader = CSVLoader(file_path=output_file_path, encoding="utf-8", csv_args={'delimiter': ','})  # Loading the CSV file
        data = loader.load()

        embeddings = OpenAIEmbeddings()  # Initializing OpenAI embeddings
        vectorstore = FAISS.from_documents(data, embeddings)  # Creating a vector store from the data and embeddings

        # Setting up the conversational retrieval chain
        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=1, model_name='gpt-4-1106-preview'),  # Configuring the chat model
            retriever=vectorstore.as_retriever()  # Setting up the retriever with the vector store
        )

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
            print("User input", user_input)
            output = send_gpt_request(user_input , model="gpt-4-1106-preview", temperature=0.7, max_tokens=None)
            print ("BEFORE : ", output)
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
                output = conversational_chat(user_input)  # Handling the chat functionality
                st.session_state['past'].append(user_input)  # Updating past queries
                st.session_state['generated'].append(output)  # Updating generated responses
            elif submit_button and user_input :
                user_input = anonymize_text(user_input)
                output = conversational_chat(user_input)  # Handling the chat functionality
                st.session_state['past'].append(user_input)  # Updating past queries
                st.session_state['generated'].append(output)  # Updating generated responses

    # Displaying the conversation history
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user',
                        avatar_style="big-smile")  # Displaying user's messages
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")  # Displaying AI's responses

