class ResultNotFoundError(Exception):
    def __init__(
        self,
        message: str = "There has been an error. Please check your entered data and try again. If you continue to experience problems, please contact us for assistance.",
    ):
        self.message = message

    def __str__(self):
        return self.message
