from user_messager_interface import UserMessager

class PoliteUserMessager(UserMessager):
    def show_user_message(self, message):
        print(f'Dear user, here is your message: {message}')