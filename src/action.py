import thecampy
from reporter import Reporter
from postman import Postman
from spy import Spy
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
GITHUB_ID = os.environ.get("GITHUB_ID")
GITHUB_ACCESS_KEY = os.environ.get("GITHUB_ACCESS_KEY")
REPO_URL = "guzus/nonsan-trainee-news"

# get list of soldiers from issue
soldiers = Spy.get_soldiers_from_issue()

# reporter fetches news
letters = Reporter.publish_letters()

# email, pw is from environment variables
# Postman(demail=EMAIL, password=PASSWORD).send_letters(letters, soldiers)
