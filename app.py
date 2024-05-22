# Install the requirements before you run the script.
# pip install streamlit  joblib

import streamlit as st
from joblib import load

image_map = {
    "Adelie": "images/Adelie.png", 
    "Chinstrap": "images/Chinstrap.png",
    "Gentoo": "images/Gentoo.png"
}

st.cache_resource()
def load_model():
    model = load("models/lr_model.joblib")
    return model


model = load_model()

if not st.session_state.get("model_loaded", False):
    if model:
        st.success("Model loaded successfully.")
    st.session_state["model_loaded"] = True

st.title("Penguin Species Prediction")

bill_length_mm = st.number_input("Bill Length (mm)", min_value=0.0, format="%f")
bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0.0, format="%f")
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0, format="%f")
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0, format="%f")
year = st.number_input("Year", min_value=2000, max_value=3000, step=1)
        
if st.button("Predict"):
    prediction = model.predict([[bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, year]])
    predicted_species = prediction[0]

    if predicted_species in image_map:
        species_image = image_map[predicted_species]
        
        col1, col2, col3 = st.columns([1, 2, 2]) 
        with col2:
            st.markdown(f"<h3 style='text-align: center; color: green;'>Predicted Species: {predicted_species}</h3>", unsafe_allow_html=True)
            st.image(species_image, width=600, use_column_width='auto')

    else:
        st.error("Prediction does not correspond to a known species.")