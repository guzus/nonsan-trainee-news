import thecampy
from .reporter import Reporter
from .postman import Postman

# get soldiers from issue

my_soldier = thecampy.Soldier(
    '이름',
    '생일(yyyymmdd)',
    '입대일(yyyymmdd)',
    '부대명(ex: 육군훈련소)'
)

# reporter fetches news

msg = thecampy.Message([제목], [내용(1500자 이하)])

# image = thecampy.ThecampyImage('sample.png')

# email, pw is from environment variables
tc = thecampy.Client(email, password)

tc.add_soldier(my_soldier)
# tc.get_soldier(my_soldier) # returns soldier code

tc.send_message(my_soldier, msg, image)