from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # pass
        self.array_dictionary = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # 1. set empty dictionary and build dictionary with for loop
        wf_dictionary= {}
        for wf in words_frequencies:
            wf_dictionary[wf.word] = wf.frequency
        # 2. assign crated dictionary to self.array_dictionary
        self.array_dictionary = wf_dictionary

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # 1. loop through array_dictionary to search word if it's contained
        count = 0
        for key, value in self.array_dictionary.items():
            if word in key:
                count += 1

        return count    

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # 1. loop through array_dictionary to check word already exists
        word_validation = True
        for key, value in self.array_dictionary.items():
            if word_frequency.word == key:
                word_validation = False                
        # 2. if word doesn't exist, add the word and frequency to the array_dictionary
        if word_validation:
            self.array_dictionary[word_frequency.word] = word_frequency.frequency

        return word_validation

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED

        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        return []
