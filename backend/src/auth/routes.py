from flask import Blueprint, request
from src.user_role.role_enum import RolesID

from src.auth.decorators import role_required, validate_create_user_fields
from src.decorators import required_fields
from .services import RegisterService, LoginService
from src.db import DbSession
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route("/register", methods=["POST"],  strict_slashes=False)
@role_required(RolesID.MASTER.value)
@required_fields(["name", "password", "role_id"])
@validate_create_user_fields
def register():
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
    register_service = RegisterService(session)

    created_user_dao = register_service.register(request.get_json())
    session.close()
    return {
        "status": "Successful registration",
        "user": created_user_dao.to_dict()
    }, 201


@auth_bp.route("/login", methods=["POST"],  strict_slashes=False)
@required_fields(["name", "password"])
def login():
    """
      Validate user credentials and create session
    """
    sessionDb = DbSession()
    login_service = LoginService(sessionDb)
    user = login_service.validate_credentials(request.get_json())
    generated_token = login_service.generate_token(user)
    sessionDb.close()
    return {
        "status": "success",
        "message": "Successful login",
        "token": generated_token
    }, 200
