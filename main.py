import task_performer 
from user_interface import UserInterface
from message_senders.shouty_message_sender import ShoutyUserMessager
from message_senders.polite_message_sender import PoliteUserMessager

def main():

    # Create a UI object to show the user messages
    # This class needs to receive a UserMessager object, so create one to pass to the UserInterface class 
    user_messager = ShoutyUserMessager()
    ui = UserInterface(user_messager)  # Create UserInterface object, passing in the user_messager object 

    # Pretend this is doing some task 
    task_result = task_performer.do_task()

    # UserInterface displays result to user 
    ui.show_message(task_result)


main()