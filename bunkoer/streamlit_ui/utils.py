import os
import PyPDF2
from langchain.chat_models import ChatOpenAI  # Chat model from Langchain for OpenAI-based chat
from langchain.chains import ConversationalRetrievalChain  # A chain for conversational retrieval
from langchain.document_loaders.csv_loader import CSVLoader  # Loader for CSV documents
from langchain.vectorstores import FAISS  # FAISS for efficient similarity search
from langchain.embeddings.openai import OpenAIEmbeddings  # OpenAI embeddings for NLP tasks

from bunkoer.security import SecureFile


def handle_file(uploaded_file):
    input_folder = 'file/input'
    output_folder = 'file/output'
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    _, file_extension = os.path.splitext(uploaded_file.name)  # Extracting file extension
    input_file_path = os.path.join(input_folder, uploaded_file.name)
    output_file_path = ""
    
    if input_file_path.endswith(".csv"):
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
            llm=ChatOpenAI(temperature=0.7, model_name='gpt-4-1106-preview'),  # Configuring the chat model
            retriever=vectorstore.as_retriever()  # Setting up the retriever with the vector store
            )
        return chain 
    
    if input_file_path.endswith(".pdf"):
        documents = []
        with open(input_file_path, 'wb') as file:
            file.write(uploaded_file.getvalue())
            original_cwd = os.getcwd()
            try:
                os.chdir(output_folder)
                safe_output = SecureFile(f"../input/{uploaded_file.name}")
                output_file_path = os.path.join(output_folder, safe_output)
            finally:
                os.chdir(original_cwd)  
            
            pdf_reader = PyPDF2.PdfReader(output_file_path)
            
            for page_number, page in enumerate(pdf_reader.pages):
                page_text  = page.extract_text()
                document = type('Document', (object,), {
                        'page_content': page_text, 
                        'metadata': {'page_number': page_number}  
                    })                
                documents.append(document)
        
        embeddings = OpenAIEmbeddings()  # Initializing OpenAI embeddings
        vectorstore = FAISS.from_documents(documents, embeddings)  # Creating a vector store from the data and embeddings

        # Setting up the conversational retrieval chain
        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.7, model_name='gpt-4-1106-preview'),  # Configuring the chat model
            retriever=vectorstore.as_retriever()  # Setting up the retriever with the vector store
            )
        return chain 
