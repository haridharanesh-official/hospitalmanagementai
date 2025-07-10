from flask import Blueprint, request, jsonify
from flask_login import login_required

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    data = request.json
    message = data.get('message', '').lower()

    # Simple rule-based logic (can be replaced with OpenAI or Ollama)
    if "headache" in message:
        reply = "You should rest and stay hydrated. Would you like to alert the nurse?"
    elif "heart rate" in message:
        reply = "Please wait while I fetch your latest heart rate from vitals."
    else:
        reply = "I'm here to assist you. Can you describe your symptoms?"

    return jsonify({'reply': reply})
