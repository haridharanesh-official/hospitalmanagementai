# 🏥 Hospital Automation AI Nurse Chatbot

An intelligent hospital assistant system that uses an AI chatbot, secure user login, role-based dashboards, and integration with ESP8266 for vitals collection.

---

## 📦 Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🔐 Secure Authentication         | Flask-Login with hashed passwords                                           |
| 👩‍⚕️ AI Nurse Chatbot            | Rule-based chatbot with health logic (OpenAI/Ollama-ready)                 |
| 📡 ESP8266 Integration           | Secure vitals endpoint with token authentication                           |
| 🧑‍⚕️ Role-based Dashboards       | Admin vs Patient view separation                                           |
| 📊 Health Monitoring             | Heart rate, symptoms, and vitals logging (extendable)                      |
| 🧱 Modular Flask App             | Uses Blueprints, templates, and clean structure                            |
| 📜 Logging & Error Handling      | Built-in logging and custom 404/500 pages                                  |
| 🐧 Linux & Raspberry Pi Support | Works on Raspberry Pi OS Lite or Desktop (headless or GUI)                 |

---

## 📁 Project Structure

```bash
Hospital_Automation_AI_Nurse_Chatbot/
├── app.py
├── models/
│   ├── database.py
│   └── user.py
├── routes/
│   ├── auth.py
│   ├── chat.py
│   └── vitals.py
├── templates/
│   ├── dashboard_admin.html
│   ├── dashboard_patient.html
│   ├── 404.html
│   └── 500.html
├── .env
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### ✅ Requirements

- Python 3.7+
- pip
- SQLite (default)
- (Optional) Raspberry Pi OS with Python 3 and internet

---

### 🧪 First Time Setup

#### 🔹 1. Clone or unzip project
```bash
unzip hospitalmanagementai.zip
cd hospitalmanagementai
```

#### 🔹 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔹 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 🔹 4. Set your environment secrets

Create a `.env` file:

```env
SECRET_KEY=your_flask_secret_key
DEVICE_SECRET=myesp8266token123  # Used for securing vitals endpoint
```

#### 🔹 5. Run the Flask app
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

---

## 🛡️ API Endpoints

| Endpoint              | Method | Auth           | Description                          |
|----------------------|--------|----------------|--------------------------------------|
| `/register`          | POST   | ❌ Public       | Register new user                    |
| `/login`             | POST   | ❌ Public       | Login with username/password         |
| `/logout`            | GET    | ✅ Logged in    | Logout user                          |
| `/me`                | GET    | ✅ Logged in    | Get current user info                |
| `/chat`              | POST   | ✅ Logged in    | Send message to AI chatbot           |
| `/vitals`            | POST   | 🔐 Device Token | Send patient vitals from ESP8266     |
| `/dashboard`         | GET    | ✅ Logged in    | Show role-based dashboard            |

---

## 📡 ESP8266 Usage Example

ESP8266 can post to Flask server using the following headers:

```http
POST /vitals HTTP/1.1
Host: <flask-server-ip>:5000
Authorization: Bearer myesp8266token123
Content-Type: application/json

{
  "heart_rate": 88,
  "temperature": 98.6
}
```

---

## 👥 User Roles

- **Patient**: Access personal chatbot, dashboard
- **Admin**: Access all dashboards, system logs, patient data (extendable)

---

## 🚀 Deploy on Raspberry Pi

1. Follow the same steps above on Raspberry Pi
2. Run app with:

```bash
flask run --host=0.0.0.0 --port=5000
```

3. Visit `http://<raspberry-pi-ip>:5000` in browser

---

## 🔐 Security Notes

- Always use strong secrets in `.env`
- ESP8266 must send a correct `Authorization` header to post vitals
- You can switch to PostgreSQL or MySQL with SQLAlchemy if needed

---

## 📜 License

MIT License - free to use, modify, and distribute.
