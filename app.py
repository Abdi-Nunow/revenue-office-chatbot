import streamlit as st
from gpt4all import GPT4All

# Initialize model (local)
model = GPT4All("ggml-gpt4all-j-v1.3-groovy")  # download model ka GPT4All website

st.title("🤖 Chatbot Xafiiska Dakhliga – Offline/Free")

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

    # Model response
    response = model.generate(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
