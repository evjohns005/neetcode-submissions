class FileSystem:

    def __init__(self):
        self.file_path = {}

    def createPath(self, path: str, value: int) -> bool:
        if len(path) < 2:
            return False
        if path in self.file_path:
            return False

        parent = path.rsplit("/", 1)[0]
        if parent and parent not in self.file_path:
            return False

        self.file_path[path] = value
        return True

    def get(self, path: str) -> int:
        return self.file_path.get(path, - 1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
