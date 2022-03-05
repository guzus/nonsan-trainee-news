import thecampy


class Postman:
    def __init__(self, email, password) -> None:
        self.client = thecampy.Client(email, password)

    def send_letters(self, letters, soldiers):
        for soldier in soldiers:
            try:
                self.client.add_soldier(soldier)  # if needed
                print("훈련병 추가 성공")
            except Exception as e:
                print("훈련병 추가 실패", e)
            for letter in letters:
                try:
                    msg = thecampy.Message(
                        title=letter.get("title"), content=letter.get("content")
                    )
                    print(soldier, msg)
                    self.client.send_message(soldier=soldier, message=msg)
                    print("편지 전송 성공")
                except Exception as e:
                    print("편지 전송 실패", e)
