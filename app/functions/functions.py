from functions.send_email_function import send_email
from functions.time_converter_function import convert_time
from functions.get_my_ip_function import get_my_ip
from functions.chuck_norris_function import get_random_chuck_norris_joke
from functions.coffee_image_function import get_random_coffee_image
from functions.get_map_function import get_map
import json

openai_functions = [
  {
    "name":"convert_time",
    "description":"Convert from one timezone to another timezone.",
    "parameters":{
        "type":"object",
        "properties":{
          "time_str":{
              "type":"string",
              "description":"The time to convert from in a format 'YYYY-MM-DD HH:MM:SS'"
          },
          "from_timezone":{
              "type":"string",
              "description":"The name of the current time zone (e.g., 'UTC')"
          },
          "to_timezone":{
              "type":"string",
              "description":"The name of the target time zone (e.g., 'US/Eastern')"
          }
        },
        "required":[
          "role"
        ]
    }
  },
  {
    "name":"send_email",
    "description":"Send an email using Gmail SMTP.",
    "parameters":{
        "type":"object",
        "properties":{
          "subject":{
              "type":"string",
              "description":"The email subject"
          },
          "body":{
              "type":"string",
              "description":"The email body"
          },
          "to_email":{
              "type":"string",
              "description":"The recipient's email address"
          }
        },
        "required":[
          "role"
        ]
    }
  },
  {
    "name": "get_my_ip",
    "description": "Retrieve the public IP address and related information."
  },
  {
    "name": "get_random_chuck_norris_joke",
    "description": "Get a random Chuck Norris fact"
  },
  {
    "name": "get_random_coffee_image",
    "description": "Get a random Coffee image"
  },
  {
    "name": "get_map",
    "description": "Get a map",
        "parameters":{
        "type":"object",
        "properties":{
          "latitude":{
              "type":"number",
              "description":"The latitude of the map"
          },
          "longitude":{
              "type":"number",
              "description":"The longitude of the map"
          }
        },
        "required":[
          "role"
        ]
    }
  } 
]

available_functions = {
  "send_email": send_email,
  "convert_time": convert_time,
  "get_my_ip": get_my_ip,
  "get_random_chuck_norris_joke": get_random_chuck_norris_joke,
  "get_random_coffee_image": get_random_coffee_image,
  "get_map": get_map
}

def call_function(function_call):
  function_to_call = available_functions[function_call.name] 
  function_args = json.loads(function_call.arguments)
  function_response = function_to_call(**function_args)
  return function_response