import streamlit as st
import pandas as pd
import tensorflow as tf
import requests
from io import BytesIO

# Define the URL of the trained model on GitHub
model_url = 'https://github.com/<username>/<repository>/raw/main/v3_pred_cott_dis.h5'

# Load the trained model from the URL
try:
    response = requests.get(model_url)
    response.raise_for_status()
    model = tf.keras.models.load_model(BytesIO(response.content))
except requests.exceptions.RequestException as e:
    st.error(f'Error loading model from {model_url}: {e}')
    st.stop()

# Define the Streamlit app interface
def app():
    st.title('Cotton Plant Disease Prediction')
    st.write('Enter the following information about your cotton plant to predict the disease:')
    
    # Create input fields for user input data
    temperature = st.text_input('Temperature (°C)')
    humidity = st.text_input('Relative Humidity (%)')
    ph = st.text_input('pH')
    rainfall = st.text_input('Rainfall (mm)')
    
    # When the user clicks the "Predict" button
    if st.button('Predict'):
        # Process the user input data
        input_data = pd.DataFrame([[temperature, humidity, ph, rainfall]], columns=['temperature', 'humidity', 'ph', 'rainfall'])
        
        # Make a prediction using the loaded model
        try:
            prediction = model.predict(input_data)
        except Exception as e:
            st.error(f'Error predicting: {e}')
            st.stop()
        
        # Display the prediction to the user
        if prediction[0][0] == 1:
            st.write('Bacterial Blight')
        elif prediction[0][1] == 1:
            st.write('Yellow Vein Mosaic Virus')
        elif prediction[0][2] == 1:
            st.write('Leaf Curl Virus')
        else:
            st.write('No disease')

# Launch the app
if __name__ == '__main__':
    app()
