import os
import json
import csv


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

    @classmethod
    def save_all_dicts(cls, dicts):
        os.makedirs("data", exist_ok=True)
        with open(cls.data_file, "w") as f:
            json.dump(dicts, f, indent=4)

    @staticmethod
    def export_csv(filename, headers, rows):
        os.makedirs("rapports", exist_ok=True)
        filepath = os.path.join("rapports", filename)
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(row)
        return filepath
