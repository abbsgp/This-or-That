# from https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
class HTable(object):
    def __init__(self, length=100):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array)/2

    def double(self):
        ht2 = HTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])
        self.array = ht2.array

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)
