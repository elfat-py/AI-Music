user_requests = 'previous_input.txt'
user_moods = 'moodOfClient.txt'



#Check if there was a previous request from the user before to use as a reference
def load_previous_input():
    try:
        with open(user_requests, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""


# Saving the data (The requests the user does)
def save_current_input(input_text):
    with open(user_requests, 'w') as file:
        file.write(input_text)




#Check what was the mood of the client or save it
def load_previous_mood():
    try:
        with open(user_moods, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

def save_current_mood(user_text):
    with open(user_moods, 'w') as file:
        file.write(user_text)

