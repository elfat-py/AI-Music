from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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
        else:
            print(f"There were no songs for the provided input: {query}")




#Pretty much we are done with this file we just need better results and also we should make it happer
#For a list of provided results to provide a list of outputs from the YouTube

