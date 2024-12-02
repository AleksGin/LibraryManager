class InputError(ValueError):
    pass


class EmptyValueError(InputError):
    pass


class InvalidTypeError(EmptyValueError):
    pass


class NegativeValueError(InvalidTypeError):
    pass
