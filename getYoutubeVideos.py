from googleapiclient.discovery import build

# Replace the API_KEY and CHANNEL_ID with your own values
API_KEY = "your_api_key_here"
CHANNEL_ID = "your_channel_id_here"

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Retrieve the latest 10 videos from the channel
request = youtube.search().list(
        part='id,snippet',
        channelId=CHANNEL_ID,
        maxResults=10,
        order='date',
        type='video'
    )
response = request.execute()

# Print the video titles and URLs
for item in response['items']:
    print(item['snippet']['title'])
    print('https://www.youtube.com/watch?v=' + item['id']['videoId'])
