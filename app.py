import streamlit as st
from openai import OpenAI

# Connect OpenAI using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Chatbot Xafiiska Dakhliga")

st.title("🤖 Chatbot – Xafiiska Dakhliga")
st.write("Ku weydii su’aal ku saabsan canshuuraha iyo adeegyada xafiiska dakhliga")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ku qor su’aashaada halkan...")

if prompt:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # OpenAI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Waxaad tahay chatbot rasmi ah oo u shaqeeya "
                    "Xafiiska Dakhliga Heer Degaan. "
                    "Ku jawaab af-Soomaali, si cad, gaaban, "
                    "oo u hoggaansan habraaca dowladeed."
                ),
            },
            *st.session_state.messages,
        ],
    )

    reply = response.choices[0].message.content

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
