from dotenv import load_dotenv
import os

def access_env(key):
    load_dotenv()
    return os.getenv(key)
