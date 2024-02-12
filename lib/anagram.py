# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words):
        returnArray = []
        for arrayword in words:
           if (sorted([letter for letter in self.word]) == sorted([letter for letter in arrayword])):
               returnArray.append(arrayword)
    
        return returnArray
