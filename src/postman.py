import thecampy


class Postman:
    def __init__(self, email, password) -> None:
        self.client = thecampy.Client(email, password)
        pass

    def send_letters(self, letters, soldiers):
        for soldier in soldiers:
            for letter in letters:
                msg = thecampy.Message(letter.get("title"), letter.get("content"))

                self.client.add_soldier(soldier)  # if needed
                # self.client.get_soldier(soldier) # returns soldier code

                self.client.send_message(soldier, msg, image)
