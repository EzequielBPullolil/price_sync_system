class UserDAO:
    def __init__(self, user_query_response, role_name) -> None:
        """
          gets the response from an orm request and converts it to a Data access object
        """
        self.id = user_query_response.get_id()
        self.name = user_query_response.name
        self.role_name = role_name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "role_name": self.role_name
        }
