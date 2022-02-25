import thecampy


class Postman:
    def __init__(self, email, password) -> None:
        self.client = thecampy.Client(email, password)

    def send_letters(self, letters, soldiers):
        for soldier in soldiers:
            self.client.add_soldier(soldier)  # if needed
            for letter in letters:
                msg = thecampy.Message(letter.get("title"), letter.get("content"))
                self.client.send_message(soldier, msg)
