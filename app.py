import streamlit as st
from transformers import pipeline

# -------------------------------
# Initialize Hugging Face chatbot
# -------------------------------
# model-ka free online hosted
chatbot = pipeline("text-generation", model="tiiuae/gpt4-x-alpaca", device=-1)

# -------------------------------
# Streamlit page setup
# -------------------------------
st.set_page_config(page_title="Chatbot Xafiiska Dakhliga", layout="centered")
st.title("🤖 Chatbot – Xafiiska Dakhliga")
st.write("Ku weydii su’aal ku saabsan canshuuraha iyo adeegyada xafiiska dakhliga")

# -------------------------------
# Initialize chat session
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Display previous messages
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# User input
# -------------------------------
prompt = st.chat_input("Ku qor su’aashaada halkan...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # -------------------------------
    # Generate response
    # -------------------------------
    try:
        response = chatbot(prompt, max_length=200)[0]['generated_text']

        # Save assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    except Exception as e:
        st.error(f"AI chatbot error: {str(e)}")
