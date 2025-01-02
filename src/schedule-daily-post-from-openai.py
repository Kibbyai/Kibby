import sys
import os
import schedule
import time
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
import keys
from functions import generate_response, initialize_tweepy, get_formatted_date

def send_post():
    prompt = "Create a short tweet about Memecoins."
    response = generate_response(prompt)

    client, _ = initialize_tweepy()
    tweet_text = f"{response}"
    client.create_tweet(text=tweet_text)
    print("Tweet posted successfully")
    
schedule.every().day.at("Random").do(send_post)

while True:
    schedule.run_pending()
    time.sleep(900)
