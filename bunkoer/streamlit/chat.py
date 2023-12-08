from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def initialize_session_states():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Upload a file for begin "]
    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]

def conversational_chat(query):
    chain = st.session_state['chain']
    result = chain({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]
