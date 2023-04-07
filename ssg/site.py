from pathlib import Path
import os


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.makedir(parents=True, exist_ok=True)

    def build(self):
        for path in self.source.rglob("*"):
            if os.path.isdir(path):
                self.create_dir(path)


