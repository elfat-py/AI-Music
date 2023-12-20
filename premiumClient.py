class PremiumClient:
    def premium_client(self):

        previous_input = self.save_data.load_previous_input()
        user_input = input("How are you feeling today: ")
        if previous_input:
            user_input = previous_input + '\n' + user_input
        else:
            user_input = input("How are you feeling today: ")
        return user_input

    pass