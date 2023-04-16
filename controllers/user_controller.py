from flask import render_template, Blueprint
from models.user_model import UserModel

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route('/')
def index():
  users = UserModel().GetUsers()
  return render_template("users/index.html", users=users)

@user_bp.route('/<int:user_id>/edit')
def edit(user_id:int):
  user = UserModel().GetUser(user_id)
  return render_template("users/edit.html", user=user)