from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from extensions import mongo

progress_bp = Blueprint("progress", __name__)

@progress_bp.route("/", methods=["GET"])
@jwt_required()
def get_progress():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return jsonify({"progress": user["progress"]})
