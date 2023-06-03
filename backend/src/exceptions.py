class DomainException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.status = "error"


class AlreadyRegisteredBarcode(DomainException):
    def __init__(self, barcode):
        super().__init__(
            message=f"The barcode {barcode} is already registered")
