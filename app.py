import streamlit as st
from openai import OpenAI
import time  # for sleep

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ... code-ka intiisa kale sida hore ...

# Retry for any exception (instead of RateLimitError)
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Waxaad tahay chatbot rasmi ah..."},
            *st.session_state.messages,
        ],
    )
except Exception:
    st.warning("API error dhacay. Fadlan sug 1 daqiiqo kadib isku day mar kale.")
    time.sleep(60)
