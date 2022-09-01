from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import string
# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = TrieNode()
        # self.root.children["c"] = TrieNode("c", None, False)
        # self.root.children["u"] = TrieNode("b", None, False)

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for wf_object in words_frequencies:
            node = self.root
            for char in wf_object.word:
                found_in_child = False
                for child in node.children:
                    if char == child:
                        # print(node.children[char])
                        node = node.children[char] #set its value TrieNode
                        found_in_child = True
                        break
                if not found_in_child:
                    # print(char)
                    new_node = TrieNode(char, None, False)
                    node.children[char] = new_node
                    node = new_node

            node.frequency = wf_object.frequency
            node.is_last = True
        # print(self.root.children["c"].children)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        node = self.root
        # return 0 if root node has no children
        if not node.children:
            return 0

        for char in word:
            char_not_found = True
            # loop through node.children to search if each char exists
            for child in node.children:
                if char == child:
                    char_not_found = False
                    node = node.children[char] #set its value TrieNode to node
                    break

            # return 0 anyway when not found a char.
            if char_not_found:
                return 0

        return node.frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        word_validation = False
        node = self.root
        for char in word_frequency.word:
            found_in_child = False
            for child in node.children:
                if char == child:
                    # print(node.children[char])
                    node = node.children[char] #set its value TrieNode
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char, None, False)
                node.children[char] = new_node
                node = new_node
                word_validation = True
        if word_validation:
            node.frequency = word_frequency.frequency
            node.is_last = True
        
        # print(self.root.children["b"].children["o"].children["o"].children["k"])
        # print(word_validation)
        return word_validation

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        return []
