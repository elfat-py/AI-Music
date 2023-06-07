import openai

# OpenAI API key
openai.api_key = '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'

def generate_response(user_input):
    response = openai.Completion.create(
        engine ='text-davinci-003',  # Use the ChatGPT 3.5 turbo engine, text-davinci-003
        prompt =user_input,
        max_tokens=50,  # Adjust the max tokens according to your needs(nr of words)
        temperature=0.7,  #Temperature (0-2) is a parameter that will tell us how random we want the output, (ex. greater values more random the input)
        n=1, #The number of returned (outputs we want to get from the user)
        stop=None, #Nr of sequences for input
        echo=False #Return the input with output(In our case we got output and the input)
    )
    return response.choices[0].text.strip() #parsing the part we need from the code
'''
def search_music_by_feeling(feeling):
    prompt = f"Find me a song that matches the feeling: {feeling}."
    response = openai.Completion.create(
        engine='chat-gpt-004',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the generated song from the API response
    generated_song = response.choices[0].text.strip().split('\n')[0]

    return generated_song
# Ask the user for their feeling
user_input = input("How are you feeling? ")

# Search for music based on the user's feeling
recommended_song = search_music_by_feeling(user_input)

print(f"Recommended song for {user_input}:")
print(recommended_song)
print()
'''
#The code here is not finished the version should be checked and also the engine response is not near
#  close to a good response


#There are needed some adjustments (should
# * Create a premium mode
# * Better speed
# * Up to 3 videos recommended
# * AI knows what was the previous mood of the user etc...)
