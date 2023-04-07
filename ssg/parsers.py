from typing import List
from pathlib import Path
import shutil


class Parser:
    def __init__(self):
        self.extensions: List[str] = []

    def valid_extensions(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, mode="r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, mode="w") as file:
            file.write(content)


def copy(path, source, dest):
    shutil.copy(path, source / dest)


class ResourceParser(Parser):
    def __init__(self):
        self.extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        copy(path, source, dest)
