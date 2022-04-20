import errors


class ConditionalError(errors.Error):
    def __init__(self, condition: bool, /, *, check: bool = True):
        super().__init__(f"ConditionalError: {condition!r}")
        if bool(condition):
            raise self
