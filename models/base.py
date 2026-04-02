import os
import json


class Base:
    data_file = None

    def to_dict(self):
        raise NotImplementedError

    @classmethod
    def save_all(cls, objects):
        os.makedirs("data", exist_ok=True)
        with open(cls.data_file, "w") as f:
            json.dump([obj.to_dict() for obj in objects], f, indent=4)

    @classmethod
    def load_all(cls):
        if not os.path.exists(cls.data_file):
            return []
        with open(cls.data_file, "r") as f:
            content = f.read()
            if not content.strip():
                return []
            return json.loads(content)