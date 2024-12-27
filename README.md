# Kibby
🌟 About The Project
This Python-based Twitter Auto-Post Bot automates tweeting, Credit to the Tweepy library for making this easy, this project enables scheduled and random tweets, offering a dynamic and engaging Twitter experience.

📁 Files Overview
Using OpenAI
Instantly:
src/instantly-tweet-from-openai.py: Immediately tweets a tweet from openAI api response, currently using GPT4

Prompt defined here
Schedule to auto post, tweet daily at a time:
src/schedule-daily-post-from-openai.py: Automates daily tweets, Runs daily at a scheduled time and queries open ai api to create a tweet, the tweet returned is then automatically tweeted each day to fully automate twitter on auto pilot. By default the model is OPENAI GPT4 
Prompt defined here
Schedule time defined here
From File
src/schedule-daily-post-from-file.py: Automates daily tweets, randomly selecting from tweets.txt.
src/tweeter-random-from-file.py: Instantly posts a random tweet from tweets.txt.
Added tweets to data/tweets.txt: one per line. They will be randomly selected and tweeted.
Manually tweeting using script
src/tweeter-from-code.py: Immediately tweets a pre-defined message with the current date, but you can change this to whatever you like.

common files
config/keys.py: Holds both the creds for openai and twitter api.
src/functions.py: Shared functions for generating tweets from openai and tweet posting
requirements.txt: Lists all necessary Python packages.
📁 Upcoming Features
Adding CLI.
📁 Current Features
pip install -r requirements.txt
bearer_token = "GET_KEY_FROM_developer.twitter.com/apps"
api_key = "GET_KEY_FROM_developer.twitter.com/apps"
api_secret = "GET_KEY_FROM_developer.twitter.com/apps"
access_token = "GET_KEY_FROM_developer.twitter.com/apps"
access_token_secret = "GET_KEY_FROM_developer.twitter.com/apps"
openai_key = "GET_YOUR_OPENAI_API_KEY_FROM_https://platform.openai.com/api-keys"

🔧 Usage
Running script using Python:

cd src/
python instantly-tweet-from-openai.py
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
