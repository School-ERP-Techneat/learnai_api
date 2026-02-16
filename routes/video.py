import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from bson import ObjectId
from extensions import mongo

video_bp = Blueprint("video", __name__)

@video_bp.route("/upload", methods=["POST"])
@jwt_required()
def upload_video():
    if "video" not in request.files:
        return jsonify({"error": "No video file"}), 400
    
    file = request.files["video"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
    
    user_id = get_jwt_identity()
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$inc": {"progress": 33}}
    )
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
    return jsonify({"message": "Video uploaded", "progress": user["progress"]})
