from typing import List, Tuple


class dataBase:
    def __init__(self):
        # Creation of the database
        # Should load all Word - Popularity combos into a hash structure
        print("\033[91mWARNING:\033[00m  Loading Data Into Tree Not Yet Implemented.")
        
    def getWords(self, n=2) -> List[str]:
        # return N random words from the dataset
        # Note, we may also want to try storing the words(without their matching keys) as an array for O(1) access of any random element
        print("\033[91mWARNING:\033[00m  getWords not yet implemented.")
        return ["apple","bannana"]
    
    def getMostPopular(self, words) -> Tuple[str, List[int]]:
        # return the most popular word in the form of a string
        # as well as a list of each words score
        print("\033[91mWARNING:\033[00m  getMostPopular not yet implemented.")
        return "apple", [0,1]