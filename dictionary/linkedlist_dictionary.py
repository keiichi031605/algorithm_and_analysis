from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = ListNode(None)
        self.length = 0

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for wf_object in words_frequencies:
            # 1. create a new ListNode
            new_node = ListNode(wf_object)
            if not self.head:
                self.head = new_node
            else:
                # 2. make next of new ListNode as head
                new_node.next = self.head
                # 3. move the head to point to new ListNode
                self.head = new_node
            self.length += 1

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        current = self.head
        for i in range(self.length):
            if current.word_frequency.word == word:
                return current.word_frequency.frequency

            current = current.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        word_validation = True
        current = self.head
        # 1. loop through and check if the word already exists or not
        for i in range(self.length):
            if current.word_frequency.word == word_frequency.word:
                word_validation = False
            current = current.next
        # 2. if the word does not exist, create a new node
        if word_validation:
            new_node = ListNode(word_frequency)
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1

        return word_validation

    def delete_word(self, word: str) -> bool:
        """ 
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # check if linked list has value in case
        if self.length  == 0:
            return False

        current = self.head
        previous = None
        # delete the node if the word is the head node
        if current.word_frequency.word == word:
            self.head = current.next
            self.length -= 1
            return True

        previous = current
        current = current.next
        # delete the node by scanning through list
        while current.word_frequency:
            if current.word_frequency.word == word:
                previous.next = current.next
                current = None
                self.length -= 1
                return True
            previous = current
            current = current.next

        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # check if linked list has value in case
        if self.length  == 0:
            return []

        frequent_words = []
        current = self.head
        # 1. loop through and check if the word already exists or not
        for i in range(self.length):
            if word[0] == current.word_frequency.word[0] and word in current.word_frequency.word:
                frequent_words.append(current.word_frequency)
            current = current.next
        frequent_words.sort(key=lambda x: x.frequency, reverse=True)

        most_frequent_words = []
        for frequent_word in frequent_words[:3]:
            most_frequent_words.append(frequent_word)

        return most_frequent_words
