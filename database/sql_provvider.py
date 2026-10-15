from pathlib import Path


class SqlProvider:
    def __init__(self, file_path):
        self.scripts = {}
        for file in Path(file_path).glob('*.sql'):
            self.scripts[file.name] = file.read_text(encoding='utf-8')

    def get(self, file):
        return self.scripts[file]
