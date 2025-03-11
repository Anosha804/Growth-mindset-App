import streamlit as st
import random
import datetime
import pandas as pd

# Set dark theme for uniqueness
st.markdown(
    """
    <style>
    body { background-color: #1e1e1e; color: white; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; }
    .stTextInput>div>div>input { background-color: #333; color: white; border-radius: 5px; }
    .stSelectbox>div>div>select { background-color: #333; color: white; }
    .stProgress>div>div>div { background-color: #4CAF50; }
    .affirm-box { padding: 10px; border-radius: 8px; margin-top: 10px; }
    .home-icon { font-size: 40px; margin-right: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------- Sidebar Navigation ----------------------
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Mindset Quiz", "Daily Affirmation", "Vision Board"])

# ---------------------- Home Page ----------------------
if page == "Home":
    st.markdown("<h1 style='display: flex; align-items: center;'><span class='home-icon'>🏡</span> Growth Mindset Hub</h1>", unsafe_allow_html=True)
    st.write("Welcome to your personal mindset transformation journey!")
    
    # Adjusting image size
    st.image("image.jpg", use_container_width=False, width=250)
    
    # Motivational Quotes
    quotes = [
        "Believe you can, and you're halfway there.",
        "Challenges make you stronger, embrace them!",
        "Progress over perfection, keep going!",
        "Your growth is limitless, never stop learning!"
    ]
    st.success(random.choice(quotes))

# ---------------------- Mindset Quiz ----------------------
elif page == "Mindset Quiz":
    st.title("🧠 Growth Mindset Quiz")
    st.write("Take this short quiz to see how strong your mindset is!")

    questions = {
        "How do you react to failure?": ["I learn from it", "I get discouraged", "I give up"],
        "Do you believe intelligence is fixed?": ["No, I can improve", "Somewhat", "Yes, it's fixed"],
        "How do you handle challenges?": ["I embrace them", "I avoid them", "I get frustrated"]
    }

    score = 0
    total_questions = len(questions)
    answered = 0

    for q, options in questions.items():
        answer = st.radio(q, options, key=q)
        if answer == options[0]:  # Best growth mindset answer
            score += 1
        if answer:
            answered += 1

    st.progress(answered / total_questions)

    if st.button("Submit Quiz"):
        if score == 3:
            st.success("🌟 You have a strong growth mindset! Keep it up!")
        elif score == 2:
            st.warning("💡 You're on the right track! Keep developing your mindset!")
        else:
            st.error("🌱 Work on building a stronger growth mindset! You can do it!")

# ---------------------- Daily Affirmation Generator ----------------------
elif page == "Daily Affirmation":
    st.title("💬 Daily Affirmation Generator")
    moods = ["Motivated", "Confident", "Peaceful", "Grateful"]
    mood = st.selectbox("How are you feeling today?", moods)

    affirmations = {
        "Motivated": "I am capable of achieving great things!",
        "Confident": "I believe in myself and my abilities!",
        "Peaceful": "I am calm and in control of my emotions.",
        "Grateful": "I appreciate everything life offers me."
    }

    colors = {
        "Motivated": "#FF5733",
        "Confident": "#3498DB",
        "Peaceful": "#2ECC71",
        "Grateful": "#F1C40F"
    }

    if st.button("Get Affirmation"):
        st.markdown(
            f'<div class="affirm-box" style="background-color:{colors[mood]};"> 🌟 {affirmations[mood]}</div>',
            unsafe_allow_html=True
        )

# ---------------------- Vision Board ----------------------
elif page == "Vision Board":
    st.title("🖼️ Create Your Vision Board")
    st.write("Upload inspiring images, quotes, or goals!")

    uploaded_files = st.file_uploader("Upload your motivational images", accept_multiple_files=True)
    if uploaded_files:
        cols = st.columns(3)
        for index, file in enumerate(uploaded_files):
            with cols[index % 3]:
                st.image(file, caption=f"Image {index+1}", use_column_width=True)

st.sidebar.markdown("---")  
st.sidebar.write("Made with ❤️ using Streamlit")
