from flask import request

from src.exceptions import MissingRequiredEntry


def required_inventory_entries(func):
    """
      Verify that the required fields exist in
      json request
    """
    def wrapper(*args, **kwargs):
        try:
            data = request.get_json()
            for field in ["barcode", "name", "price", "stock"]:
                data[field]
            return func(*args, **kwargs)
        except KeyError as e_info:
            raise MissingRequiredEntry(e_info)

    return wrapper
