class UserInterface:

    def __init__(self, user_message_sender):
        self.user_message_sender = user_message_sender

    def show_message(self, message):
        self.user_message_sender.show_user_message(message)
