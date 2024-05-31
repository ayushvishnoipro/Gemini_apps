from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemeni_response(question):
  """
  Gets a response from the Gemini model and handles potential errors.

  Args:
      question: The user's question to be answered by the model.

  Returns:
      The text content of the generated response, or an informative message if an error occurs.
  """
  try:
    response = model.generate_content(question)
    return response.text
  except Exception as e:
    # Handle any errors that might occur during generation
    return f"An error occurred: {e}"

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemeni LLM Application")
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# Process user input on button click
if submit_button:
  response = get_gemeni_response(input_text)
  st.subheader("The response is:")
  st.write(response)
