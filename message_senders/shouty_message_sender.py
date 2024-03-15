from user_messager_interface import UserMessager

class ShoutyUserMessager(UserMessager):
    def show_user_message(self, message):
        print(f'HEY USER THIS IS YOUR MESSAGE!! {message}')