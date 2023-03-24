import streamlit as st
import pandas as pd
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model(r"C:\Users\ASUS\OneDrive\Desktop\v3_pred_cott_dis.h5")

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
        prediction = model.predict(input_data)
        
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