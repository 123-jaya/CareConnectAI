import streamlit as st
import random

st.set_page_config(page_title="CareConnectAI Dashboard", layout="centered")

st.title("🧠 CareConnectAI – Interactive Dashboard")
st.markdown("Click on each agent to learn more about their role and view a simulated mobile alert below.")

agents = {
    "👨‍⚕️ Health Monitor Agent": "Monitors vital signs like heart rate, blood pressure, and logs health trends to shared memory.",
    "🛡️ Fall Detection Agent": "Detects prolonged inactivity or sudden movements indicating potential falls.",
    "⏰ Reminder Agent": "Sends reminders for medicine, hydration, stretching, and appointments.",
    "🚨 Emergency Alert Agent": "Sends alerts to caregivers when vitals cross risk thresholds or falls are detected.",
    "💬 Conversation Agent": "Engages the user in supportive conversation to reduce isolation.",
    "🧠 Advice Agent": "Analyzes emotional score trends and suggests caregiver interventions."
}

with st.expander("👨‍⚕️ Health Monitor Agent"):
    st.write(agents["👨‍⚕️ Health Monitor Agent"])
with st.expander("🛡️ Fall Detection Agent"):
    st.write(agents["🛡️ Fall Detection Agent"])
with st.expander("⏰ Reminder Agent"):
    st.write(agents["⏰ Reminder Agent"])
with st.expander("🚨 Emergency Alert Agent"):
    st.write(agents["🚨 Emergency Alert Agent"])
with st.expander("💬 Conversation Agent"):
    st.write(agents["💬 Conversation Agent"])
with st.expander("🧠 Advice Agent"):
    st.write(agents["🧠 Advice Agent"])

# Mobile Notification Simulation
st.markdown("---")
st.subheader("📲 Mobile Notification")

messages = [
    "Ravi, it's time for your hypertension meds. 💊",
    "Don't forget to drink water and stay hydrated 💧",
    "No movement detected for 10 minutes. Please check in.",
    "Heart rate is stable. Keep it up! ❤️",
    "Time to stretch for 2 minutes 🧘‍♂️",
    "A caregiver will check in with you today. 😊"
]

if "last_msg" not in st.session_state:
    st.session_state.last_msg = random.choice(messages)

if st.button("🔄 Generate Notification"):
    new_msg = random.choice(messages)
    while new_msg == st.session_state.last_msg:
        new_msg = random.choice(messages)
    st.session_state.last_msg = new_msg

st.info(st.session_state.last_msg)

st.markdown("---")
st.caption("© 2025 CareConnectAI | Gen AI Hackathon")
