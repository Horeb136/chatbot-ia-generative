from dotenv import load_dotenv
import os 
import praw
import json 

# Get env variables 
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_APP_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_APP_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

# Check some posts about "artificial"
subreddit = reddit.subreddit('artificial')
posts = []

for submission in subreddit.search("Generative AI", limit=10):
    posts.append({
        'title': submission.title,
        'selftext': submission.selftext,
        'url': submission.url,
        'score': submission.score,
        'comments': submission.num_comments
    })

# Save data 
with open('reddit_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)

print("Données Reddit sauvegardées avec succès !")