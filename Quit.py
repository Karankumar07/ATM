class Quit:
    def __init__(self, atm_interface):
        self.atm_interface = atm_interface

    def quit(self):
        self.atm_interface.logout()
        print("Logged out. Goodbye!")