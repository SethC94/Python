# Coursera - Python Basics Certification - Week 4

## Sequence Mutation and Accumulation Patterns

### Objectives:
* Simulate execution of list assignment, appending, and deletion
* Read and write code that uses the string and list methods
* Identify the type of value returned by each of the methods
* Select the appropriate string or list method given a problem
* Interpret code as implementing an accumulator pattern
* Write code to implement accumulator patterns
* Recognize when aliasing may lead to confusing results
* Write your own reference diagram
* Choose good variable names

### 9.2. Mutability
Example: [mutability.py](https://github.com/SethC94/Python/tree/master/coursera/python_basics_01/week_4/mutability.py)

### 9.2.2. Strings are Immutable


### 9.2.3. Tuples are Immutable

### 9.7. Mutating Methods

There are mutating methods and non-mutating methods. Mutating methods change the object after the method has been used

Notes:
append - adds the argument passed to it to the end of the list

insert - takes in 2 arguments, the index to instert at, and the argument to insert

### 9.8. Append versus Concatenate

Appending to a list just adds to an existing list. Concatenation creates a new list entirely.

Identification tags are unique to each Python object

concatenation writes an assignment statement that uses the accumulator pattern

**You cannot concatenate a list with an integer**

### Non-mutating Methods on Strings

upper:	Returns a string in all uppercase

lower:	Returns a string in all lowercase

count:	Returns the number of occurrences of item

index:	Returns the leftmost index where the substring item is found and causes a
 runtime error if item is not found

strip:	Returns a string with the leading and trailing whitespace removed

replace:	Replaces all occurrences of old substring with new

### 9.10. The Accumulator Pattern with Lists

### 9.12. 👩‍💻 Accumulator Pattern Strategies

**Q: What is the accumulation pattern?**

A: The pattern of iterating the updating of a variable

__Note:__ _Each time we iterate through a list python does not reevaluate the iterator variable._
