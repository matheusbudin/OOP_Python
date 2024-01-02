from .user import User

class BasicUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.user_type = "Basic"

    def display_info(self):
        return super().display_info() + f", Type: {self.user_type}"
