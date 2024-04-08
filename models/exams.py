import json
import requests

from .constants import SERVER_URL

class Exam:
    ENDPOINT = "/exams/"

    def __init__(self, subject=None, academic_year=None, session=None, duration=None, id=None) -> None:
        self.id = id
        self.subject = subject
        self.academic_year = academic_year
        self.session = session
        self.duration = duration
        self.files = []

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'subject': self.subject,
        'session': self.session,
        'duration': self.duration,
        'academic_year': self.academic_year}
        files=[
        ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        ('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        self.id = data['id']

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if id:
            exam = __class__(**response)
            return exam
        else:
            exams = []

            for result in response:
                exam = __class__(**result)
                exams.append(exam)
            
            return exams

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise exception