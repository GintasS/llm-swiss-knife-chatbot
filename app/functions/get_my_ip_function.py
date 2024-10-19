import requests

def get_my_ip():
  """
  Calls the API at https://api.myip.com to get the IP address and related information.
  
  Returns:
      dict: A dictionary containing the IP address, country, and country code.
  """
  try:
    response = requests.get("https://api.myip.com")
    response.raise_for_status()  # Raise an error for bad responses
    ip_info = response.json()
    ip = ip_info.get("ip", "Unknown IP")
    country = ip_info.get("country", "Unknown Country")
    return ip
  except requests.RequestException as e:
    print(f"An error occurred: {e}")
    return None
