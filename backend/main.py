from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Tweet, TweetRequest
from database import tweets_collection
from bson.objectid import ObjectId
import requests

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Keys (keep secret in production)
OPENROUTER_API_KEY = # when you using then put your api key 
TWITTER_CLONE_API_KEY = # when you using then put your api key 
TWITTER_CLONE_URL = # when you using then put your api key 

# === 1. Generate Tweet with DeepSeek model ===
@app.post("/generate-tweet")
def generate_tweet(request: TweetRequest):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "Tweet Generator Bot"
    }

    payload = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who writes concise, interesting tweets."},
            {"role": "user", "content": request.prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("OpenRouter API error:", response.text)
        raise HTTPException(status_code=500, detail="OpenRouter API failed")

    try:
        content = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("Parse error:", response.json())
        raise HTTPException(status_code=500, detail="Unexpected response from OpenRouter")

    return {"content": content}


# === 2. Save Tweet as Draft ===
@app.post("/save-draft")
def save_draft(tweet: Tweet):
    tweet.status = "draft"
    result = tweets_collection.insert_one(tweet.dict())
    return {"id": str(result.inserted_id)}


# === 3. Post Tweet to Twitter Clone ===
@app.post("/post-tweet/{tweet_id}")
def post_tweet(tweet_id: str):
    tweet_data = tweets_collection.find_one({"_id": ObjectId(tweet_id)})
    if not tweet_data:
        raise HTTPException(status_code=404, detail="Tweet not found")

    payload = {
        "username": TWITTER_CLONE_API_KEY.split("_")[0],  # You can change this name if needed
        "text": tweet_data.get("content", "")
    }

    headers = {
        "api-key": TWITTER_CLONE_API_KEY
    }

    print("Sending to Twitter Clone:", payload)

    response = requests.post(TWITTER_CLONE_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print("Twitter Clone error:", response.status_code, response.text)
        raise HTTPException(status_code=500, detail="Failed to post tweet to Twitter Clone")

    # Mark as posted
    tweets_collection.update_one(
        {"_id": ObjectId(tweet_id)},
        {"$set": {"status": "posted"}}
    )

    return {"message": "Tweet posted successfully"}


# === 4. Get All Tweets ===
@app.get("/tweets")
def get_tweets():
    tweets = []
    for tweet in tweets_collection.find():
        tweets.append({
            "id": str(tweet["_id"]),
            "content": tweet["content"],
            "status": tweet["status"]
        })
    return tweets
