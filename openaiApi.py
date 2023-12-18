import os
from openai import OpenAI
from dotenv import load_dotenv


"""
Currently the response we get seems to be outdated and quite old
-The suggested music is outdated
-Does not suit so well based to the user input
"""
# load_dotenv()
# client = OpenAI(
#     # The key is going to be received by .env file in the same directory
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )
#
#
# def music_suggestion_openai(user_input):
#     returned_output = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": "You are some music therapist suggestor that helps people by picking up a music based on "
#                                           "their sentences which represent their current mood. The music should be suitable for the user and as lately dated as possible."
#                                           "IMPORTANT(you should always provide a music) - Format: music name and artist band or what ever"},
#             {"role": "user", "content": user_input},
#         ],
#         model="gpt-4",
#         temperature=0.3
#     )
#     return returned_output.choices[0].message.content  # Scripting the output that will be shown to the users


from dotenv import load_dotenv
from openai import OpenAI
import os

class OpenAiAPI:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def music_suggestion(self, user_input):
        returned_output = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are some music therapist suggestor that helps people by picking up a music based on "
                                              "their sentences which represent their current mood. The music should be suitable for the user and as lately dated as possible."
                                              "IMPORTANT(you should always provide a music) - Format: music name and artist band or whatever"},
                {"role": "user", "content": user_input},
            ],
            model="gpt-4",
            temperature=0.3
        )
        return returned_output.choices[0].message.content

if __name__ == "__main__":
    # Assuming your OpenAI API key is stored in the .env file as OPENAI_API_KEY
    music_therapist = OpenAiAPI("OPENAI_API_KEY")

    user_input = input("Enter a sentence to get a music suggestion: ") #This one should be the user arg we get from main

    try:
        suggestion = music_therapist.music_suggestion(user_input)
        print("Music Suggestion:", suggestion)
    except Exception as e:
        print(f"An error occurred: {e}")





# There are needed some adjustments, should:
# * Create a premium mode
# * Better speed
# * Up to 3 videos recommended
# * AI knows what was the previous mood of the user etc...


# You are some music therapist suggestor that helps people by picking up a music based on
# their sentences which represent their current mood. The music should be suitable for the user and as lately dated as possible. IMPORTANT(you should always provide a music) - Format: music name and artist band or what ever