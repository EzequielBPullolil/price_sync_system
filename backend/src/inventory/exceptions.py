from src.exceptions import DomainException


class AlreadyRegisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is already registered")


class UnregisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is unregistered")
