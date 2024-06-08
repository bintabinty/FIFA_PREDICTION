import streamlit as st
import pickle
import pandas as pd
import math

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Function to load the models and encoders
def load_pickle(file_name):
    with open(file_name, "rb") as file:
        return pickle.load(file)
    
# Load the models
model_GK = load_pickle("model_GK.pkl")
model_FW = load_pickle("model_FW.pkl")
model_DEF = load_pickle("model_DEF.pkl")
model_MID = load_pickle("model_MID.pkl")

# Load encoders
work_rate_mid = load_pickle("work_rate_mid.pkl")
preferred_foot_mid = load_pickle("preferred_foot_mid.pkl")
body_type_gk = load_pickle("body_type_gk.pkl")
work_rate_fw = load_pickle("work_rate_fw.pkl")
work_rate_def = load_pickle("work_rate_def.pkl")

# Helper function to predict rating
def predict(model, features):
    df = pd.DataFrame([features])
    return model.predict(df.values)[0]

st.title("Player Position Rating Prediction")

# Select player position
position = st.sidebar.selectbox("Select Player Position", ["Goalkeeper", "Forward", "Defender", "Midfielder"])

if position == "Goalkeeper":
    st.header("Goalkeeper Input")
    league_rank = st.number_input("League Rank", min_value=1, max_value=5, step=1)
    international_reputation = st.number_input("International Reputation", min_value=1, max_value=5, step=1)
    weak_foot = st.number_input("Weak Foot", min_value=1, max_value=5, step=1)
    body_type = st.selectbox("Body Type", body_type_gk.classes_)
    movement_reactions = st.number_input("Movement Reactions", min_value=1, max_value=100, step=1)
    power_shot_power = st.number_input("Power Shot Power", min_value=1, max_value=100, step=1)
    goalkeeping_diving = st.number_input("Goalkeeping Diving", min_value=1, max_value=100, step=1)
    goalkeeping_handling = st.number_input("Goalkeeping Handling", min_value=1, max_value=100, step=1)
    goalkeeping_kicking = st.number_input("Goalkeeping Kicking", min_value=1, max_value=100, step=1)
    goalkeeping_positioning = st.number_input("Goalkeeping Positioning", min_value=1, max_value=100, step=1)
    goalkeeping_reflexes = st.number_input("Goalkeeping Reflexes", min_value=1, max_value=100, step=1)
    
    if st.button("Predict Rating"):
        features = [
            league_rank, 
            international_reputation, 
            weak_foot, 
            body_type_gk.transform([body_type])[0], 
            movement_reactions, 
            power_shot_power, 
            goalkeeping_diving,
            goalkeeping_handling,
            goalkeeping_kicking,
            goalkeeping_positioning,
            goalkeeping_reflexes
        ]
        rating = predict(model_GK, features)
        truncated_rating = math.trunc(rating)
        st.write(f"Predicted Rating: {truncated_rating}")

elif position == 'Forward':
    st.header('Forward Input')
    league_rank = st.number_input("League Rank", min_value=1, max_value=5, step=1)
    international_reputation = st.number_input("International Reputation", min_value=1, max_value=5, step=1)
    weak_foot = st.number_input("Weak Foot", min_value=1, max_value=5, step=1)
    skill_moves = st.number_input("Skill Moves", min_value=1, max_value=5, step=1)
    work_rate = st.selectbox("Work Rate", work_rate_fw.classes_)
    attacking_volleys = st.number_input("Attacking Volleys", min_value=1, max_value=100, step=1)
    movement_reactions = st.number_input("Movement Reactions", min_value=1, max_value=100, step=1)
    power_long_shots = st.number_input("Power Long Shots", min_value=1, max_value=100, step=1)
    mentality_positioning = st.number_input("Mentality Positioning", min_value=1, max_value=100, step=1)
    mentality_composure = st.number_input("Mentality Composure", min_value=1, max_value=100, step=1)
    passing = st.number_input("Passing", min_value=1, max_value=100, step=1)
    dribbling = st.number_input("Dribbling", min_value=1, max_value=100, step=1)
    cam = st.number_input("CAM (Central Attacking Midfielder)", min_value=1, max_value=100, step=1)
    st_ = st.number_input("ST (Striker)", min_value=1, max_value=100, step=1)
    lw = st.number_input("LW (Left Winger)", min_value=1, max_value=100, step=1)
    cf = st.number_input("CF (Center Forward)", min_value=1, max_value=100, step=1)

    if st.button("Predict Rating"):
        features = [
            league_rank, 
            international_reputation,
            weak_foot,
            skill_moves,
            work_rate_fw.transform([work_rate])[0],
            attacking_volleys,
            movement_reactions,
            power_long_shots,
            mentality_positioning,
            mentality_composure,
            passing,
            dribbling,
            cam,
            st_,
            lw,
            cf
        ]
        rating = predict(model_FW, features)
        truncated_rating = math.trunc(rating)
        st.write(f"Predicted Rating: {truncated_rating}")

