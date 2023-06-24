from flask import Blueprint, jsonify, request
from src.db import DbSession
from src.auth.decorators import role_required
from .services import RoleManager, UserModifierService
from src.user_role.role_enum import RolesID
roles_bp = Blueprint('roles', __name__, url_prefix='/roles')
users_bp = Blueprint('users', __name__, url_prefix='/users')


@roles_bp.route("/", methods=["GET"],  strict_slashes=False)
def list_roles():
    """
      responds with a list of all available roles
    """
    session = DbSession()
    role_manager = RoleManager(session)

    roles = role_manager.find_all_roles()
    session.close()
    return jsonify(roles), 200


@roles_bp.route("/<role_id>", methods=["GET"],  strict_slashes=False)
def get_user_with_role(role_id):
    """
      responds with a list of all available roles
    """
    session = DbSession()
    role_manager = RoleManager(session)

    users = role_manager.find_all_user_with_role(role_id)
    session.close()
    return jsonify(users), 200


@users_bp.route("/<user_id>", methods=["PUT"],  strict_slashes=False)
@role_required(RolesID.MASTER.value)
def modify_user(user_id):
    """
      Modifies the user belonging to the id passed by the url
      param and returns the userDAO along with the status message
      The endpoint requires the user to be a master
      The only user field that cannot be modified is the ID

      In case of passing the "name" field, the name should not be registered.
      :urlparams
        user_id(uuid): The id of the user to update
      :headers JWT
      All req bodies are optional
      :reqbody
        - name(str): The new name of user
        - password(str): The new password of user
        - role_id(int): The new role_id of user
      :jsonresponse
        - status(str): The request status 
        - user(dict): The updated user
    """
    session = DbSession()
    user_modifier = UserModifierService(session)

    modified_user = user_modifier.modify_by_id(user_id, newFields=request.get_json())

    session.close()

    return {
        "status": "User modified",
        "user": modified_user.to_dict()
    }
