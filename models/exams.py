import json
import requests

from .constants import SERVER_URL

class Exam:
    ENDPOINT = "/exams"

    def __init__(self, subject=None, academic_year=None, session=None, duration=None) -> None:
        self.id = id
        self.subject = subject
        self.academic_year = academic_year
        self.session = session
        self.duration = duration

    def save(self):
        pass

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        response = json.loads(requests.get(url))

        if id:
            exam = __class__(**response)
            return exam
        else:
            exams = []

            for result in response:
                exam = __class__(**result)
                exams.append(exam)
            
            return exams