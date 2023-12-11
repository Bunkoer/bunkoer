import tempfile
import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

import os
import tempfile

def handle_file_upload(uploaded_file):
    input_folder = 'file/input'
    output_folder = 'file/output'

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    _, file_extension = os.path.splitext(uploaded_file.name)

    input_file_path = os.path.join(input_folder, uploaded_file.name)

    with open(input_file_path, 'wb') as f:
        f.write(uploaded_file.getvalue())

    output_file_name = 'output' + file_extension
    output_file_path = os.path.join(output_folder, output_file_name)

    return output_file_path 


def process_uploaded_data(file_secure):
    try:
        loader = CSVLoader(file_path=file_secure, encoding="utf-8")
        data = loader.load()
    except:
        loader = CSVLoader(file_path=file_secure, encoding="cp1252")
        data = loader.load()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(data, embeddings)
    return data, vectorstore
