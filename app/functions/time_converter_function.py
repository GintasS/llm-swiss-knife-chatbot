from datetime import datetime
import pytz

def convert_time(time_str, from_timezone, to_timezone):
  """
  Convert time from one timezone to another.

  :param time_str: str, time in the format 'YYYY-MM-DD HH:MM:SS'
  :param from_timezone: str, the timezone to convert from (e.g., 'UTC')
  :param to_timezone: str, the timezone to convert to (e.g., 'US/Eastern')
  :return: str, the converted time in the format 'YYYY-MM-DD HH:MM:SS'

  Time zone examples:
  # 1. 'UTC' - Coordinated Universal Time
  # 2. 'US/Eastern' - Eastern Time (US & Canada)
  # 3. 'Europe/London' - London Time
  # 4. 'Asia/Tokyo' - Tokyo Time
  # 5. 'Australia/Sydney' - Sydney Time
  # 6. 'America/New_York' - New York Time
  # 7. 'Europe/Paris' - Paris Time
  # 8. 'Asia/Kolkata' - Kolkata Time
  # 9. 'Africa/Johannesburg' - Johannesburg Time
  # 10. 'America/Los_Angeles' - Los Angeles Time
  # 11. 'Europe/Vilnius' - Vilnius Time (Lithuania)

  """

  try:
    # Create timezone objects
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)

    # Parse the input time string
    naive_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

    # Localize the naive datetime to the from_timezone
    from_time = from_tz.localize(naive_time)

    # Convert to the target timezone
    to_time = from_time.astimezone(to_tz)

    # Return the converted time as a string
    return to_time.strftime('%Y-%m-%d %H:%M:%S %p')
  except Exception as e:
    print(f"Failed to convert time. Error: {e}")
    return None