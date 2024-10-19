import pandas as pd
import numpy as np

def get_map(latitude, longitude):
  """
  Generates a DataFrame containing random geographical coordinates centered around the specified latitude and longitude.

  Args:
      latitude (float): The central latitude for the generated coordinates.
      longitude (float): The central longitude for the generated coordinates.

  Returns:
      pd.DataFrame: A DataFrame with 1000 rows and 2 columns ('lat', 'lon'), where each row represents a random geographical point.
  """
  
  return pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [latitude, longitude],
    columns=["lat", "lon"],
  )