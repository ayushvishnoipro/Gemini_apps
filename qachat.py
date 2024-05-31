from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure the Gemini model with your API key from the .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini Pro model and initialize a chat session
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Start a new chat with empty history

def get_gemeni_response(question):
  """
  Sends the user's question to the ongoing chat session and retrieves the response.

  Args:
      question: The user's question to be answered by the Gemini model.

  Returns:
      A generator object containing the chunked response text from the model.
  """
  response = chat.send_message(question, stream=True)
  return response

# Initialize the Streamlit app and set the page title
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Check if chat history exists in session state, otherwise initialize an empty list
if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []

# Input field for the user's question
input_text = st.text_input("Input: ", key="input")

# Button to submit the question
submit_button = st.button("Ask the question")

# Process user input when the button is clicked and input is provided
if submit_button and input_text:
  response = get_gemeni_response(input_text)

  # Add user query and model response to the chat history in session state
  st.session_state['chat_history'].append(("you", input_text))
  st.subheader("The response is:")
  for chunk in response:
    st.write(chunk.text)
    # Append each chunk of the response to the chat history
    st.session_state['chat_history'].append(("bot", chunk.text))

# Display the chat history
st.subheader("The chat history is:")
for role, text in st.session_state['chat_history']:
  st.write(f"{role}: {text}")
