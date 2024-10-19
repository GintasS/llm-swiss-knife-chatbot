import requests

def get_random_chuck_norris_joke():
  """
  Fetches a random Chuck Norris joke from the API at https://api.chucknorris.io/jokes/random.

  Returns:
      str: A random Chuck Norris joke.
  """
  try:
      response = requests.get("https://api.chucknorris.io/jokes/random")
      response.raise_for_status()  # Raise an error for bad responses
      joke_data = response.json()
      return joke_data.get("value", "No joke found.")
  except requests.RequestException as e:
      print(f"An error occurred: {e}")
      return None
