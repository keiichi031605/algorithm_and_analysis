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
                        node = node.children[char] #set its value TrieNode
                        found_in_child = True
                        break
                if not found_in_child:
                    new_node = TrieNode(char, None, False)
                    node.children[char] = new_node
                    node = new_node

            node.frequency = wf_object.frequency
            node.is_last = True

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
                    node = node.children[char] #set its value TrieNode
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char, None, False)
                node.children[char] = new_node
                node = new_node
                word_validation = True
        # if the last character is not found
        if word_validation:
            node.frequency = word_frequency.frequency
            node.is_last = True
        # if last character is found but it's not the last character yet, add its frequency
        if found_in_child and not node.is_last:
            node.frequency = word_frequency.frequency
            node.is_last = True
            word_validation = True

        return word_validation

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # validate if the word is deletable
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if char == child:
                    node = node.children[char] #set its value TrieNode
                    found_in_child = True
                    break
            if not found_in_child:
                return False
        # if last node has children, just update its statuses, otherwise execute recursive _delete algorithm
        if len(node.children) > 0:
            node.is_last = False
            node.frequency = None
        else:
            self._delete(word, 0, self.root)

        return True

    def _delete(self, word, i, current):
        deletable = False
        if i == len(word):
            if not current.is_last:
                return False
            return len(current.children) == 0
        char = word[i]
        if char not in current.children:
            return False
        next_node = current.children[char]
        should_delete_ref = self._delete(word, i+1, next_node)
        # execute deleting child node if self._delete returns true
        if should_delete_ref:
            del current.children[char]
            deletable = True

        if current.is_last:
            return False
        if len(current.children) > 0:
            return False

        return deletable

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        self.frequent_words = []
        self.depth_first_search(node, word[:-1])

        self.frequent_words.sort(key=lambda x: x[1], reverse=True)
        most_frequent_words = []
        for frequent_word in self.frequent_words[:3]:
            most_frequent_words.append(WordFrequency(frequent_word[0], frequent_word[1]))

        return most_frequent_words

    # additional my own function to do depth-first-search to get word by prefix
    def depth_first_search(self, node, pre):
        if node.is_last:
            word_tuple = (pre + node.letter, node.frequency)
            self.frequent_words.append(word_tuple)

        for child in node.children.values():
            self.depth_first_search(child, pre + node.letter)
