import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.set_page_config(page_title="Chatbot Xafiiska Dakhliga")


st.title("🤖 Chatbot – Xafiiska Dakhliga")
st.write("Ku weydii su’aal ku saabsan canshuuraha, adeegyada, ama waraaqaha rasmiga ah")


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


response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "Waxaad tahay chatbot u shaqeeya Xafiiska Dakhliga Heer Degaan, kuna jawaaba af-Soomaali si rasmi ah."},
*st.session_state.messages
]
)


reply = response.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": reply})


with st.chat_message("assistant"):
st.markdown(reply)
