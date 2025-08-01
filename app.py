import streamlit as st
import pandas as pd
import pickle
import requests
import zipfile
import os

# ------------------------------
# 1. Get Google Drive File ID
# ------------------------------
def get_file_id_from_txt():
    with open("Pickle/Refer.txt", "r") as f:
        url = f.read().strip()
        if "id=" in url:
            return url.split("id=")[1]
        elif "/d/" in url:
            return url.split("/d/")[1].split("/")[0]
        else:
            st.error("Invalid Google Drive link format.")
            st.stop()

# ------------------------------
# 2. Download and Extract Model
# ------------------------------
def download_and_extract_zip(file_id, zip_path="model.zip", extract_to="."):
    if os.path.exists("score_predictor.pkl"):
        return  # Skip if already exists

    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)

    # Handle warning tokens
    token = None
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            token = value
    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    # Download ZIP
    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

    # Extract ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# ------------------------------
# 3. Load Model
# ------------------------------
file_id = get_file_id_from_txt()
download_and_extract_zip(file_id)

with open('score_predictor.pkl', 'rb') as f:
    pipe = pickle.load(f)

# ------------------------------
# 4. Streamlit UI
# ------------------------------
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals', 'Gujarat Titans', 'Lucknow Super Giants']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Pune', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Raipur', 'Ranchi', 'Ahmedabad', 'Lucknow', 'Bhubaneswar']

st.title('🏏 IPL Final Score Predictor')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_city = st.selectbox('Select City', sorted(cities))

# Match inputs
st.subheader("📊 Match Situation")
col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input("Current Runs", min_value=0)
with col4:
    balls_bowled = st.number_input("Balls Bowled (in 1st innings)", min_value=1, max_value=120)
with col5:
    wickets_lost = st.number_input("Wickets Lost", min_value=0, max_value=10)

# Last 5 overs
st.subheader("🔥 Last 5 Overs Performance")
col6, col7 = st.columns(2)
with col6:
    last_5_runs = st.number_input("Runs Scored (Last 5 Overs)", min_value=0)
with col7:
    last_5_wickets = st.number_input("Wickets Lost (Last 5 Overs)", min_value=0, max_value=5)

# Predict
if st.button('🎯 Predict Final Score'):
    balls_left = 120 - balls_bowled
    crr = (current_score / balls_bowled) * 6 if balls_bowled > 0 else 0

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

    predicted_score = int(pipe.predict(input_df)[0])
    st.success(f"🏁 Predicted Final Score: {predicted_score}")
