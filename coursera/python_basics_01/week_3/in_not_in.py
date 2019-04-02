
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

#Note that a string is a substring of itself, and the empty string is a substring of any other string. (Also note that computer scientists like to think about these edge cases quite carefully!)
print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')

# The not in operator returns the logical opposite result of in.
print('x' not in 'apple')

# We can also use the in and not in operators on lists!
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])

# However, remember how you were able to check to see if an “a” was in “apple”? Let’s try that again to see if there’s an “a” somewhere in the following list.
print("a" in ["apple", "absolutely", "application", "nope"])
