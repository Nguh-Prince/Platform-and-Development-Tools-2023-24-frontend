import os
import json
import requests

from .constants import SERVER_URL

class Subject:
    ENDPOINT = "/subjects/"

    def __init__(self, name, id=None) -> None:
        self.id = id
        self.name = name

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'name': self.name}
        headers = {}

        if not self.id: # save to the backend with a POST request
            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            data = json.loads(response.text)
            self.id = data['id']
        else: # update a particular subject
            url += str(self.id)
            response = requests.request("PATCH", url, headers=headers, data=payload, files=files)


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
        except Exception as e:
            raise e