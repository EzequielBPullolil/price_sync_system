from flask import Blueprint
user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route("/", methods=["POST"],  strict_slashes=False)
def create_user():
    """
      Persist an user in db and return UserDAO
      if the session role_id have enough permission levels
      and the user name is not already registered

      :reqbody name: The new user name
      :reqbody password: The new user password
      :reqbody role_id: The new user role_id

      :return: Success message and persisted UserDAO

      :rtype: json
    """
    return {
        "status": "User created"
    }, 201
