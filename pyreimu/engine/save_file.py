

from datetime import date
import json


class Save:
    def __init__(self, path):
        self.path = path
        self.data = {}
    
    def load(self):
        with open(self.path, "r") as f:
            self.data = json.load(f)
            # get last_index
            self.last_index = self.data["last_index"]
        return self.last_index

    def save(self, current_index):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)
            # save last_index variable
            self.data["last_index"] = current_index
            # set saved_at variable to current time and date
            self.data["saved_at"] = date.today().strftime("%d/%m/%Y %H:%M:%S")
