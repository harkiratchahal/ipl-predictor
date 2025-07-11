import streamlit as st
import pickle
import pandas as pd
import base64

# Set page configuration
st.set_page_config(
    page_title="🏆 IPL Win Predictor",
    layout="centered",
    page_icon="🏏"
)

# Load model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Team & city data
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bengaluru',
    'Kolkata Knight Riders', 'Punjab Kings', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals', 'Gujarat Titans'
]

cities = sorted([
    'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
    'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
    'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Rajkot', 'Kanpur', 'Bengaluru', 'Indore', 'Dubai', 'Sharjah',
    'Navi Mumbai', 'Guwahati', 'Mohali'
])

# Title & subtitle
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Predict your favorite team's chances in real-time!</p>", unsafe_allow_html=True)
st.markdown("---")

# Input fields
with st.container():
    st.subheader("🧮 Match Setup")
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox("🏏 Batting Team", sorted(teams))
    with col2:
        bowling_team = st.selectbox("🎯 Bowling Team", sorted([t for t in teams if t != batting_team]))

    selected_city = st.selectbox("📍 Match Location", cities)
    target = st.number_input("🎯 Target Score", min_value=1, step=1)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input("🏏 Current Score", min_value=0, step=1)
    with col4:
        overs = st.number_input("⏱ Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
    with col5:
        wickets_out = st.number_input("🚑 Wickets Lost", min_value=0, max_value=10, step=1)

# Predict Button
if st.button("🔮 Predict Win Probability"):
    if overs == 0 or overs > 20 or wickets_out > 10:
        st.error("⚠️ Please enter valid overs and wickets.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets = 10 - wickets_out
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left else 0

        # Prepare input for model
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        st.markdown("---")
        st.subheader("📋 Match Summary")
        st.success(f"**{batting_team}** vs **{bowling_team}** in *{selected_city}*")
        st.write(f"🎯 Target: `{target}`")
        st.write(f"🏏 Score: `{score}/{wickets_out}`")
        st.write(f"⏱ Overs: `{overs:.1f}`  |  🧮 Balls Left: `{balls_left}`")

        # Win/Loss display
        colA, colB = st.columns(2)
        with colA:
            st.metric(label=f"🔵 {batting_team} Win %", value=f"{round(win * 100)}%")
            st.progress(win)
        with colB:
            st.metric(label=f"🔴 {bowling_team} Win %", value=f"{round(loss * 100)}%")
            st.progress(loss)

        st.markdown("🏆 *Prediction powered by a machine learning model trained on historical IPL data*")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2025 IPL Predictor | Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)


