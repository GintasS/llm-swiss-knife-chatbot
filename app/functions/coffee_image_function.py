import requests

def get_random_coffee_image():
    """
    Fetches a random coffee image URL from the API at https://coffee.alexflipnote.dev/random.json.

    Returns:
        str: A URL to a random coffee image.
    """
    try:
        response = requests.get("https://coffee.alexflipnote.dev/random.json")
        response.raise_for_status()  # Raise an error for bad responses
        image_data = response.json()
        return image_data.get("file", "No image found.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
