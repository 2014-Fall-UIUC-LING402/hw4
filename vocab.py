###############################################################################
# Instructions:
################
#
# Implement the following vocabulary class (10 points).
#
# When you are done, your code must:
#
# 1. Have a constructor (__init__) that properly initializes its member variables
#   * Correctly initialize a member variable called int_to_word as an empty list (1 point)
#   * Correctly initialize a member variable called word_to_int as an empty dictionary (1 point)
#
#
# 2. Have a get_index method that accepts a string as a parameter:
#   * If that string has not been seen before, 
#     append the string to the end of the int_to_word list (1 point),
#     and add a new entry to the word_to_int dictionary,
#     such that the string is the key and the index of that string
#     (in the int_to_word list) is the value associated with that key (1 point)
#     Return the index of the string (1 point)
#   * If that string has been seen before, return its index (1 point)
#
#   This method must return an int.
#
#
# 3. Have an get_word method that accepts an integer as a parameter:
#   * If a string exists at the specified index
#      (in the int_to_word list), return the string at that index (1 point)
#   * Otherwise, return the Python built-in constant None (1 point)
#
#
# 4. Have a size method:
#    * Returns the number of items stored in the list (1 point)
#
#
# 5. Have a contains method that accepts a string:
#    * Returns True if the string is stored in the vocabulary, and False otherwise (1 point)
#
#
# Optional extra credit:
#
# 6. Modify the constructor: (3 points)
#    * If the constructor is called without an argument, the behavior should be as it was in instruction 1 above
#    * If the constructor is called with a Vocabulary object as an argument, 
#      initialize the member variables with the data from the other object
# 
###############################################################################
###############################################################################


class Vocabulary:

    def __init__(self, other=None):
        pass

    def get_index(self, word):
        pass

    def get_word(self, index):
        pass

    def size(self):
        pass

    def contains(self, word):
        pass

