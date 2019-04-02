# #This exercise demonstrates how you can use the '[:]' brakets to select characters
# in a string and even strings from a list
#


singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

# # The slice operator [n:m] returns the part of the string starting with the character
# at index n and go up to but not including the character at index m. Or with normal
# counting from 1, this is the (n+1)st character up to and including the mth character.
# # If you omit the first index (before the colon), the slice starts at the beginning
# of the string. If you omit the second index, the slice goes to the end of the string.

fruit = "banana"
print(fruit[:3])
print(fruit[3:])

# The slice operation we saw with strings also work on lists. Remember that the
# first index is the starting point for the slice and the second number is one
# index past the end of the slice (up to but not including that element).
# Recall also that if you omit the first index (before the colon), the slice
# starts at the beginning of the sequence. If you omit the second index, the
# slice goes to the end of the sequence.

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])
