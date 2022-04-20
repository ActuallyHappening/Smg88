import errors


class ConditionalError(errors.Error):
    def __init__(self, condition: bool, /, *, check: bool = True):
        super().__init__(f"ConditionalError: {condition!r}")
        if bool(condition) is bool(check):
            raise self


class ExpectedError(ConditionalError):
    def __init__(self, condition: bool):
        super().__init__(condition=condition, check=False)


class TestError(ConditionalError):
    def __init__(self, condition: bool):
        super().__init__(condition=condition, check=True)
