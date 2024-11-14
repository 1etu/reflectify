import os
from config.config import DATA_DIR

class FileHandler:
    @staticmethod
    def write_list_to_file(filename, data):
        filepath = os.path.join(DATA_DIR, filename)
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write('\n'.join(data))

    @staticmethod
    def read_list_from_file(filename):
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]