import requests
import os
from config import *
import thecampy


class Spy:
    # change below to fetch information from README.md
    # since issue comment is editable only by comment creator
    def get_soldiers_from_readme(repo_url="guzus/nonsan-trainee-news"):
        r = requests.get(
            f"https://api.github.com/repos/{repo_url}/issues/{issue_no}",
            auth=(os.environ.get("GITHUB_ID"), os.environ.get("GITHUB_ACCESS_KEY")),
        )
        body = r.json().get("body")
        print(body)

        if r.status_code != 200:
            raise Exception()

        soldiers = []
        soldier_rows = body.split("\n")[2:]
        for soldier_row in soldier_rows:
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

        return soldiers
