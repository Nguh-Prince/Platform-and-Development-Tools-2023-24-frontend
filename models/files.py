import os

class File:
    ENDPOINT = "/files"

    def __init__(self, id=None, path=None) -> None:
        self.id = id
        self.path = path

    @property
    def filename(self):
        return os.path.basename(self.path) if self.path else ''