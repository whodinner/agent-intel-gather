from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

# open csv with wordlist
keywords = []
if os.path.exists("keywords.csv"):
    keywords = pd.read_csv("keywords.csv")["keyword"].tolist()

# loadback dataset
if os.path.exists("data.csv"):
    try:
        df = pd.read_csv("data.csv")
        if {"platform", "user", "text"}.issubset(df.columns) and not df.empty:
            posts = df.to_dict(orient="records")
        else:
            posts = []
    except Exception:
        posts = []
else:
    posts = []

# simulation if dataset is missing
if not posts:
    posts = [
        {"platform": "Twitter", "user": "@alice", "text": "My cat is sleeping on the keyboard again"},
        {"platform": "Facebook", "user": "Bob Smith", "text": "Family barbecue on Sunday, can't wait"},
        {"platform": "Reddit", "user": "sunnydays", "text": "Dogs playing in the park are the best"},
        {"platform": "Instagram", "user": "traveller_jane", "text": "Sunset in Bali is breathtaking"},
        {"platform": "LinkedIn", "user": "John Doe", "text": "Team celebrated with cupcakes after the project"},
        {"platform": "TikTok", "user": "danceking", "text": "Check out this funny dog dance video"},
        {"platform": "YouTube", "user": "FoodieChannel", "text": "Top 10 recipes for homemade pizza"},
        {"platform": "Medium", "user": "writer123", "text": "Why cats make the best roommates"},
        {"platform": "HackerNews", "user": "techfan", "text": "Sharing photos of my new puppy"},
        {"platform": "WordPress Blog", "user": "myblog", "text": "Travel packing list for summer holidays"},
        {"platform": "NewsSite", "user": "ReporterX", "text": "Local fair opens with a parade and cotton candy"},
        {"platform": "Discord", "user": "gamer42", "text": "Who is bringing snacks to the movie night"},
        {"platform": "Telegram", "user": "channel_admin", "text": "Sharing cat pictures all week"},
        {"platform": "Quora", "user": "curiousmind", "text": "Why do dogs tilt their heads when we talk"},
        {"platform": "Pinterest", "user": "designlover", "text": "DIY flower arrangements for spring"},
        {"platform": "Snapchat", "user": "funnyfaces", "text": "My dog made a silly face today"},
        {"platform": "Clubhouse", "user": "speaker123", "text": "Live chat about favorite hiking trails"},
        {"platform": "Tumblr", "user": "aestheticvibes", "text": "Vintage cats in art history"},
        {"platform": "Twitch", "user": "streamer42", "text": "Streaming cozy games with my cat nearby"},
        {"platform": "Mastodon", "user": "openworld", "text": "Morning walk with sunshine and coffee"},
        {"platform": "Vimeo", "user": "filmmaker", "text": "Short film featuring a dog adventure"},
        {"platform": "Weibo", "user": "happyuser", "text": "Cats and dogs living together peacefully"},
        {"platform": "Line", "user": "linefriend", "text": "Sending stickers of cute puppies"},
        {"platform": "KakaoTalk", "user": "kakaofan", "text": "Shared a funny cat story with friends"},
        {"platform": "WhatsApp", "user": "familygroup", "text": "Good morning, don't forget to bring cookies"},
        {"platform": "Messenger", "user": "Jane Doe", "text": "Sending love and cat gifs"},
    ]

# keyword detection
def detect_matches():
    matches = []
    for post in posts:
        found = [k for k in keywords if k.lower() in post["text"].lower()]
        if found:
            matches.append({
                "platform": post["platform"],
                "user": post["user"],
                "text": post["text"],
                "matched_keywords": ", ".join(found)
            })
    return matches

# fast api route
@app.get("/")
def root():
    return {"message": "Keyword Detection API is running"}

@app.get("/matches")
def get_matches():
    results = detect_matches()
    return {"matches": results}
