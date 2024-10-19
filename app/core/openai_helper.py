from openai import OpenAI
from core.constants import *

def get_response_from_chatgpt(client, messages, functions):
  if functions is None:
    return client.chat.completions.create(model=OPENAI.MODEL, messages=messages)
  else:
    return client.chat.completions.create(model=OPENAI.MODEL, messages=messages, functions=functions, function_call="auto")

def add_function_response(function_name, response_from_function):
  return {
    "role": "function",
    "name": function_name,
    "content": response_from_function
  }

def add_function_call(function_name, function_args):
  return {
    "role": "assistant",
    "function_call": {
        "name": function_name,
        "arguments": function_args,
    },
    "content": None
  }

def add_user_prompt(user_prompt):
  return {
    "role": "user", 
    "content": user_prompt
    }

def add_first_chat_message():
  return {
    "role": "assistant", 
    "content": "How can I help you?"
    }

def add_assistant_message(msg):
  return {
    "role": "assistant", 
    "content": msg
    }

def is_chatgpt_wants_to_call_function(response):
  return response.choices[0].message.content is None and response.choices[0].message.function_call.name