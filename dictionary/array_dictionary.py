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
        self.array_dictionary = []

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # 1. assign sorted words_frequencies to self.array_dictionary
        self.array_dictionary = sorted(words_frequencies, key=lambda x: x.word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # 1. loop through array_dictionary to search
        for wf_object in self.array_dictionary:
            if word == wf_object.word:
                return wf_object.frequency

        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # 1. loop through array_dictionary to check word already exists
        word_validation = True
        for wf_object in self.array_dictionary:
            if word_frequency.word == wf_object.word:
                word_validation = False
        # 2. if word doesn't exist, add the @param(word_frequency) to the array_dictionary and sort it.
        if word_validation:
            self.array_dictionary.append((word_frequency))
            self.array_dictionary.sort(key=lambda x: x.word)

        return word_validation

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        # """
        # 1. loop through the array_dictionary to find the position of 'word' in the list with idx var
        word_validation = False
        count = -1
        idx = None
        for wf_object in self.array_dictionary:
            count += 1
            if word == wf_object.word:
                word_validation = True
                idx = count
        # 2. if 'word' doesn't exist, remove it from the array_dictionary by pop() with index
        if idx:
            self.array_dictionary.pop(idx)

        return word_validation

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        frequent_words = []
        for wf_object in self.array_dictionary:
            if prefix_word[0] == wf_object.word[0] and prefix_word in wf_object.word:
                frequent_words.append(wf_object)
        frequent_words.sort(key=lambda x: x.frequency, reverse=True)

        most_frequent_words = []
        for frequent_word in frequent_words[:3]:
            most_frequent_words.append(frequent_word)

        return most_frequent_words