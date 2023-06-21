from openAiAPI import *
from saveData import save_current_mood,  save_current_input, load_previous_input
from googleAPI import YouTubeAPI
from authDownload import *
from googleapiclient.discovery import build
import requests
import io
from pydub import AudioSegment
from pydub.playback import play

# Main interaction loop
def main():
    api_key_you_tube = 'AIzaSyAmuxK_HoCBpxflYdGd0CDY5DSoNlDjgjw'

    premium = False

    def premium_client(): #We should combine the previous input with the client_mood of the client as well
        if premium:
            previous_input = load_previous_input()  # We should create such response only if premium also if premium is true we should make the response faster and more efficient
            user_input = input("User input: ")

            if previous_input:
                user_input = previous_input + '\n' + user_input
        else:
             user_input = input("User input: ")
        return user_input

    user_input = premium_client() #Here is a short version if the client is not on premium we will just ask him (we should create a function which will be called if the client is not premium)

    response = generate_response(user_input)
    print("AI: " + response) #The response from AI
    save_current_input(user_input)

    def determine_mood(): #We are tellling the AI to take choose the client_mood our client has depending on the client request
        determine_client_mood = "'" + user_input + "'" + " , based on my  request, what client_mood am I: 'sad', 'happy', 'fear', 'angry', 'neutral' (One word, output) "
        client_mood = generate_response(str(determine_client_mood)) #In the data of AI he knows the previous request so we determine the client_mood
        return client_mood

    mood = determine_mood() #Determening the client_mood
    print("AI decision: " + mood)
    save_current_mood(mood)

    googleAPI = YouTubeAPI(api_key_you_tube)
    googleAPI.search_for_video(user_input)
    #googleAPI.get_video_ids()

    #userVideo = YouTubeMusicDownload()
    #userVideo.download_audio([f'https://www.youtube.com/watch?v={video_id}')


# Run the program
if __name__ == "__main__":
    main()
