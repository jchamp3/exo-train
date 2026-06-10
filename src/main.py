import pandas as pd
import urllib3
import requests
from pathlib import Path
import os

url = "https://exo.quebec/xdata/trains/google_transit.zip"

target_directory =  Path("/home/jchamp/projects/exo-train/data")

response = requests.get(url)

# ['agency.txt', 'calendar.txt', 'calendar_dates.txt', 'feed_info.txt', 'routes.txt', 'shapes.txt', 'stop_times.txt', 'stops.txt', 'trips.txt']

with open(target_directory / "google_transit.zip", "wb") as f:
    f.write(response.content)

