# make exception
class NewException(Exception):
    def __init__(self, error, message=""):
        self.error = error
        self.message = message
        if message != "":
            super().__init__(self.message)
        else:
            super().__init__(f"A {self.error} has occured")

# test exception
raise NewException("test")