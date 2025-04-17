import streamlit as st
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from langchain_groq import ChatGroq

llm = chat = ChatGroq(
    temperature = 0,
    model='deepseek-r1-distill-llama-70b'
)

st.set_page_config(page_title='Chat Deepseek', layout='centered')
st.title('Deepseek Test')

# Checking if session has any state, if not create one
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Attributes session state and message history to chat
messages = st.session_state['messages']
for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)

# Chat
in_message = st.chat_input('Send your message:')
if in_message:
    # Appends human messages to chat history
    messages.append(('human', in_message))
    chat = st.chat_message('human')
    chat.markdown(in_message)
    
    response = llm.invoke(messages).content
    # Appends ai messages to chat history
    messages.append(('ai', response))
    chat = st.chat_message('ai')
    chat.markdown(response)
