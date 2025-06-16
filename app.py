import streamlit as st
import openai

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Ask GPT a question
def ask_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a friendly and polite fitness assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# BMI calculator function
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

# Streamlit app UI
st.title("🏋️‍♂️ Fitness AI Agent")
st.write("Ask fitness-related questions like your BMI, a workout plan, or a diet suggestion.")

# User inputs
question = st.text_input("Ask your fitness question (e.g., 'Suggest me a workout plan')")

with st.expander("Or calculate your BMI"):
    weight = st.number_input("Weight (kg)", min_value=1)
    height = st.number_input("Height (cm)", min_value=1)
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is {bmi}")
        bmi_result = ask_gpt(f"My BMI is {bmi}. Please give me some advice.")
        st.info(bmi_result)

# Handle general questions
if question:
    with st.spinner("Thinking..."):
        answer = ask_gpt(question)
        st.success(answer)
