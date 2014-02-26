class Storage(object):
    def __init__(self):
        self.storage = []

    def put(self, node):
        self.storage.append(node)

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)


class Stack(Storage):
    def get(self):
        return self.storage.pop()


class Queue(Storage):
    def get(self):
        return self.storage.pop(0)
