

from datetime import date
import toml


class Save:
    def __init__(self, path):
        self.path = path
        self.data = {}
    
    def load(self):
        # get last_index and saved_at variables, from toml file *.rei
        with open(self.path, "r") as f:
            self.data = toml.load(f)
            # get last_index variable
            self.last_index = self.data["last_index"]
            # get saved_at variable
            self.saved_at = self.data["saved_at"]

    def save(self, current_index):
        # save last_index and saved_at variables, to toml file *.rei
        with open(self.path, "w") as f:
            self.data = {
                "last_index": current_index,
                "saved_at": str(date.today())
            }
            toml.dump(self.data, f)


    def get_time(self):
        return self.data["saved_at"]
