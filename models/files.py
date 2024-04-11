import os
import json
import requests

from .constants import SERVER_URL

class File:
    ENDPOINT = "/files/"

    def __init__(self, id=None, path=None, exam=None) -> None:
        self.id = id
        self.path = path
        self.exam = exam

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

    @property
    def filename(self):
        return os.path.basename(self.path) if self.path else ''