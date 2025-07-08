from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # Connect to MongoDB (with error handling and timeout)
    client = MongoClient(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=5000  # 5 second timeout
    )
    
    # Verify connection by pinging the server
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    
    # Access database
    db = client["tweet_db"]
    
    # Access collection
    tweets_collection = db["tweets"]
    
    # Test collection access
    print(f"Collection stats: {tweets_collection.count_documents({})} documents")
    
except ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
except Exception as e:
    print(f"An error occurred: {e}")