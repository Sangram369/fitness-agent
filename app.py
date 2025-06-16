import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def ask_gpt(question):
    prompt = f"You are a polite and helpful fitness assistant. Answer clearly and kindly.\n\nUser: {question}\n\nAssistant:"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a friendly fitness coach."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def calculate_bmi(weight, height):
    try:
        bmi = weight / ((height/100)**2)
        return round(bmi, 2)
    except:
        return None

# Streamlit UI
st.title("🏋️‍♂️ Fitness AI Assistant")
st.write("Ask me anything about fitness, diet, or workouts!")

question = st.text_input("Your Question")

with st.expander("📊 Or Calculate Your BMI"):
    weight = st.number_input("Your weight (kg)", min_value=20.0, max_value=300.0)
    height = st.number_input("Your height (cm)", min_value=100.0, max_value=250.0)
    if weight and height:
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is {bmi}")
        if bmi < 18.5:
            st.info("You're underweight. Focus on protein-rich diet and strength workouts.")
        elif 18.5 <= bmi < 25:
            st.success("You have a healthy weight. Keep going!")
        elif 25 <= bmi < 30:
            st.warning("You're overweight. Try cardio and a calorie deficit.")
        else:
            st.error("You're obese. Please follow a professional plan.")

if question:
    with st.spinner("Thinking..."):
        answer = ask_gpt(question)
        st.write("🤖", answer)
