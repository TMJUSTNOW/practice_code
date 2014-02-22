class Dictionary(object):
    def __init__(self):
        self.storage = {}

    def add_key_value_pair(self, key, value):
        self.storage[key] = value

    def get_value(self, key):
        return self.storage[key]

    def remove_key(self, key):
        self.storage.pop(key)

    def __str__(self):
        return self.storage.__str__()

    def __repr__(self):
        return self.__str__()


class AssociatedList(object):
    def __init__(self):
        self.keys = []
        self.values = []

    def add_key_value_pair(self, key, value):
        if key in self.keys:
            idx = self.keys.index(key)
            self.values[idx] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get_value(self, key):
        idx = self.keys.index(key)
        return self.values[idx]

    def remove_key(self, key):
        print(key)
        print(self.keys)
        idx = self.keys.index(key)
        self.keys.remove(key)
        del self.values[idx]

    def __str__(self):
        output = '{'
        for idx in range(len(self.keys)):
            if idx != 0:
                output += ', '
            output += "'{0}': '{1}'".format(self.keys[idx], self.values[idx])
        output += '}'
        return output

    def __repr__(self):
        return self.__str__()


example = Dictionary()
example.add_key_value_pair('key1', 'value1')
example.add_key_value_pair('key2', 'value2')
print example
example.remove_key('key2')
print example

example2 = AssociatedList()
example2.add_key_value_pair('key1', 'value1')
example2.add_key_value_pair('key2', 'value2')
print example2
example2.remove_key('key2')
example2.add_key_value_pair('key1', 'value1better')
print example2
