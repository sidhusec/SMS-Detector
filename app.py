from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allows frontend to access backend

SCAM_KEYWORDS = ["urgent", "immediate action required", "your account is suspended", "verify your identity",
                 "click the link", "limited time offer", "congratulations you won", "claim your prize",
                 "free gift", "update your payment", "suspicious activity detected", "unauthorized login attempt",
                 "reset your password", "account verification", "security alert", "confirm your details",
                 "final notice", "lottery winner", "transfer funds", "act now", "urgent response needed",
                 "verify your card", "banking alert", "paypal alert", "your card is blocked", "refund available",
                 "overdue invoice", "fake invoice", "payment failed", "confirm payment", "request for donation",
                 "government grant", "tax refund", "debt collection", "confidential information needed",
                 "ssn required", "winning notification", "bitcoin investment", "crypto giveaway", "gift card scam",
                 "you have been selected", "dear customer", "dear user", "official notice", "click below",
                 "login required", "your subscription expired", "renew now", "account compromised",
                 "important notification", "act immediately", "final warning", "unusual transaction",
                 "billing issue", "verify phone number"]

def is_fraudulent(message):
    message_lower = message.lower()
    for word in SCAM_KEYWORDS:
        if word in message_lower:
            return True
    return False

@app.route("/")  
def home():
    return "Backend is running! Use /check endpoint for SMS detection."

@app.route("/check", methods=["POST"])  # ✅ Must use POST
def check_message():
    try:
        data = request.get_json(force=True)  # ✅ Ensures JSON parsing

        if not data or "message" not in data:
            return jsonify({"error": "No message provided"}), 400

        message = data["message"]
        result = "⚠️ Fraudulent Message!" if is_fraudulent(message) else "✅ Safe Message"

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ Returns error details

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # ✅ Runs on all devices in network
