import random
from typing import List, Tuple
from hash import HTable


class dataBase:
    def __init__(self, autoPopulate=True):
        self.myHash = HTable()
        self.keys = list()
        if autoPopulate:
            self.populate()

    def populate(self):
        with open("database.csv", "r") as file:
            for line in file:
                kvpair = line.split(",")
                self.myHash.add(kvpair[0], int(kvpair[1]))
                self.keys.append(kvpair[0])

    def insert(self, key, value):
        self.myHash.add(key, value)
        self.keys.append(key)

    def getWords(self, n=2) -> List[str]:
        return random.sample(self.keys, n)

    def getMostPopular(self, words) -> Tuple[str, List[int]]:
        bestWord = words[0]
        bestValue = 0
        allvalues = list()
        for word in words:
            val = self.myHash.get(word)
            if val > bestValue:
                bestValue = val
                bestWord = word
            allvalues.append(val)
        return bestWord, allvalues
