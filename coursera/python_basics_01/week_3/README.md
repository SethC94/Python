# Coursera - Python Basics Certification - Week 3

## Topic: Booleans Expressions

### 8.1.1. Learning Goals
* To understand boolean expressions and logical operators
* To understand conditional execution
* To be able to write a boolean function
* To know when to use binary, unary, chained and nested conditional statements

### 8.1.2. Objectives
* To properly evaluate a (compound) boolean expression
* To use parenthesis to properly demonstrate operator precedence
* To use conditional statements to properly branch code

In the [selection_conditional_statement.py](https://github.com/SethC94/Python/tree/master/coursera/python_basics_01/week_3/selection_conditional_statement.py), we first set amy’s pen color to be “Pink” and then move her forward. Next we want one of two actions to happen, either amy should move right and then forward, or left and then forward. The direction that we want her to go in depends on her pen color. If her pen color is set to pink - which is determined by writing amy.pencolor() == "Pink" which checks to see if the value returned by amy.pencolor() is the equivalent to the string “Pink” - then we should have her move right and forward. Else (or otherwise) she should move left and forward. Both things can’t happen though. She can’t move right, forward and left, forward. We then do the same thing for kenji, though in this case, we didn’t change kenji’s pen color.

It might seem a bit odd to add the conditionals in this example. Wouldn’t we already know that we set up amy and kenji’s colors, so why would we need a conditional? While it’s true that this isn’t the best place to use a conditional, we can combine conditional statements with for loops to make something pretty cool!

#### 8.2. Boolean Values and Boolean Expressions

The Python type for storing true and false values is called **bool**, named after the British mathematician, George Boole. George Boole created Boolean Algebra, which is the basis of all modern computer arithmetic.

There are only two boolean values. They are _True_ and _False_. **Capitalization is important**, since true and false are not boolean values (remember Python is case sensitive) Look at [boolean_types.py](https://github.com/SethC94/Python/tree/master/coursera/python_basics_01/week_3/boolean_types.py) for examples of this

**_Note:_
Boolean values are not strings!**

It is extremely important to realize that True and False are not strings. They are not surrounded by quotes. They are the only two values in the data type bool. Take a close look at the types shown below.


A **boolean expression** is an expression that evaluates to a boolean value. The equality operator, `==`, compares two values and produces a boolean value related to
whether the two values are equal to one another.

Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). Remember that = is an assignment operator and == is a comparison operator. Also, there is no such thing as =< or =>.
### Comparison Operators:
`x != y`              `# x is not equal to y`

`x > y`               `# x is greater than y`

`x < y`               `# x is less than y`

`x >= y`              `# x is greater than or equal to y`

`x <= y`              `# x is less than or equal to y`

Note too that an equality test is symmetric, but assignment is not. For example, if `a == 7` then `7 == a`. But in Python, the statement `a = 7` is legal and `7 = a` is not. (Can you explain why?)

#### 8.3. Logical operators

There are three logical operators: `and`, `or`, and `not`. The semantics (meaning) of these operators is similar to their meaning in English. For example, `x > 0` and `x < 10` is true only if x is greater than 0 and at the same time, x is less than 10. How would you describe this in words? You would say that x is between 0 and 10, not including the endpoints.

`n % 2 == 0` or `n % 3 == 0` is true if either of the conditions is true, that is, if the number is divisible by 2 or divisible by 3. In this case, one, or the other, or both of the parts has to be true for the result to be true.

Finally, the not operator negates a boolean expression, so not  `x > y` is true if `x > y` is false, that is, if x is less than or equal to y.

##### _Common Mistake!_
There is a very common mistake that occurs when programmers try to write boolean expressions. For example, what if we have a variable number and we want to check to see if its value is 5, 6, or 7? In words we might say: “number equal to 5 or 6 or 7”. However, if we translate this into Python, `number == 5 or 6 or 7`, it will not be correct. The or operator must join the results of three equality checks. The correct way to write this is: `number == 5 or number == 6 or number == 7`

This may seem like a lot of typing but it is absolutely necessary. You cannot take a shortcut.

Well, actually, you can take a shortcut but not that way. Later in this chapter you’ll learn about the in operator for strings and sequences: you could write number in [5, 6, 7].

#### 8.4. The in and not in operators

If you look at [in_not_in.py](https://github.com/SethC94/Python/tree/master/coursera/python_basics_01/week_3/in_not_in.py), we can tell that a is in the word apple, and absolutely, and application. For some reason though, the Python interpreter returns False. Why is that? When we use the in and not in operators on lists, Python checks to see if the item on the left side of the expression is equivalent to an element in the item on the right side of the expression. In this case, Python is checking whether or not an element of the list is the string “a” - nothing more or less than that.

#### 8.5. Precedence of Operators

Arithmetic operators take precedence over logical operators. Python will always evaluate the arithmetic operators first (*** is highest, then multiplication/division, then addition/subtraction). Next comes the relational operators. Finally, the logical operators are done last. This means that the expression x*5 >= 10 and y-6 <= 20 will be evaluated so as to first perform the arithmetic and then check the relationships. The and will be done last. Many programmers might place parentheses around the two relational expressions, (x*5 >= 10) and (y-6 <= 20). It is not necessary to do so, but causes no harm and may make it easier for people to read and understand the code.

The following table summarizes the operator precedence from highest to lowest. A complete table for the entire language can be found in the [Python Documentation](http://docs.python.org/py3k/reference/expressions.html#expression-lists).
