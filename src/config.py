import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("THE_CAMP_EMAIL")
PASSWORD = os.environ.get("THE_CAMP_PASSWORD")
GITHUB_ID = os.environ.get("MY_GITHUB_ID")
GITHUB_ACCESS_KEY = os.environ.get("MY_GITHUB_ACCESS_KEY")
REPO_URL = "guzus/nonsan-trainee-news"
