import streamlit as st
import openai

# Set OpenAI API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# GPT function using latest OpenAI SDK (v1.x)
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or use "gpt-3.5-turbo" if free
        messages=[
            {"role": "system", "content": "You are a polite and friendly fitness assistant who answers fitness-related queries like BMI, workout plans, and diet suggestions."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

# Streamlit app UI
st.set_page_config(page_title="Fitness AI Agent", page_icon="🏋️", layout="centered")
st.title("🏋️ Fitness AI Agent")
st.write("Ask me anything related to your fitness, BMI, workout, or diet. I'm here to help politely!")

# Input from user
question = st.text_input("Ask your fitness question:")

if question:
    with st.spinner("Thinking..."):
        try:
            answer = ask_gpt(question)
            st.success("Here's your personalized fitness advice:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
