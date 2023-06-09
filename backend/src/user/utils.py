class UserDAO:
    def __init__(self, user_query_response) -> None:
        """
          gets the response from an orm request and converts it to a Data access object
        """
        self.id = user_query_response.id
        self.name = user_query_response.name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }
