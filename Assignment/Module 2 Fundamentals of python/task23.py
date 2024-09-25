#  What are negative indexes and why are they used? 

"""
Negative indexes in Python allow you to access elements from the end of a sequence, such as a list or a string, rather than from the beginning. 
This can be particularly useful when you want to quickly access elements at the end without knowing the exact length of the sequence.

Here's how negative indexing works:

The index -1 refers to the last element.
The index -2 refers to the second last element, and so on.
For example, 
consider the list my_list = [10, 20, 30, 40, 50]:
my_list[-1] returns 50 (the last element).
my_list[-2] returns 40 (the second last element).

# Slicing using negative indexing
print(my_list[-3:])  # Output: [30, 40, 50]
 
Negative indexing provides a Convenient and intuitive way to work with sequences from the end.
"""
