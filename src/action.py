import thecampy
from reporter import Reporter
from postman import Postman
from spy import Spy
from config import *

# get list of soldiers from issue
soldiers = Spy().get_soldiers_from_readme()

# reporter fetches news
letters = Reporter().publish_letters()

Postman(email=EMAIL, password=PASSWORD).send_letters(letters, soldiers)
