x = input("Enter a number: ")

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")


# Write code to assign the string "You can apply to SI!" to output if the string "SI 106" is in the list courses. If it is not in courses, assign the value "Take SI 106!" to the variable output.

courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if ("SI 106" in courses):
    output = "You can apply to SI!"
else:
    output = "Take SI 106!"
print(output)


#Create a variable, b, and assign it the value of 15. Then, write code to see if the value b is greater than that of a. If it is, a’s value should be multiplied by 2. If the value of b is less than or equal to a, nothing should happen. Finally, create variable c and assign it the value of the sum of a and b.

a = 20
b =15

if (b > a):
    a = a * 2
else:
    print("'B's value was less then or equal to 'A'")

c = (a + b)

# This example shows how you dont need the else statement

x = 10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")
