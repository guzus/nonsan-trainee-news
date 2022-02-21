import requests

class Spy:
    def get_soldiers_from_issue():
        r = requests.get(
            f"https://api.github.com/repos/{repo_url}/issues/{issue_no}",
            auth=("guzus", GITHUB_ACCESS_KEY),
        )
        body = r.json().get("body")
        if r.status_code != 200:
            raise Exception()

        print(body)

        # my_soldier = thecampy.Soldier(
        #     '이름',
        #     '생일(yyyymmdd)',
        #     '입대일(yyyymmdd)',
        #     '부대명(ex: 육군훈련소)'
        # )

        return []
