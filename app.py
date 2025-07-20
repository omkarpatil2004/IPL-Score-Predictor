import streamlit as st
import pandas as pd
import pickle

# Load the model
pipe = pickle.load(open('score_predictor.pkl', 'rb'))

# Define teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals', 'Gujarat Titans', 'Lucknow Super Giants']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Pune', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Raipur', 'Ranchi', 'Ahmedabad', 'Lucknow', 'Bhubaneswar']

# App title
st.title('🏏 IPL Final Score Predictor')

# Input: Teams and City
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_city = st.selectbox('Select City', sorted(cities))

# Match Progress Inputs
st.subheader("📊 Match Situation")

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input("Current Runs", min_value=0)
with col4:
    balls_bowled = st.number_input("Balls Bowled (in 1st innings)", min_value=1, max_value=120)
with col5:
    wickets_lost = st.number_input("Wickets Lost", min_value=0, max_value=10)

# Last 5 Overs Inputs
st.subheader("🔥 Last 5 Overs Performance")

col6, col7 = st.columns(2)
with col6:
    last_5_runs = st.number_input("Runs Scored (Last 5 Overs)", min_value=0)
with col7:
    last_5_wickets = st.number_input("Wickets Lost (Last 5 Overs)", min_value=0, max_value=5)

# Predict Button
if st.button('🎯 Predict Final Score'):
    # Derived features
    balls_left = 120 - balls_bowled

    # Avoid division by zero
    crr = (current_score / balls_bowled) * 6 if balls_bowled > 0 else 0

    # Create input DataFrame
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_till_now': [current_score],
        'balls_bowled': [balls_bowled],
        'balls_left': [balls_left],
        'wickets_till_now': [wickets_lost],
        'crr': [crr],
        'last_5_runs': [last_5_runs],
        'last_5_wkts': [last_5_wickets]
    })

    # Prediction
    predicted_score = int(pipe.predict(input_df)[0])
    st.success(f"🏁 Predicted Final Score: {predicted_score}")
