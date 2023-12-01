import requests
import json
import os

from langchain.llms.openai import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI


def send_gpt_request(input_message, model, temperature, max_tokens):
    API_KEY = os.environ.get('OPENAI_API_KEY')
    API_ENDPOINT = "https://api.openai.com/v1/chat/completions"


    messages = [
        #{"role": "system", "content": "You are a helpful assistant."}, Can be useful for set the beavior 
        {"role": "user", "content": f"{input_message}"}
    ]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    
    if max_tokens is not None:
        data["max_tokens"] = max_tokens
    
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"[ERROR] Gpt request : {response.status_code}: {response.text}")
    
def embeding(temperature, model_name, user_input, base_file):
    if os.path.isfile(base_file):
        try:
            loader = CSVLoader(file_path=base_file, encoding="utf-8")
            data = loader.load()
        except:
            loader = CSVLoader(file_path=base_file, encoding="cp1252")
            data = loader.load()

        embeddings = OpenAIEmbeddings()
        vectors = FAISS.from_documents(data, embeddings)
        llm = ChatOpenAI(temperature=temperature, model_name=model_name)
        qa = RetrievalQA.from_chain_type(llm=llm,
                                         chain_type="stuff",
                                         retriever=vectors.as_retriever(),
                                         verbose=True)

        def conversational_chat(query):
            result = qa.run(query)
            answer = result
            return answer

        response_text = conversational_chat(user_input)
        return response_text
    else:
        return "Error the file is empty"
