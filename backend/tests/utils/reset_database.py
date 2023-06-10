from sqlalchemy import text


def reset_database(session):
    """
      Deletes all rows of database
    """
    session.execute(
        text("DELETE FROM user_role")
    )
    session.execute(
        text("DELETE FROM roles")
    )

    session.execute(
        text("DELETE FROM inventorys")
    )
    session.execute(
        text("DELETE FROM users")
    )
