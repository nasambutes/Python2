import requests
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = 'teresiawaliuba13@gmail.com'
receiver_email = 'wakahiad@gmail.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_email
smtp_password = 'your_email_password'

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of the email'

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
    # Email body
    message.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f'Error: {str(e)}')

    finally:
        server.quit()


def main():
    while True:
        send_notification(f"Your favorite player won a set in match {match['id']}!")
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