elif position == "Defender":
    st.header("Defender Input")
    league_rank = st.number_input("League Rank", min_value=1, max_value=5, step=1)
    international_reputation = st.number_input("International Reputation", min_value=1, max_value=5, step=1)
    weak_foot = st.number_input("Weak Foot", min_value=1, max_value=5, step=1)
    work_rate = st.selectbox("Work Rate", work_rate_def.classes_)
    attacking_short_passing = st.number_input("Attacking Short Passing", min_value=1, max_value=100, step=1)
    skill_ball_control = st.number_input("Skill Ball Control", min_value=1, max_value=100, step=1)
    movement_reactions = st.number_input("Movement Reactions", min_value=1, max_value=100, step=1)
    mentality_composure = st.number_input("Mentality Composure", min_value=1, max_value=100, step=1)
    defending_sliding_tackle = st.number_input("Defending Sliding Tackle", min_value=1, max_value=100, step=1)
    passing = st.number_input("Passing", min_value=1, max_value=100, step=1)
    defending = st.number_input("Defending", min_value=1, max_value=100, step=1)
    cb = st.number_input("CB (Center Back)", min_value=1, max_value=100, step=1)
    lb = st.number_input("LB (Left Back)", min_value=1, max_value=100, step=1)
    lwb = st.number_input("LWB (Left Wing Back)", min_value=1, max_value=100, step=1)
    
    if st.button("Predict Rating"):
        features = [
            league_rank, 
            international_reputation,
            weak_foot,
            work_rate_def.transform([work_rate])[0],
            attacking_short_passing,
            skill_ball_control,
            movement_reactions,
            mentality_composure,
            defending_sliding_tackle,
            passing,
            defending,
            cb,
            lb,
            lwb
        ]
        rating = predict(model_DEF, features)
        truncated_rating = math.trunc(rating)
        st.write(f"Predicted Rating: {truncated_rating}")

elif position == "Midfielder":
    st.header("Midfielder Input")
    league_rank = st.number_input("League Rank", min_value=1, max_value=5, step=1)
    international_reputation = st.number_input("International Reputation", min_value=1, max_value=5, step=1)
    weak_foot = st.number_input("Weak Foot", min_value=1, max_value=5, step=1)
    skill_moves = st.number_input("Skill Moves", min_value=1, max_value=5, step=1)
    work_rate = st.selectbox("Work Rate", work_rate_mid.classes_)
    preferred_foot = st.selectbox("Preferred Foot", preferred_foot_mid.classes_)
    skill_long_passing = st.number_input("Skill Long Passing", min_value=1, max_value=100, step=1)
    movement_reactions = st.number_input("Movement Reactions", min_value=1, max_value=100, step=1)
    power_long_shots = st.number_input("Power Long Shots", min_value=1, max_value=100, step=1)
    mentality_composure = st.number_input("Mentality Composure", min_value=1, max_value=100, step=1)
    shooting = st.number_input("Shooting", min_value=1, max_value=100, step=1)
    lam = st.number_input("LAM (Left Attacking Midfielder)", min_value=1, max_value=100, step=1)
    lcm = st.number_input("LCM (Left Central Midfielder)", min_value=1, max_value=100, step=1)   
    lm = st.number_input("LM (Left Midfielder)", min_value=1, max_value=100, step=1)   

    if st.button("Predict Rating"):
        features = [
            league_rank, 
            international_reputation,
            weak_foot,
            skill_moves,
            work_rate_mid.transform([work_rate])[0],
            preferred_foot_mid.transform([preferred_foot])[0],
            skill_long_passing,
            movement_reactions,
            power_long_shots,
            mentality_composure,
            shooting,
            lam,
            lcm,
            lm
        ]
        rating = predict(model_MID, features)
        truncated_rating = math.trunc(rating)
        st.write(f"Predicted Rating: {truncated_rating}")
