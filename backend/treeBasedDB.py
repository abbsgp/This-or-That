from random import randint, randrange
import random
from typing import List, Tuple
from rbtree import RBtree


class dataBase:     
    def __init__(self, autoPopulate=True):
        # Creation of the database
        # Should load all Word - Popularity combos into the tree
        self.myTree = RBtree()
        self.keys = list()
        if autoPopulate: self.populate()
        #print("\033[91mWARNING:\033[00m  Loading Data Into Tree Not Yet Implemented.")
        
    def populate(self):
        with open("database.csv", "r") as file:
            for line in file:
                kvpair = line.split(",")
                self.myTree.insert(kvpair[0],int(kvpair[1]))
                self.keys.append(kvpair[0])
                
    def insert(self,key,value):
        self.myTree.insert(key,value)
        self.keys.append(key)
        
    def getWords(self, n=2) -> List[str]:
        # return N random words from the dataset
        # Note, we may also want to try storing the words(without their matching keys) as an array for O(1) access of any random element
        #print("\033[91mWARNING:\033[00m  getWords not yet implemented.")
        return random.sample(self.keys, n)
    
    def getMostPopular(self, words) -> Tuple[str, List[int]]:
        # return the most popular word in the form of a string
        # as well as a list of each words score
        bestWord = words[0]
        bestValue = 0
        allvalues = list()
        #print("\033[91mWARNING:\033[00m  getMostPopular not yet implemented.")
        for word in words:
            val = self.myTree.GetValue(word)
            if val > bestValue:
                bestValue = val
                bestWord = word
            allvalues.append(val)
        return bestWord,allvalues