from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import os
from util.get_colors import get_colors

router = Blueprint("item", __name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@router.route("/get-colors", methods=["POST"])
def post_image():

    if "file" not in request.files:
        return jsonify({"error": "No File Part"})

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No Selected File"})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        colors = get_colors(filepath, 16)

        return jsonify(colors)
    else:
        return jsonify({"error": "File Type Not Allowed"})

    return
