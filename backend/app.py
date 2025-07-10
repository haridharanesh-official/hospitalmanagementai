from flask import Flask
from models.database import db
from routes.vitals import vitals_bp
from routes.chat import chat_bp
from routes.auth import auth_bp, login_manager
from config import Config
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Init extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"

with app.app_context():
    db.create_all()
    logger.info("Database tables created.")

# Register Blueprints
app.register_blueprint(vitals_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return "Hospital Automation AI Nurse Chatbot is running!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        return render_template("dashboard_admin.html", user=current_user)
    else:
        return render_template("dashboard_patient.html", user=current_user)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
