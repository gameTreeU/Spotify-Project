import spotipy
import spotipy.util as util
import random
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import csv

#OAuth ID, SECRET, USERNAME
CLIENT_ID=""
CLIENT_SECRET=""
USERNAME = ""


token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
print(token)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

data = spotify.user_playlist_tracks(USERNAME, "1gDyaVxq6iAxlJxzIoRtpF?si=_tgUjrW-Qteod4tbjSdbcA")


#get playlist tracks and track data
def getPlaylistSentiment():
    jsonDict = {}
    
    headers = {'Authorization': "Bearer " + cache_token}
    for track in data['tracks']['items']:
        songId = track['track']['id']
        url = "https://api.spotify.com/v1/audio-features/" + songId
        response = requests.get(url, headers=headers)
        jsonDict[track['track']['name']] = json.loads(response.text)
    return jsonDict

out = getPlaylistSentiment()
print(out)

#write to JSON file
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName +'.json'
    with open (filePathNameWExt, 'w') as fp:
        json.dump(data, fp, indent = 4)

path = './'
fileName = 'playlistData'
data = out
writeToJSONFile(path, fileName, data)

#write JSON file to CSV
with open('playlistData.json') as json_file:
    readJSON = json.load(json_file)

playlistDataForCSV = readJSON['playlistData.json']['track']['id']
print(playlistDataForCSV)

csv_file = open('csv_file.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_file.close()



#plotRange = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
#plt.scatter(plotRange, playlistData.json["danceability"], color='r')




# url = "https://api.spotify.com/v1/audio-features/19YKaevk2bce4odJkP5L22"

# headers = {'Authorization': "Bearer " + cache_token}
# response = requests.get(url, headers=headers)
# jsonDict = json.loads(response.text)

#write to text file
#with open('SongData.txt', 'w') as f:
#    json.dump(out, f)

# def getTrackInfo(trackID):
#     return spotify.track(trackID)
# # print spotify

# tempTrack = getTrackInfo("https://open.spotify.com/track/0fujQqs6ybS47td4sEwPcA") #nikes by Frank Ocean
# print(tempTrack)