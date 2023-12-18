

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    # The key is going to be received by .env file in the same directory
    api_key=os.environ.get("OPENAI_API_KEY"),
)
userInput = input("How are you feeling today: ")


def music_suggestion_openai(user_input):
    returned_output = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are some therapist that helps people by picking up a music based on "
                                          "their mood, your return output should be in the following format: name of "
                                          "music + artist or band}"},
            {"role": "user", "content": user_input},
        ],
        model="gpt-4",
        temperature=0.6
    )
    return returned_output.choices[0].message.content  # Scripting the output that will be shown to the users


music_suggestion_openai(user_input=userInput)

#The code here is not finished the version should be checked and also the engine response is not near
#  close to a good response


#There are needed some adjustments (should
# * Create a premium mode
# * Better speed
# * Up to 3 videos recommended
# * AI knows what was the previous mood of the user etc...)
