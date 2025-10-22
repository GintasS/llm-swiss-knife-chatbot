from openai import OpenAI
import streamlit as st
from functions.functions import openai_functions
from functions.functions import call_function
from core.openai_helper import *
from core.constants import *
import pandas as pd

# Read credentials
with st.sidebar:
    OPENAI.API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    EMAIL_FUNCTION.EMAIL_ADDRESS = st.text_input("Email Address (Gmail)", key="email_address", type="password")
    EMAIL_FUNCTION.EMAIL_PASSWORD = st.text_input("Email App Password (Gmail)", key="email_address_password", type="password")

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi there! I'm your AI assistant. I'm programmed to help you with your questions and tasks. You can ask me questions and give me commands like: whats my ip address, get a random Chuck Norris fact, send an email address, convert time or draw a random map."},
        {"role": "assistant", "content": "Before writing your first message, please add your OpenAI API key on the left sidebar to continue."},
        {"role": "assistant", "content": "You can also add your email address and password to send an email."},
        {"role": "assistant", "content": "The procedure for sending email differs from client to client. For example, in Gmail, you need to create an app password."},
    ]

for msg in st.session_state.messages:  
    # Do not print function call data into chat.  
    if msg["role"] == "function" or "function_call" in msg:
        continue
    
    # Write a map to the chat when we got a map in the messages.
    if msg["role"] == "assistant" and "map_data" in msg:
        chat_message = st.chat_message(msg["role"])
        chat_message.map(pd.DataFrame(msg["map_data"]))
        continue
    
    chat_message = st.chat_message(msg["role"])
    chat_message.write(msg["content"])

# Handle user input.
if prompt := st.chat_input():
    # Prevent handling user input if OpenAI key is not set.
    if not OPENAI.API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Initialize constants for the input handling.
    client = OpenAI(api_key=OPENAI.API_KEY)
    is_map = False
    map_data = None

    # Write user input to chat.
    st.session_state.messages.append(add_user_prompt(prompt))
    st.chat_message("user").write(prompt)


    # Handle user input.
    response = get_response_from_chatgpt(client, st.session_state.messages, openai_functions)
    if is_chatgpt_wants_to_call_function(response):
      function_name = response.choices[0].message.function_call.name
      function_obj = response.choices[0].message.function_call

      response_from_function = call_function(function_obj)
      if response_from_function is None:
          msg = f"There was an error while calling {function_name}."
      elif function_name == "get_map":
          st.session_state.messages.append(add_function_call(function_name, function_obj.arguments))

          summarize_function_call = get_response_from_chatgpt(client, st.session_state.messages, None)
          msg = summarize_function_call.choices[0].message.content
          is_map=True
          map_data=response_from_function  
      else:
          # Adding assistant response to messages.
          st.session_state.messages.append(add_function_call(function_name, function_obj.arguments))

          # Adding function response to messages.
          st.session_state.messages.append(add_function_response(function_name, response_from_function))
          summarize_function_call = get_response_from_chatgpt(client, st.session_state.messages, None)
          msg = summarize_function_call.choices[0].message.content
    else:
        msg = response.choices[0].message.content

    # Add assistant response.
    st.session_state.messages.append(add_assistant_message(msg))
    chat_message_obj = st.chat_message("assistant")
    chat_message_obj.write(msg)

    # We are serializing map data to a dict, so we can hold it inside "messages"
    # Content is needed for OpenAI API, if it does not have it, it will fail.
    if is_map is True:
      chat_message_obj.map(map_data)
      st.session_state.messages.append({
          "role": "assistant",
          "content": "",
          "map_data": map_data.to_dict('records')  
      })
