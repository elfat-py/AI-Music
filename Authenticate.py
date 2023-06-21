from pytube import YouTube
from pytube.exceptions import AgeRestrictedError
from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request

class YouTubeMusicPlayer:
    def __init__(self):
        self.credentials = None # We let it to none at the beggining because there might be no need for authentication that will shorten the time needed for downloading the vid

    def authenticate(self):
        credentials_file = 'credentials.json' #This will make it possible for our test cases we are going to need a configuration for each user
        scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']# I think this will open the window for authentication

        flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
        self.credentials = flow.run_local_server(port=0)

    def download_audio(self, video_url):
        try:
            if not self.credentials or not self.credentials.valid:
                self.authenticate()

            yt = YouTube(video_url)
            print(yt.title)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download()
        except AgeRestrictedError:
            print("This video is age-restricted.")

vid1 = YouTubeMusicPlayer()
vid1.download_audio("https://www.youtube.com/watch?v=pVjdMQ_iAh0&list=RDMM&index=21&ab_channel=GANGSTERGANG")#This should be the link to the song
