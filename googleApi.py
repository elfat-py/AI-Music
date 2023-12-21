# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# # from authDownload import *
# from pytube import YouTube
# import os
#
# #url = 'https://www.youtube.com/watch?v=jWfoyg6z3Dw&list=RDMMf8WdxqcH1QQ&index=2'
# # music_output = YouTube(url)
#
# # Get the audio stream with the desired format (e.g., mp4)
# print("done")
# #loadVideos = YouTubeMusicDownload()
#
# class YouTubeAPI:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.youtube = build('youtube',
#                              'v3',
#                              developerKey=self.api_key
#         )
#
#     def search_videos(self, query, video_duration='any'):
#         try:
#             search_response = self.youtube.search().list(
#                 q=query,
#                 part='snippet',
#                 maxResults=3,
#                 type='video',
#                 videoDuration=video_duration
#             ).execute()
#             videos = []
#
#             for search_result in search_response.get('items', []):
#                 if search_result['id']['kind'] == 'youtube#video':
#                     videos.append({
#                         'title': search_result['snippet']['title'],
#                         'video_id': search_result['id']['videoId']
#
#                     })
#
#             return videos
#
#         except HttpError as e:
#             print(f'An HTTP error {e.resp.status} occurred: {e.content}')
#
#     def search_for_video(self, query, video_duration='any'):
#         results = self.search_videos(query)
#
#         if results:
#             print("Recommended Videos: ")
#             for video in results:
#                 print(f"Title: {video['title']}")
#                 print(f"Video ID: {video['video_id']}") #We need the video ID here
#                 #loadVideos.download_audio(f"https://www.youtube.com/watch?v={video['video_id']}")
#                 music_output = YouTube(f"https://www.youtube.com/watch?v={video['video_id']}")
#                 out_path = music_output.streams.filter(only_audio=True).get_by_itag(251).download()
#                 new_name = os.path.splitext(out_path)
#                 os.rename(out_path, new_name[0] + '.mp3')
#                 print("The music has been downloaded")
#         else:
#             print(f"There were no songs for the provided input: {query}")
#
#     # def get_video_ids(self, query, video_duration='any'):
#     #     results = self.search_videos(query)
#     #     video_ids = []
#     #
#     #     if results:
#     #         for video in results:
#     #             video_ids.append(video['video_id'])
#     #
#     #     return video_ids


# Pretty much we are done with this file we just need better results and also we should make it happer
# For a list of provided results to provide a list of outputs from the YouTube

"""""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydub import AudioSegment
from pydub.playback import play
import requests
import io

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def search_videos(self, query, video_duration='any'):
        try:
            search_response = self.youtube.search().list(
                q=query,
                part='snippet',
                maxResults=3,
                type='video',
                videoDuration=video_duration
            ).execute()
            videos = []

            for search_result in search_response.get('items', []):
                if search_result['id']['kind'] == 'youtube#video':
                    videos.append({
                        'title': search_result['snippet']['title'],
                        'video_id': search_result['id']['videoId']
                    })

            return videos

        except HttpError as e:
            print(f'An HTTP error {e.resp.status} occurred: {e.content}')

    def search_for_video(self, query, video_duration='any'):
        results = self.search_videos(query)

        if results:
            print("Recommended Videos: ")
            for video in results:
                print(f"Title: {video['title']}")
                print(f"Video ID: {video['video_id']}")
                print()

            # Choose a video from the results
            video_id = input("Enter the Video ID of the song you want to play: ")

            # Play the audio of the chosen video
            self.play_audio(video_id)
        else:
            print(f"There were no songs for the provided input: {query}")

    def play_audio(self, video_id):
        try:
            # Retrieve video details
            video_response = self.youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()

            # Extract audio URL
            audio_url = video_response['items'][0]['contentDetails']['audio']['url']

            # Download audio from the URL
            response = requests.get(audio_url)
            audio_data = response.content

            # Load audio data into PyDub AudioSegment
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))

            # Play the audio
            play(audio_segment)

        except HttpError as e:
            print(f'An HTTP error {e.resp.status} occurred: {e.content}')

# YouTube API key
#API_KEY = 'YOUR_API_KEY'

# Create a YouTubeAPI instance
youtube_api = YouTubeAPI(API_KEY)

# Search for videos
query = input("Enter a song name to search: ")
youtube_api.search_for_video(query)
"""""
import os
from googleapiclient.discovery import build


class YouTubeAPI:

    def __init__(self):
        self.api_key = os.environ.get("YOUTUBE_API_KEY")
        self.youtube = build("youtube", "v3", developerKey=self.api_key)
        self.video_id = None


    def find_music_id(self, query, max_results=1):
        # Search for music related to the provided name
        search_response = self.youtube.search().list(
            q=query,
            part="id,snippet",
            type="video",
            maxResults=max_results
        ).execute()

        music_link = ""

        # Extract video details from the search response
        for search_result in search_response.get("items", []):
            self.video_id = search_result["id"]["videoId"]
            music_link = f"https://www.youtube.com/watch?v={self.video_id}"

        return music_link

    def find_similar_music(self, max_results=3):
        search_response = self.youtube.search().list(
            relatedToVideoId=self.video_id,
            type=["audio", "video"],
            q=self.video_id,
            part=["id", "snippet"],
            maxResults=max_results
        ).execute()

        music_links = []

        for search_result in search_response.get("items", []):
            self.video_id = search_result["id"]["videoId"]
            video_title = search_result["snippet"]["title"]
            music_links.append((video_title, self.video_id))

        return music_links

