from flask import Blueprint, request, jsonify
from flask_login import login_required
import os

vitals_bp = Blueprint('vitals', __name__)

# Load secret token from env
DEVICE_SECRET = os.getenv("DEVICE_SECRET", "default-secret")

@vitals_bp.route('/vitals', methods=['POST'])
def receive_vitals():
    token = request.headers.get("Authorization")
    if token != f"Bearer {DEVICE_SECRET}":
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    # Here you would validate and store the vitals
    return jsonify({"status": "Vitals received"})
