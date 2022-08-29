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
            front = self.head
            rear = front.next
            while rear:
                front = rear
                rear = rear.next
            list_node = ListNode(wf_object)
            list_node.next = rear
            front.next = list_node
        
        # print(self.head.word_frequency)
        # print(self.head.next.word_frequency.word)
        # print(self.head.next.next.word_frequency.word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # # Initialize current to head
        # current = self.head
 
        # # Loop till current not equal to None
        # while current != None:
        #     if current.data == x:
 
        #         # Data found
        #         return True
        
        #     current = current.next
         
        # # Data Not found
        # return False

        # front = self.head
        # rear = front.next
        # while rear:
        #     print(rear.word_frequency)
        #     if rear.word_frequency == word:
        #         break
        #     front = rear
        #     rear = rear.next
        # if not rear:
        #     print("[*] Data not found")
        #     return
        # front.next = rear.next
        # rear = None
        # TO BE IMPLEMENTED
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        # TO BE IMPLEMENTED
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        return []



