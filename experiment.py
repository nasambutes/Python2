import requests
import time

# Replace these with actual API endpoints 
API_BASE_URL = "https://api.example.com/tennis"
API_KEY = "your_api_key_here"

# favorite player (replace with actual player identifier)
FAVORITE_PLAYER_ID = "player123"

def get_live_match_data():
    # Make an API request to get live match data
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{API_BASE_URL}/live-matches", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("error failed to fetch live match data")
        return None

def check_favorite_player_won_set(match_data):
    # Replace this with actual logic to check if your favorite player won a set
    # You'll need to parse the match_data to find your player and set scores
    # For simplicity, let's assume you find the data and determine they won a set
    return True

def send_notification(message):
    # notification method e.g., push notification, email
    print(f"Notification: {message}")

def main():
    while True:
        live_data = get_live_match_data()

        if live_data:
            for match in live_data:
                if FAVORITE_PLAYER_ID in match["players"]:
                    if check_favorite_player_won_set(match):
                        send_notification(f"Your favorite player won a set in match {match['id']}!")

        # Poll every 5 minutes(adjustable)
        time.sleep(300)

if __name__ == "__main__":
    main()
