from src.exceptions import DomainException


class InvalidUserField(DomainException):
    def __init__(self, field):
        super().__init__(
            message=f"The field'{field}' is invalid")


class InvalidLoginCredentials(DomainException):
    def __init__(self):
        super().__init__(
            message=f"Invalid login credentials")


class UnauthorizedUser(DomainException):
    def __init__(self):
        super().__init__(
            message=f"User permissions are not enough to enter this endpoint")


class AlreadyRegisteredName(DomainException):
    def __init__(self, name):
        super().__init__(
            message=f"The name {name} is already registered")
