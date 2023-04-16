from flask import render_template, Blueprint
from models.action_model import ActionModel

action_bp = Blueprint("action", __name__, url_prefix="/actions")

@action_bp.route('/')
def index():
  actions = ActionModel().GetActions()
  return render_template("actions/index.html", actions=actions)

@action_bp.route('/<int:action_id>/edit')
def edit(action_id:int):
  action = ActionModel().GetAction(action_id)
  return render_template("actions/edit.html", action=action)