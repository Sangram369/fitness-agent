import streamlit as st
from openai import OpenAI
import os

# Load OpenAI API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful fitness assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.set_page_config(page_title="Fitness AI Agent", page_icon="🏋️", layout="centered")
st.title("🏋️ Fitness AI Agent")
st.write("Ask me anything related to your fitness, workout, BMI or diet plan.")

question = st.text_input("Ask your fitness question:")

if question:
    with st.spinner("Getting your answer..."):
        try:
            answer = ask_gpt(question)
            st.success("Here's your advice:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
