from flask import Blueprint, request
from src.user_role.role_enum import RolesID
from src.user.decorators import role_required
from .services.user_creator import UserCreator
from src.db import DbSession
user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route("/", methods=["POST"],  strict_slashes=False)
@role_required(RolesID.MASTER.value)
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
    session = DbSession()
    user_creator = UserCreator(session)

    created_user_dao = user_creator.create(request.get_json())
    session.close()
    return {
        "status": "User created",
        "user": created_user_dao.to_dict()
    }, 201
