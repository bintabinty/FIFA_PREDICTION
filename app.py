import streamlit as st # type: ignore

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    load_css('style.css')  # Load the CSS file
    
    if 'page' not in st.session_state:
        st.session_state.page = 'page1'
    
    if st.session_state.page == 'page1':
        page1()
    elif st.session_state.page == 'page2':
        page2()
    elif st.session_state.page == 'page3':
        page3()

def page1():
    st.title("FIFA Player Prediction")

    with st.form(key='player_form'):
        st.header("Enter Player Details")
        first_name = st.text_input("First Name:", value=st.session_state.get('first_name', ''))
        last_name = st.text_input("Last Name:", value=st.session_state.get('last_name', ''))
        
        position = st.selectbox("Select Player Position:", 
                                ["--Select Position--", "Goalkeeper", "Defender", "Midfielder", "Forward"], 
                                index=["--Select Position--", "Goalkeeper", "Defender", "Midfielder", "Forward"].index(st.session_state.get('position', '--Select Position--')))

        next_button = st.form_submit_button(label='Next')
    
    if next_button:
        if position == "--Select Position--":
            st.warning("Please select a valid position.")
        else:
            st.session_state.first_name = first_name
            st.session_state.last_name = last_name
            st.session_state.position = position
            st.session_state.page = 'page2'
            st.experimental_rerun()

def page2():
    st.title("FIFA Player Prediction")
    st.header(f"Enter Characteristics for {st.session_state.position}")

    with st.form(key='characteristics_form'):
        if st.session_state.position == 'Goalkeeper':
            league_rank = st.number_input("League Rank:", min_value=1, max_value=10, value=st.session_state.get('league_rank', 1))
            international_reputation = st.number_input("International Reputation:", min_value=1, max_value=5, value=st.session_state.get('international_reputation', 1))
            weak_foot = st.number_input("Weak Foot:", min_value=1, max_value=5, value=st.session_state.get('weak_foot', 1))
            body_type = st.text_input("Body Type:", value=st.session_state.get('body_type', '1'))
            movement_reactions = st.number_input("Movement Reactions:", min_value=0, max_value=100, value=st.session_state.get('movement_reactions', 60))
            power_shot_power = st.number_input("Power Shot Power:", min_value=0, max_value=100, value=st.session_state.get('power_shot_power', 60))
            GK_attribute = st.number_input("GK Attribute:", min_value=0, max_value=100, value=st.session_state.get('GK_attribute', 60))
        # Add additional forms for other positions as needed
        
        next_button = st.form_submit_button(label='Next')
    
    if next_button:
        st.session_state.league_rank = league_rank
        st.session_state.international_reputation = international_reputation
        st.session_state.weak_foot = weak_foot
        st.session_state.body_type = body_type
        st.session_state.movement_reactions = movement_reactions
        st.session_state.power_shot_power = power_shot_power
        st.session_state.GK_attribute = GK_attribute
        st.session_state.page = 'page3'
        st.experimental_rerun()

def page3():
    st.title("FIFA Player Prediction")
    st.header("Predicted Rating")

    # Placeholder for the prediction logic
    rating = predict_rating()
    
    st.write(f"The predicted rating of the player is {rating}")

def predict_rating():
    # Placeholder for the actual prediction logic
    # Here, just a mock prediction is returned
    return 85

if __name__ == "__main__":
    main()
