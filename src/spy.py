import requests
import os
from config import *
import thecampy
import base64


class Spy:
    def get_soldiers_from_readme(self, repo_url=REPO_URL):
        r = requests.get(
            f"https://api.github.com/repos/{repo_url}/readme",
            auth=(GITHUB_ID, GITHUB_ACCESS_KEY),
        )
        # print(r.json())
        body = r.json().get("content")
        content = base64.b64decode(body).decode('utf-8')
        print(content)

        if r.status_code != 200:
            raise Exception()

        soldiers = []
        soldier_rows = list(filter(lambda line: "|" in line, content.split("\n")))
        print(soldier_rows)
        for soldier_row in soldier_rows:
            try:
                name, birth, enter_date, unit_name, *_ = soldier_row.replace(" ", "").split(
                    "|"
                )[1:-1]
                soldier = thecampy.Soldier(
                    name,  # '이름',
                    birth,  # '생일(yyyymmdd)',
                    enter_date,  # '입대일(yyyymmdd)',
                    unit_name,  # '부대명(ex: 육군훈련소)'
                )
                soldiers.append(soldier)
            except:
                print("parse error")

        return soldiers
