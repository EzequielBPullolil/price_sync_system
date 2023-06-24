"""
    Here the layer exceptions and specific case are defined
"""


class DomainException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class MissingRequiredField(DomainException):
    def __init__(self, field):
        super().__init__(
            message=f"Missing the required field '{field}'")


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


class UnregisteredRole(DomainException):
    def __init__(self, role_id):
        super().__init__(
            message=f"The role with id {role_id} is unregistered")
