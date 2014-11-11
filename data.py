###############################################################################
# Instructions:
################
#
# Implement the following tip calculator class (10 points).
#
# When you are done, your code must:
#
# 1. Have a constructor (__init__) that properly stores the data as a list:
#   * Correctly process parameter when bill is a list  (1 point)
#   * Correctly process parameter when bill is a set (1 point)
#   * Correctly process parameter when bill is a tuple (1 point)
#
#   The constructor must initialize a member variable called data that stores the provided data.
#
# 2. Have a value method:
#   * Correctly returns the data (as a list) (1 point)
#
# 2. Have a get_item method:
#   * Correctly gets the item in data at the specified index (1 point)
#
# 3. Have a get_items method:
#   * Correctly gets a list containing the items at the specified range, using list slicing (1 point)
#
# 4. Have a get_sorted_items method:
#   * Correctly returns a new sorted list containing all elements in data (1 points) 
#
# 5. Have a size method:
#   * Correctly returns the number of elements in the list (as an integer) (1 point)
#
# 6. Have a reverse method:
#   * Correctly returns a new list containing all elements in data (but in reverse order) (1 point)
#
# 7. Have a count method:
#   * Correctly returns (as an integer) the number of times the specified element is in the data (1 point)
#
# 
# Optional extra credit:
#
# 8. Have an apply_function method:
#   * Correctly returns a new list created by applying the provided function to each data element, using a list comprehension (3 points)
#
#
# IMPORTANT NOTE: None of the methods (other than the constructor) of your class
#                 should modify the data stored in the class  
# 
###############################################################################
###############################################################################

class Data:

   def __init__(self, data):
      pass

   def value(self):
      pass

   def get_item(self, index):
      pass

   def get_items(self, inclusive_starting_index, exclusive_ending_index):
      pass

   def get_sorted_items(self):
      pass

   def size(self):
      pass

   def reverse(self):
      pass

   def count(self, element):
      pass

# The following method is extra credit:

   def apply_function(self, function):
      pass

