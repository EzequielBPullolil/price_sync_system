"""
    Here the layer exceptions and specific case are defined
"""


class DomainException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class ApplicationLayerException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class MissingRequiredEntry(ApplicationLayerException):
    def __init__(self, missingEntry):
        super().__init__(
            message=f"The entry {missingEntry} is missing")


class AlreadyRegisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is already registered")


class UnregisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is unregistered")
