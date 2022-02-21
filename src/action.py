import thecampy
from .reporter import Reporter
from .postman import Postman
from .spy import Spy

# get list of soldiers from issue
soldiers = Spy.get_soldiers_from_issue()

# reporter fetches news
letters = Reporter.publish_letters()

# email, pw is from environment variables
Postman(email=1, password=1).send_letters(letters, soldiers)
