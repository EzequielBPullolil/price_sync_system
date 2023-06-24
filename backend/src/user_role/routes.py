from flask import Blueprint, jsonify
from src.db import DbSession
from .services.role_manager import RoleManager
roles_bp = Blueprint('roles', __name__, url_prefix='/roles')


@roles_bp.route("/", methods=["GET"],  strict_slashes=False)
def list_roles():
    """
      responds with a list of all available roles
    """
    session = DbSession()
    role_manager = RoleManager(session)

    roles = role_manager.find_all_roles()

    return jsonify(roles), 200
