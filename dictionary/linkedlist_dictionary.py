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

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for wf_object in words_frequencies:
            # 1. create a new Node
            new_node = ListNode(wf_object)
            # 2. make next of new ListNode as head
            new_node.next = self.head
            # 3. move the head to point to new ListNode
            self.head = new_node
        
        # print(self.head.word_frequency.word)
        # print(self.head.next.word_frequency.word)
        # print(self.head.next.next.word_frequency.word)
    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # 1. initialize current to head
        current = self.head
        # 2. define return value
        frequency = 0
        # 3. loop till current not equal to None
        while current != None:
            if current.word_frequency and current.word_frequency.word == word:
                frequency = current.word_frequency.frequency
            current = current.next
        return frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        word_validation = True
        # 1. initialize current to head
        current = self.head

        while current != None:
            if current.word_frequency and current.word_frequency.word == word_frequency.word:
                word_validation = False
            current = current.next
        # add it here
        if word_validation:
            # 1. create a new Node
            new_node = ListNode(word_frequency)
            # 2. make next of new ListNode as head
            new_node.next = self.head
            # 3. move the head to point to new ListNode
            self.head = new_node

        return word_validation

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        word_validation = False

        current = self.head
        while current != None:
            print(current.word_frequency.word)
            if current.word_frequency and current.word_frequency.word == word:
                word_validation = True
            current = current.next

            prev = current
            current = current.next
        # current = self.head
        # rear = current.next
        # while rear:
        #     if rear.value == value:
        #         break
        #     current = rear
        #     rear = rear.next
        # if not rear:
        #     print("[*] Data not found")
        #     return
        # current.next = rear.next
        # rear = None

        return word_validation
        # TO BE IMPLEMENTED
        # return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        return []



