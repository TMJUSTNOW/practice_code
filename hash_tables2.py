class Dummy(object):
    pass


class HashTable(object):
    dummy = Dummy()

    def __init__(self):
        self.size = 8
        self._storage = [self.dummy for _ in range(self.size)]

    def __repr__(self):
        return str(self._storage)

    def __setitem__(self, key, value):
        hashed_key = hash(key)
        index = hashed_key % self.size
        item = (hashed_key, key, value)

        if self._storage[index] is self.dummy:
            self._storage[index] = LinkedList(item)
        else:
            self._storage[index].append(item)

    def __getitem__(self, key):
        hashed_key = hash(key)
        index = hashed_key % self.size
        value = self._storage[index].value[2]
        return value


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, value):
        self.first = Node(value)
        self.last = self.first

    def __iter__(self):
        def f():
            item = self.first
            while item is not None:
                yield item.value
                item = item.next

        return f

    def append(self, value):
        self.last.next = Node(value)
        self.last = self.last.next

    def remove(self, value):
        """Removes first appearance of value in linked list."""
        if self.first.value == value:
            self.first = self.first.next
            return

        item = self.first.next
        previtem = self.first

        while item is not None:
            if item.value == value:
                if item.next is None:
                    self.last = previtem
                previtem.next = item.next

            previtem = item
            item = item.next

    def __repr__(self):
        item = self.first
        reps = []

        while item is not None:
            reps.append(repr(item))
            item = item.next

        return "[{}]".format(", ".join(reps))
