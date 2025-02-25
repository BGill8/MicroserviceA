import requests

MICROSERVICE_URL = "http://localhost:5101"
def fetch_quote(category=None):
    """Fetch a quote from the microservice."""
    url = f"{MICROSERVICE_URL}/quote/{category}" if category else f"{MICROSERVICE_URL}/quote"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            quote = response.json()
            print("\n--- Motivational Quote ---")
            print(f'"{quote["q"]}"')
            print(f'— {quote["a"]}')
            print("--------------------------\n")
        else:
            print("Error fetching quote:", response.text)
    except requests.RequestException:
        print("Failed to connect to the microservice.")

def toggle_notifications(enable):
    """Enable or disable daily notifications."""
    url = f"{MICROSERVICE_URL}/notifications"
    try:
        response = requests.post(url, json={"enabled": enable}, timeout=5)
        print(response.json()["message"])
    except requests.RequestException:
        print("Failed to connect to the microservice.")

def main():
    """Main function to interact with the user."""
    while True:
        print("\n=== Motivational Quote Client ===")
        print("1. Get a random motivational quote")
        print("2. Get a quote by category")
        print("3. Enable daily notifications")
        print("4. Disable daily notifications")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            fetch_quote()
        elif choice == "2":
            print("\n=== Categories ===")
            print("confidence, excellence, inspiration, success, time")
            category = input("Enter category: ").lower()
            fetch_quote(category)
        elif choice == "3":
            toggle_notifications(True)
        elif choice == "4":
            toggle_notifications(False)
        elif choice == "5":
            print("Exiting program. Stay motivated!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
