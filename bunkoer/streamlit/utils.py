import tempfile
import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def handle_file_upload(uploaded_file):
    _, file_extension = os.path.splitext(uploaded_file.name)
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return SecureFile(tmp_file.name)

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
