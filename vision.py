from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini model and get responses
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemeni_response(input,image):
    if(input!= ""):
        response= model.generate_content([input,image])
    else:
        response= model.generate_content(image)
    return response.text

# initializing our streamlit app
st.set_page_config(page_title="Gemeni Image Demo")

st.header("gemeni application")
input = st.text_input("Input Prompt" , key="input")

uploaded_file = st.file_uploader("choose an image ", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Upload Image ",use_column_width=True)

submit = st.button("tell me about image")


# if submit is clicked
if submit:
    response = get_gemeni_response(input,image)
    st.subheader("The response is:")
    st.write(response)