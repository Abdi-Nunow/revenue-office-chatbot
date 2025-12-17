import streamlit as st
from transformers import pipeline

# Initialize chatbot pipeline (Hugging Face)
chatbot = pipeline("text-generation", model="tiiuae/gpt4-x-alpaca", device=-1)

st.title("🤖 Chatbot Xafiiska Dakhliga – Free Online")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ku qor su’aashaada halkan...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = chatbot(prompt, max_length=200)[0]['generated_text']
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
