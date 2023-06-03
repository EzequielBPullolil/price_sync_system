class InventoryDAO:
    def __init__(self, query_response) -> None:
        self.name = query_response.name
        self.price = query_response.price
        self.stock = query_response.stock

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
