from flask import Flask, jsonify, request
import json
import random
import threading
import time

app = Flask(__name__)

#load quotes from file
with open("quotes.json", "r") as file:
    QUOTES = json.load(file)

#notification state
NOTIFICATIONS_ENABLED = False

def fetch_random_quote(category=None):
    """Fetch a quote from the local JSON file."""
    if category and category in QUOTES:
        return random.choice(QUOTES[category])
    all_quotes = [q for cat in QUOTES.values() for q in cat]
    return random.choice(all_quotes)

@app.route("/quote", methods=["GET"])
def get_quote():
    """Endpoint to return a random quote."""
    return jsonify(fetch_random_quote())

@app.route("/quote/<category>", methods=["GET"])
def get_quote_by_category(category):
    """Endpoint to return a quote filtered by category."""
    if category in QUOTES:
        return jsonify(fetch_random_quote(category))
    return jsonify({"error": "Invalid category. Choose from: confidence, excellence, inspiration, success, time."}), 400

@app.route("/notifications", methods=["POST"])
def toggle_notifications():
    """Enable or disable daily notifications."""
    global NOTIFICATIONS_ENABLED
    data = request.json
    if "enabled" in data and isinstance(data["enabled"], bool):
        NOTIFICATIONS_ENABLED = data["enabled"]
        state = "enabled" if NOTIFICATIONS_ENABLED else "disabled"
        return jsonify({"message": f"Daily notifications {state}."})
    return jsonify({"error": "Invalid request. Send JSON with 'enabled': true or false."}), 400

def notification_worker():
    """Background thread to send quotes every 10 seconds when notifications are enabled."""
    global NOTIFICATIONS_ENABLED
    while True:
        if NOTIFICATIONS_ENABLED:
            quote = fetch_random_quote()
            print("\n--- Daily Motivational Quote ---")
            print(f'"{quote["q"]}"')
            print(f'— {quote["a"]}')
            print("--------------------------------\n")
        time.sleep(10)  # 10-second interval for demo purposes

#start notification worker in a separate thread
threading.Thread(target=notification_worker, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5101, debug=True)
