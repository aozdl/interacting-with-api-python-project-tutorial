#%pip install spotipy
#%pip install python-dotenv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
client_credentials_manager=SpotifyClientCredentials(client_id, client_secret)
connection = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print(connection)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
result = sp.artist_top_tracks("6XyY86QOPPrYVGvF9ch6wz")
print(result.keys())

print(type(result["tracks"]))
tracks = result["tracks"][0:10]
#print(tracks)
sub_tracks = [(d["name"],d["popularity"],d["duration_ms"]) for d in tracks]
print(sub_tracks)
columns = ["Track", "Popularity", "Duration"]

df = pd.DataFrame(sub_tracks,columns=columns)
df_sorted = df.sort_values(by="Popularity")
print(df_sorted.head(3))

x_vals = df.Popularity
y_vals = df.Duration

plt.scatter(x_vals,y_vals)
plt.xlabel("Popularity")
plt.ylabel("Duration (ms)")
plt.show()
plt.savefig("Scatter.jpg",dpi = 300)
corr = df.corr()
print(corr)
print("Given the distribution of the scatter plot at the PMCC value (0.35), the conclusion is that there is very weak positive correlation between song duration and popularity")


