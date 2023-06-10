"""
    Here the layer exceptions and specific case are defined
"""


class DomainException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class UnauthorizedUser(DomainException):
    def __init__(self):
        super().__init__(
            message=f"User permissions are not enough to enter this endpoint")


class ApplicationLayerException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class MissingRequiredEntry(ApplicationLayerException):
    def __init__(self, missingEntry):
        super().__init__(
            message=f"The entry {missingEntry} is missing")


class AlreadyRegisteredName(DomainException):
    def __init__(self, name):
        super().__init__(
            message=f"The name {name} is already registered")


class AlreadyRegisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is already registered")


class UnregisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is unregistered")
