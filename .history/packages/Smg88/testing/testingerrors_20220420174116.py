import errors


class ConditionalError(errors.Error):
    def __init__(self, condition: bool)
