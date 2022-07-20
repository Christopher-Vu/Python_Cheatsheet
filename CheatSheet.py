# IMPORTANT NOTE: This is a copy of my original cheatsheet document, the only different being I used pycharm's
# autoformat feature to format it. My formatting for the original was definetly a lot more messy, so this is
# the document that I will be sharing with others if they want it (b/c it's probably easier to read)

# PYCHARM AUTO-FORMAT: Ctrl + Alt + L
# PYCHARM AUTO-FORMAT SETTINGS: Ctrl + Alt + Shift + L

# Guide to formatting
# <GENERAL INFORMATIONAL GROUPS> (broader topics/topics without subsets); encased in <> & all caps
#:Informational Subsets: (smaller topics/pieces of a bigger topic); encased in :: and capitalized like book titles
# ---[SUBSET SECTIONS]--- (for informational subsets that are too broad); encased in ---[]--- and all caps
# IGNORE THIS FUNCTION
import math

skip_input = ""


def q():
    global skip_input
    skip_input = input("Skip all input sections while running (y/n)? ")
    if skip_input != "y" and skip_input != "n":
        print("please enter either y or n.")
        q()


q()

# <PRINT AND VARIABLES>
# use the print() command to print something onto the console. Use vairable = "" to make a variable for a string
import sys

print("\n---------------\n<PRINT AND VARIABLES>")
character_name = "John"
character_age = 25
print("There once was a man named " + character_name + ", ")
# In order to display an integer as a string, you must put it in str() to convert it to a string
print("he was " + str(character_age) + " years old.")
print("He liked the name " + character_name)
print("But he didn't like being " + str(character_age) + " years old")

# <DATA TYPES AND COMMON METHODS>
print("\n\n\n\n---------------\n<DATA TYPES AND COMMON METHODS>")

#:Working With Strings/String Methods:
print("\n:Working With Strings/String Methods:")
phrase = "example"
print(phrase[4])  # strings 0 index, so it goes 0, 1, 2, 3, etc. So this will print the fifth letter no the fourth
print(phrase.index("p"))  # you can do this the other way around as well
print(phrase.replace("ple", " season"))  # you can also replace somethign with another thing

#:Formatting Strings:
print("\n:Formatting Strings:")
print("Hello {}".format(
    "Christopher"))  # The format method interpolates premade strings. This will return 'Hello Christopher'
print("{} {} {}".format("Hi ", "hello ",
                        "how Are you"))  # This will return 'hi hello how are you' (note that {} is inside the "")
print("{0} {0} {1}".format("Hi ", "hello ",
                           "how Are you"))  # You can also change the order/recur; this will return 'Hi Hi hello'
print("{a} {b} {c}".format(a="a", b="b", c="c"))  # You can also return keyworded arguments; this will return 'a b c'
print("{0} {1} {last}".format("Hi ", "hello ", last="how Are you"))  # You can also mix keywords and positions
name = "Christopher"
print(f"Hi, my name is {name}")  # These are called F strings and only work in python 3.6+
from string import Template  # template is a simpler and often safer option

temp = Template("Hello, my name is $name!")
my_name = "Chris"
print(temp.substitute(name=my_name))  # good for user input
number = 9
square = eval("number * number")  # The eval method evaluates code that is passed into it
print(square)  # prints 81; the code still works even though it is all inside of a string

#:String/List Splicing:
print("\n:Splicing:")
# ---[LIST SPLICING]---
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[start:end:step]
print(nums[0:5])  # Does not include the end; will only print indexes 0-4
print(nums[1:-2])  # Remember negative values can be used to count from the end
print(nums[5:])  # If a number if left out, then it will continue to the end (in this statement, indexes 5-10)
print(nums[:5])  # Same other way around (ends list early)
print(nums[:-3])  # Same functionality w/ negatives
print(nums[0:9:2])  # The third value wil tem through the values (every 'step'th value)
print(nums[-1:-8:-1])  # Step works w/ negatives, but the range must be negative
print(nums[::-2])  # Works with negative steps too
print(nums[::-1])  # Goes through the list backwards and returns it in the opposite order
# IMPORTANT NOTE: All splicing syntax is the same for string, where each character has an index

#:Working With Numbers/Int Methods:
print("\n:Working With Numbers/Int Methods:")
print(abs(-5.23))  # prints absolute value
print(pow(4, 6))  # exponentiation
print(round(3.2))  # rounds a number
# if a number is a decimal, then do not convert to a string, convert to a float
num = "3.8945"
print(float(num) + 3.56)
# to go further, you must import the math function
import math as M  # you can import something as another name

print(M.sqrt(36))  # there are others, but that was just a demonstration
print(55 % 15)  # returns the remainder; 55/15 = 3 remainder 10 (returns 10)
print(55 // 15)  # Rounds down to the nearest whole number; 55/15 = 3 remainder 10 (returns 3)

#:Input:
if skip_input == "n":
    print("\n:Input:")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hi " + name + ", you are " + age + "years old.")
else:
    print("\n:INPUT SECTION SKIPPED:")

#:String and List Sclicing:
print("\n:String and List Slicing:")
print("wefhuhjioe")

# <BASIC DATA STRUCTURES AND LIST OPERATIONS>
print("\n\n\n\n---------------\n<BASIC DATA STRUCTURES AND LIST METHODS>")

#:Lists and List Methods:
print("\n:List and List Methods:")
print("\n\n\n\n---------------\n<LISTS, 2D LISTS, TUPLES, AND SETS>")
friendlist = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Jim"]  # you can also store booleans (true/false) or numbers
print(friendlist[2])  # once again, we zero index (0, 1, 2), and 2 will be "Jim", not "Karen"
print(friendlist[-1])  # you can also go backwards
print(friendlist[1:3])  # print a range of indexes
friendlist[1] = "Michael"  # alter list elements
print(friendlist[1])
numbers = [1, 2, 89, 3, 9, 45, 923]
friendlist.extend(numbers)  # extend with another list
print(friendlist)
friendlist.clear()  # clears list
friendlist = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Jim"]
print(
    " ".join(friendlist))  # Combines every element in the list; the first param is what to put in between the elements
print(friendlist.append("Creed"))  # add item to list
print(friendlist.insert(1, "Kelly"))  # Insert Item in a specific spot
print(friendlist.remove("Jim"))  # remove item
print(friendlist.pop())  # remove the frontmost item
print(friendlist.index("Oscar"))  # gives index of item
print(friendlist.count("Jim"))  # counts occurences of an item
friends2 = friendlist.copy()
print(friends2)
cat = ["fat", "orange", "loud"]  # This represents the descriptions of a cat
size, color, disposition = cat  # Instead of keywording each description individually, this (multiple assignment) will
# assign each variable in order of the list; size="fat", color="orange", and disposition="loud".

#:2D lists and Matrices (Matrix):
print("\n:2D Lists and Matrices (Matrix):")
twoDList = [
    [1, 2, 3, 4, 5],  # This is row one, with 3 indexes inside of it
    [6, 7, 8, 9],  # note that this can be typed as one line, the new lines are for ease of understanding
    [10, 11, 12],
]
print(twoDList[1][1])  # You enter the row and the column (0 index)
print(twoDList[0])  # Whole lists can also be accessed
Matrix = [  # Matrixes are 2d lists in which every list has the same amount of elements
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  # it is mostly a technical term as they function exactly the same as 2d lists in python

#:Tuples:
print("\n:Tuples:")
coords = (4, 5)
print(coords[0])
# tuples are like lists but not able to be modified; you cant say coords[0] = 5 or it will throw an error

#:Sets:
print("\n:Sets:")
s1 = {1, 2, 3, 4}  # sets are defined by curly brackets
s2 = set([])  # Can also be defined by the set() function; this is important because {} is recognized as a dictionary
print({1, 2, 1, 3, 2, 4})  # Sets remove all duplicates; this will print (1, 2, 3, 4)
# Sets cannot be indexed; set1[1] will throw an error because there is no order in a set
print(s2.add(1))  # adds 1 element to the set
print(s2.update([3, 4, 5, 6]))  # adds multiple elements to the set
print(s2)
print(s2.discard(3))  # removes an element from the set
print(s1 | s2)  # Union; combines the sets. Also written as: s1.union(s2)
print(s1 & s2)  # Intersection; only keeps values in both sets. Also written as: s1.intersection(s2)
print(s1 - s2)  # Difference; returns values unique to the first set. Also written as: s1.difference(s2)
print(s1 ^ s2)  # Symmetric Difference; values not common to both sets. Also written as: s1.symmetric_difference(s2)

#:#:Map, Filter, and Reduce:
print("\n:Map, Filter, and Reduce:")
# Map and filter functions require the list() function to encompass them so that they will return a list
# A traditional function can be used for any of these instead of lambda but lambda is shorter
# MAP: applies the same function to each element of a sequence
n = [4, 3, 2, 1]
print(list(map(lambda x: pow(x, 2), n)))  # map takes 2 parameters, 1) the function and 2) the list.
# Returns [16,9,4,1]
# FILTER: Filters items out of a sequence
n = [4, 3, 2, 1]
print(list(filter(lambda x: x > 2, n)))  # filter takes the same two parameters; 1) the condition and 2) the list
# Returns [4,3]
# REDUCE: Same operation to list items but uses the result of an operation as the first parameter of the next operation
import functools  # reduce comes from functools

n = [4, 3, 2, 1]
print(functools.reduce(lambda x, y: x * y, n))  # This will multiply each element and return one value (returns 24)

#:List/Set/Dictionary Comprehensions:
print("\n:List, Set and Dictionary Comprehensions:")
# List Comprehensions
# Basic format for list comprehensions is this;   new_list = [transform_sequence[filter]]
under_10 = [x for x in range(10)]  # will return a list of numbers 0-9; x is the element that is added to the list while
# 'for x in range 10' defines how many times it is done (like a for loop)
squares = [x ** 2 for x in under_10]  # You can alter the number before it is added to the list, and here a list is
# used instead of a range
even = [x for x in range(10) if x % 2 == 0]  # In this comprehension a filter is added; in this case an if statement
string = "I love 2 g0 to the store 7 times a w33k"
nums = [x for x in string if x.isnumeric()]  # This returns all numbers in the string
# Set Comprehensions
ExampleSet = {"abc", "def"}
print({element.upper() for element in ExampleSet})
# Dictionary Comprehensions
Christopher = {"name": "Christopher", "age": 14}
print({term: definition for term, definition in Christopher.items()})

#:Generators:
print("\n:Generators:")


# Generators are similar to lists but they output values one at a time and do not sotre them in memory
# This makes them much more efficient in terms of memory because values are handled one at a time
def square(nums):  # square function
    for num in nums:
        yield num * num  # yield keyword marks the generator


lst = square([1, 2, 3])
print(next(lst))  # the next() function calls the next value
print(next(lst))
print(next(lst))
gen_comp = (num * num for num in [1, 2, 3])  # Generators can also be written like list comprehensions; they are
# written the same way but with parenthesis instead of brackers
for num in gen_comp:
    print(num)  # For loops can also be used

#:Itertools:
# Usually to get elements from an itertools function, you would use a for loop
# Instead of using a for loop and taking up a ton of lines, I will sacrifice some readability by using a
# list comprehension; focus on the function, not the list comprehension
print("\n:Itertools:")
import itertools

shapes = ["oval", "triangle", "square"]
colors = ["green", "blue", "purple"]
TF = [True, False, True]
print([x for x in
       itertools.combinations(shapes, 2)])  # return returns all combinations of an iterable of a specified length
print([x for x in itertools.combinations_with_replacement(shapes, 2)])  # allows an element to repeat in 1 result
for num in itertools.count(10, 3):  # count returns evenly spaced numbers with a starting point (10+3n)
    print(num)
    if num > 20:
        break
itertools.cycle(shapes)  # cycles through a list endlessly (not printing it for obvious reasons)
print([element for element in itertools.chain(shapes, colors)])  # returns two iterables as one iterable
print([element for element in itertools.compress(shapes, TF)])  # filters one iterable w/ another; written
# as itertools.compress(iterable,filter)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
print([num for num in
       itertools.dropwhile(lambda x: x < 5, nums)])  # Filters out all elements while the predicate is true,
# then #returns all subsequent values regardless of the predicate; written as itertools.dropwhile(predicate, data)
print([num for num in itertools.takewhile(lambda x: x < 5, nums)])  # opposite of dropwhile; predicate must be true
print([num for num in
       itertools.filterfalse(lambda x: x < 5, nums)])  # Only returns values in which the predicate is false
print([element for element in itertools.islice(colors, 2)])  # returns the first x elements of an iterable
print([perm for perm in itertools.permutations(colors)])  # Prints all permutations of an iterable (all orders)
print([perm2 for perm2 in itertools.permutations(colors, 2)])  # You can also define how long each permutation is
print(
    [p for p in itertools.product(colors, shapes)])  # Returns the cartesian products of 2 iterables (1-1 combinations)
print([object for object in itertools.repeat("spam", 3)])  # repeats an object a certain number of times
starmapvalues = [(2, 3), (5, 2), (9, 1)]
print([num for num in itertools.starmap(lambda a, b: a + b, starmapvalues)])  # computes a function using arguments
# from the iterable; similar to map
print([pair for pair in itertools.zip_longest(colors, nums, fillvalue=None)])  # Pairs elements from the 2 lists and
# gives a fillvalue if they are uneven in length (ex: (None, 4)); continues until the longest iterable is exhausted


# <FUNCTIONS>

#:Basics:
print("\n\n\n\n---------------\n<FUNCTIONS>")
print("\n:Basics:")


def Hello(name, age):  # anything inside of the parenthesis is the parameters, and they can be used in the function
    print("Hello " + name + ", you are " + str(age) + " years old")


Hello("Mike", 23)  # the function takes the "hi" parameter into the function and excecutes the code
Hello("Bob", 14)

#:Return:
print("\n:Return:")


# the return statement will return a value in place of the function
def cube(num):
    return num * num * num


print(cube(5))  # you can print it
cube3 = cube(3)  # or set it as a value
print("the cube of 3 is " + str(cube(3)))

#:*Args and **Kwargs:
print("\n:*Args and **Kwargs:")


def person(name, *data):  # using a one star arg like this means that you can pass in multiple variables under the one
    # variable name
    print(name)
    print(data)


person("Michael", 28, "Boston", 5625334524)


def person2(name, **data):  # two star kwargs are keyworded variable arguments, where each argument can
    # have its own keyword
    print(name)
    print(data)
    for i, j in data.items():  # i for the name keyword, j for the item
        print(i, j)


person2("Jim", age=30, city="Scranton", number=5627541822)

#:Passing a List to a Function:
print("\n:Passing a List to a Function:")


def function2(listhere):
    even = 0
    odd = 0
    for i in listhere:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


numbers2 = [1, 6, 15, 28, 32, 39, 42, 48, 55, 61, 86]
even, odd = function2(numbers2)
print("even : {}, odd : {}".format(even, odd))

#:Global Keyword:
# variables in functions stay in functions; the variables will be different outside of the function shown here:
print("\n:Global Keyword:")
a = 10


def function():
    a = 15
    print("Within function: " + str(a))


function()
print("outside of function: " + str(a))
# If there is no declaration of value in the function, you can access the global var in the local function
a = 10


def function():
    print("Within function: " + str(a))


function()
print("outside of function: " + str(a))
# Using this global keyword, you can access local changes in a variable globally
a = 10


def function():
    global a
    a = 15
    print("Within function: " + str(a))


function()
print("outside of function: " + str(a))
# The globals variable will bring you a global variable
x = globals()['a']
print(str(x))

#:Recursion:
print("\n:Recursion:")


def greet():
    print("Hello")
    # greet() #This will recur this function over and over when called
    # It will stop at the recursion limit, and you can see the recursion limit with this function:


sys.getrecursionlimit()
# You can change the recursion limit with this function
sys.setrecursionlimit(2000)

#:Lambda Functions:
print("\n:Lambda Functions:")
# Lambda is a way to shorten simple liens of code so that you don't have to create a function for it
# It creates the possibility for one-liners, list sorting, and is used in filter/map/reduce
multiply = lambda n, m: n * m  # double is the name, parameters go before the colon, the return value goes after
print(multiply(5, 2))
greater = lambda x, y: x if x > y else y  # you can use if else statements  within a lambda function
names = ["Dwight", "Oscar", "Pam",
         "Michael"]  # lambda is also used as a key to sort to sort lists by a custom parameter
names.sort(key=lambda x: len(x))  # Here, lambda is used to sort the list by length; the parameter are the list objects
# and the return statement is the sorting parameter

#:Decorators:

print("\n:Decorators:")


# ---[WRAPPER FUNCTIONS/PREREQUISITE KNOWLEDGE]---

def func(string):
    def wrapper():  # Nested function; declares new 'wrapper' function when func is called
        print("Started")
        print(string)  # The function that is passed in is run
        print("Ended")

    return wrapper()  # when func() is run, wrapper() is run


print("With return value as wrapper():")
x = func("Hello")  # Notice that we have not printed the val of x yet; the code above is being run because func() was
# called, but the output value is not the value of x
print(f"x = {x}")  # within x, there is nothing


def func(string):  # Redefine the function w/ a change to the return value
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    return wrapper  # when func() is run, wrapper() is run


print("With return value as wrapper and no ():")
x = func("Hello")  # Notice that nothing is printed here as the wrapper function is never run
print(f"x = {x}")  # within x, an instance to the wrapper() function resides; x is the wrapper() function


def func(function):  # Redefine func w/ a function as the parameter
    def wrapper():
        print("Started")
        function()
        print("Ended")

    return wrapper


def func2():
    print("I am func2.")


print("With a function as a parameter stored inside the wrapper function and wrapper returned w/out ():")
x = func(func2)  # No operations are performed until x is called; wrapper() is stored within x
print(f"x = {x}")  # instance to wrapper is stored within x
x()  # x itself is a function

# We can replicate this behaviour where instead of storing the function inside a variable, we can store it inside of
# a variable of it's own name.
func2 = func(func2)  # Now, whenever func2() is called, the variable with an instance to func() is run instead of
# func2 itself. Now the wrapper() function around func2() is run instead.
print("Running func2 after creating a func2 variable of func(func2):")
func2()


# ---[DECORATORS]---
# Instead of going through this process, we can use a decorator which acts as a wrapper function to change the
# functionality of a function without changing it's code; the decorator functino must take a function as
# a parameter and run it in it's code.

@func  # declared like a dataclass
def func3():
    print("I am func3.")


print("Running func3() w/ func() as decorator: ")
func3()


# If your function takes arguments and you want to put a decorator on it, this may break other functions that use
# the same decorator since they use a different amount of arguments.
def keyworded_decorator(function):
    def wrapper(*args, **kwargs):  # We can use arge and kwargs to pass arguments into decorated functions
        print("Started")
        function(*args, **kwargs)  # also need to be in the function itself
        print("Ended")

    return wrapper


@keyworded_decorator
def func4():  # Normal function
    print("I am func4.")


@keyworded_decorator
def func_str(x):  # Function with args
    print(x)


func4()  # Despite having a different number of arguments with the same dataclass
func_str("I am func_str.")  # They both work


# You may also want to return values, and to do so you need to store the function in a variable
def returnable_decorator(function):  # Lots of boilerplate in this but just focus on what changes
    def wrapper(*args, **kwargs):
        print("Started")
        return_val = function(*args, **kwargs)  # Function is stored in return_val
        print("Ended")
        return return_val  # Returned after any post-function actions

    return wrapper


@returnable_decorator
def func_return(x, y):
    print(x)
    return y


rv = func_return("I am func_return.", "I am func_return's return value.")
print(rv)

# <CONDITIONALS>
print("\n\n\n\n---------------\n<CONDITIONALS>")

#:Basics:
print("\n:Basics:")
male = True
tall = False
if male:  # if you are not male, it will just skip this
    print("You are male.")
if male or tall:  # any parameter can be true
    print("You are either male or tall or both.")
if male and tall:  # all parameters must be true with "and"
    print("You are a tall male")
if not male and not tall:  # not means that the parameter must be false
    print("You are a short female.")
elif tall:
    # elif only excecutes if 1) the conditions are met and 2) the prev if statement doesn't run
    print("You are a tall female.")
else:  # if the if statement(s) previous to it is not true
    print("You are a short male.")

#:One Line Conditionals:
print("\n:One Line Conditionals:")
age = 15
print("kid" if age < 18 else "adult")  # Ternary conditionals; format: <expression1> if <condition> else <expression2>
print("kid" if age < 13 else "teenager" if age < 18 else "adult")  # they can also be chained


def divisible_by_5_or_3(num):
    return "Divisible by 3. " * (num % 3 == 0) + "Divisible by 5. " * (
            num % 5 == 0)  # Conditionals can be mimicked by multiplying


# by a true or false statement; False and True values will decide whether or not something is printed
print(divisible_by_5_or_3(45))
print(divisible_by_5_or_3(18))

# <DICTIONARIES>
print("\n\n\n\n---------------\n<DICTIONARIES>")
Definition = {  # Dictionaries are held inside of curly crackets
    "Hello": "A greeting used in America, The U.K, and other English speaking countries.",
    # Format: "Term : Definition"
    "Good Morning": "expressing good wishes on meeting or parting during the morning.",
    "Glasses": "a pair of lenses set in a frame resting on the nose and ears, used to "
               "correct or assist defective eyesight or protect the eyes.",
    "Keyboard": "a panel of keys that operate a computer or typewriter.",
    "Computer": "an electronic device for storing and processing data, typically in binary "
                "form, according to instructions given to it in a variable program.",
    "Hippo": "a large thick-skinned semiaquatic African mammal, with massive jaws and large tusks."
}
print(Definition["Keyboard"])  # Prints the defined parameter next to it
print(Definition.get("Abajabalaba", "Invalid"))  # Second parameter will run if the definition is not a valid parameter
for key in Definition.keys():  # Keys are the terms (left side of the colon)
    print(key)
for value in Definition.values():  # Values are the definitions (right side of the colon)
    print(value)
for item in Definition.items():  # Items are the keys and values
    print(item)
for key, value in Definition.items():  # You can also use items to return the key and value as keyworded variables
    print(key + " : " + value)

# <WHILE AND FOR LOOP (AND FOR ELSE)>

#:While Loops:
print("\n\n\n\n---------------\n<WHILE AND FOR LOOP (AND FOR ELSE)>")
print("\n:While Loops:")
i = 1
while i <= 4:  # While something is happening, a condition occurs
    print(i)
    i += 1
print("Loop finished.")

#:For Loops:
print("\n:For Loops:")
lettercount = 0
for letter in "Hello":  # Letter can be any variable name; for strings it is for each letter
    print(letter)  # you can interact with the variable in the for statement
    lettercount += 1
print(str(lettercount) + " (loop Finished)")
for index in range(3):  # you can also use a range (it will not use 3 in this scenario, because it zero indexes)
    print(index)
print("Loop Finished")

#:For Else:
print("\n:For Else:")
numbers = [12, 14, 16, 26, 43]
for number in numbers:
    if number % 5 == 0:  # as you can see, none of the numbers here are divisiblue by 5
        print(number)
else:  # You can use an else statement to set a sort of try except for a for loop; it has to be on the same indent level
    # as the original for loop, otherwise it will run after every for iteration
    print("not found")

# <TRY AND EXCEPT>
print("\n\n\n\n---------------\n<TRY AND EXCEPT>")
if skip_input == "n":
    try:  # essentially, try will move to carry out a different piece of code instead of throwing an error if an error occurs
        number = int(input("Enter a number: "))
        print(number)
    except:
        print("Please enter a number.")
    # You can also make different except blocks to catch different kinds of errors
    try:
        number = int(input("Enter a number to divide 100 by: "))
        print("100 divided by " + str(number) + " is " + str(100 / number) + ".")
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("Error")  # and you can jsut print the error with err
else:
    print("\n\n\n\n---------------\nTRY AND EXCEPT SECTION SKIPPED (CONTAINS INPUT)")

# <FILE IO>

#:Reading:
print("\n\n\n\n---------------\n<FILE IO>")
print("\n:Reading:")
example_text = open("example_text", "r")  # The first paramter is the file you're opening, the second is the type of
# access you have to that file (read R, write W, read and write R+, append A, etc.) Using the file name only works
# if the file is in the same directory as the python file
print(example_text.readable())  # checks if the file is readable
print(example_text.readline())  # Prints the first line
print(example_text.readline())  # Reads the next line
print(example_text.read())  # Prints the whole text / the rest of the unread text
print(example_text.readlines())  # Takes all lines and puts them into an array
# They are a little buggy when used one after the other
for employee in example_text.readlines():  # This is another way to use readlines
    pass
example_text.close()  # closes file

#:Appending:
print("\n:Appending:")
example_text = open("example_text", "a")
example_text.write("\nToby - Human Recources")  # adds to the end of the file
example_text.close()  # closes file
#:Making new files and writing to files:
# To write to a new file, write the same thing to open a file but add a name to a file that does not exist
test = open("index.html", "w")
test.write("<p>This is HTML<p>")  # Since you are writing to the file and not appending, it will override the whole
# file with whatever you choose to write
test.close()

#:Context Managers:
print("\n:Context Managers:")
with open("example_text", "w") as txt:  # The with keyword signifies a context manager; it will auto close after the
    # code is finished
    txt.write("Michael - Manager")  # This garuntees that all actions finish and the file closes after operation


class File:  # You can create your own context managers using classes
    def __init__(self, filename, method):
        self.file = open(filename, method)  # Opening the file on initialization

    def __enter__(self):  # This method is called when the file opens
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):  # This method is called if an exception is thrown or all actions within
        # the 'with' conditional have been completed. If an exception is raised, type is the exception type, value is
        # the exception value, and traceback is a traceback to the exception object
        print(f"type : {type}, value : {value}, traceback : {traceback}")  # Returning possible error data
        print("Exit")
        self.file.close()
        if type == Exception:  # Makes sure that the exception is expected; if the exception is an unexpected type,
            # then the program actually will stop (which is what you want b/c the exception is unexpected)
            return True  # Allows file to keep running after an exception with no interruptions or error message


with File("example_text", "w") as file:  # Notice that the __enter__ and __exit__ methods are run
    print("Middle")  # Within the context manager
    file.write("Jim - Sales")
    raise Exception()  # __Exit__ is run even if an exception is thrown, making exit handling possible

from contextlib import contextmanager  # a decorator from this file allows context managers to be made with generators


@contextmanager
def file(filename, method):
    print("Enter")  # Any __enter__ code
    file = open(filename, method)  # Acts as the __enter__
    yield file
    file.close()  # Acts as the __exit__
    print("Exit")  # Any __exit__ code


with file("example_text", "w") as file:
    print("Middle")
    file.write("Pam - Receptionist")

# <CLASSES AND OBJECTS>
print("\n\n\n\n---------------\n<CLASSES AND OBJECTS>")

#:Initialise and def:
# A class is simply defined with class [param]
print("\n:Initialize and Def:")


class Student():  # You can then define variables for said cass that can be accessed with class.var
    # you can make these defined on creation with the __init__ function (or initialise)
    def __init__(self, name, major, gpa, is_on_probation):  # These variables are defined on startup
        print("student created")  # You can also add things that the program will do on startup
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # These four make it so that you don't have to type self.name every time you want to call the name or other var


Jim = Student("Jim", "Buisness", 3.1, False)
Pam = Student("Jim", "Art", 2.5, True)
print(Jim.name)  # you can now access the classes variables
print(Pam.gpa)

#:Polymorphism:
print("\n:Polymorphism:")  # Polymorphism is simply different classes using the same function name. Generally the two


# functions have similar output as they answer the same demand.
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()

#:Class Functions:
print("\n:Class Functions:")


class Student2():
    def __init__(self, gpa):
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    # You can define class variables and use the object's variables to run them


Oscar = Student2(3.3)
Dwight = Student2(4.0)
Oscar.on_honor_roll()
Dwight.on_honor_roll()

#:Metaclasses/One Line Objects:
print("\n:Metaclasses/One Line Objects:")


# Metaclasses, in the same way that classes have objects as instances, metaclasses have classes as instances.
# In short, classes define how an object behaves and metaclasses define how classes behave.
# ---[ONE LINE OBJECTS]---
class inherited_object:
    def hello(self):
        print("hello")


def example_function(self):
    self.num = 10


object_type = type("object_name", (inherited_object,), {"x": 5, "num": example_function})  # Custom objects can be
# defined without a class; the format is type("name", (inherited objects), {"attribute name" : attribute})
# Note that the inherited objects list is a tuple and that the function attribute does not have a ()
object = object_type()
object.hello()
print(object.x)
object.num()
print(object.num)


# ---[METACLASSES]---
class capitalize_attributes(type):  # Metaclasses are defined by "type"
    def __new__(self, class_name, bases, attributes):
        print(attributes)  # Prints attributes before the capitalization
        capitalized_attrributes = {}  # Stored in a dict b/c attributes in type() are stored in a dictionary
        for name, val in attributes.items():
            if name.startswith("__"):  # Do not replace dunder methods
                capitalized_attrributes[name] = val
            else:
                capitalized_attrributes[name.upper()] = val
        print(attributes)  # Prints attributes after capitalization
        return type(class_name, bases, capitalized_attrributes)  # this return value returns the class parameters


class Dog(metaclass=capitalize_attributes):  # metaclass = {name of metaclass} will define the use of a metaclass
    x = 5  # These two variables and the function will be printed b/c of the print function in __new__
    y = 5

    def hello(self):
        print("hi")


example_dog = Dog()
try:
    print("Attempting to print dog.x")
    print(example_dog.x)  # This will break because (due to the metaclass) .x is no longer a attribuite of dog
except:
    print("Could not print dog.x, now attempting dog.X")
    print(example_dog.X)  # The attributes have been capitalized, so dog.X is the new attribute

#:Inheritance; Parent and Daughter classes:
print("\n:Inheritance:")


class chef():  # generic chef class
    def make_chicken(self):
        print("The chef makes chicken")

    def make_rice(self):
        print("The chef makes rice")

    def make_ribs(self):
        print("The chef makes ribs")


Chef1 = chef()
Chef1.make_rice()


class specialised_chef(chef):  # Tspecialised chef can do everything that a regular chef can do.
    def make_special_dish(self):  # you can also make this class do extra things
        print("The chef makes a special dish")

    def make_rice(self):  # You can also override a function or thing from the original class
        print("The chef makes brown rice")


Chef2 = specialised_chef()
Chef2.make_rice()
Chef2.make_special_dish()

#:Dunder/Magic Methods:
print("\n:Dunder/Magic Methods:")


# Double underscore (dunder) methods, also called magic methods, are used to override default functionality in python
# and create unique functions for your class; they override default functionality. There are more dunder methods other
# than the ones shown below, but these are the most important ones.
class overwrite:
    def __new__(cls, integer, string, boolean,
                name):  # The __new__ method is called before the class is formed; can make changes before the object is
        # made, thereby either changing how it is made or operating before the __init__ method
        print("Creating new object based on class 'overwrite'... ")
        obj = object.__new__(
            cls)  # These two lines are basically boilerplate; after you're done w/ the __new__ method you need to return the class
        return obj

    def __init__(self, integer, string, boolean, name):
        self.integer = integer
        self.string = string
        self.boolean = boolean
        self.name = name
        self.record = {
            "name": name,
            "balance": 100,
        }
        self.record_value_list = [key for key in self.record]

    def __repr__(self):  # represents a class's data as a string (ex: in a print statement)
        return f'overwrite("{self.integer}","{self.string}","{self.boolean}","{self.name}","{self.record["balance"]})'

    def __str__(self):  # override the str() method
        return self.string

    def __int__(self):  # override the int() method
        return self.integer

    def __bool__(self):  # override the bool() method
        return self.boolean

    def __setitem__(self, key, value):  # allows you to set an item of a dict/list with an instance to it's object
        self.record[key] = value

    def __getitem__(self, key):  # allows you to access dict/list items with just an instance of it's object
        return self.record[key]

    def __delitem__(self, key):  # allows you to delete an item in a dict/list with an instance of it's object
        del self.record[key]

    def __len__(self):  # allows you to access the length of an iterable with an instance of it's object
        return len(self.record_value_list)

    def __contains__(self, value):  # overrides membership operators
        return True if value in self.record else False

    def __call__(self):  # allows a function to be callable
        return f"{self.integer} {self.string} {self.boolean}"


overwrite = overwrite(0, "string", True, "Dave")
print(repr(overwrite))
print(str(overwrite))
print(int(overwrite))
print(bool(overwrite))
overwrite["debt"] = 25  # __setitem__
print(overwrite.record["debt"])  # __getitem__
del overwrite["debt"]  # __del__
try:
    print(overwrite.record["debt"])
except KeyError:
    print("KeyError: No key 'debt' found in overwrite.record.")
print(len(overwrite))
print("name" in overwrite)
print(overwrite())  # __call__

#:Dataclasses:

import random
from dataclasses import dataclass  # imported from dataclasses

print("\n:Dataclasses:")


# ---[BASICS]---

@dataclass  # dataclasses are specifically for storing (predominantly) data values and representing data
class number():
    val: int  # Values are defined as such; name : datatype


example_object = number(2)
print(example_object.val)  # values are called the same way you would from a class w/ an __init__ function
from typing import Any  # any can be used when you don't want to specifically define a datatype


@dataclass
class Undefined():
    name: Any
    value: Any


number_data = Undefined("three", 3)
from dataclasses import make_dataclass

string = make_dataclass("string", ["string_data"])  # make_dataclass does effectively the same thing
# The format for make_dataclass is make_dataclass("name", ["data"])
hello = string("Hello.")
print(hello.string_data)


# Dataclasses can also be used to remove boilerplate in classes; dataclasses automatically instantiate basic dunder
# methods for your classes. Those methods are __init__, __hash__, __repr__, __eq__, __lt__, __gt__, __le__, and __ge__
@dataclass
class Position:
    name: str
    longitude: float
    latitude: float


pos = Position("Oslo", 10.8, 59.9)
print(pos)  # notice how the values in the class can be printed without a __repr__ method


@dataclass
class YT_comment:
    comment: str
    user: str


comment1 = YT_comment("I subscribed.", "ChrisV")
comment2 = YT_comment("Bad video, I unsubscribed.", "BirdLuvr100")
comment3 = YT_comment("I subscribed.", "ChrisV")
print(comment1 == comment2)  # Once again, no __eq__ necessary
print(comment1 == comment3)

# ---[FIELD]---
from dataclasses import field
from typing import List  # List can be used to define a data value's datatype as list


# The field() function is used to specify aspects of each field of a dataclass specifically

def random_num():
    return random.randint(0, 15)


@dataclass
class field_values:
    default_3: int = field(default=3)  # default = {val} creates a default value
    random_number: int = field(default_factory=random_num)  # Uses a function's return value as default (note that
    # only the function's name is used and no () is used; b/c of this parameters cannot be used)
    no_repr: int = field(default=40, repr=False)  # Repr defined whether or not the field appears in the object's repr
    random_number2: int = field(default=20, compare=False)  # compare=False excludes field from comparisons such as
    # ==,  <, >,  etc;  order needs to be true for < and > to function (see ---[DATACLASS PARAMETERS]---)


test1 = field_values()
test2 = field_values(3, test1.random_number, 40, 22)
print(test1.default_3)
print(test1.random_number)
print(repr(test1))  # the fielf fourty is not present because it's repr=False
print(f"Test1.random_number1 = {test1.random_number2}")
print(f"Test2.random_number2 = {test2.random_number2}")
print(test1 == test2)  # Even though the random_num2 for the two objects are different, random_number2 has it's compare


# value set to False


# ---[DATACLASS PARAMETERS]---


@dataclass(frozen=True)  # frozen makes the dataclass immutable and disallowes the changing of values
class number:  # In general freezing dataclasses is a good practice as it garuntees a constant value
    num: int  # Usually with a dataclass no values need to be changed anyway


five = number(5)
try:
    print("Changing five.num to 6...")
    five.num = 6
except:
    print("Could not change five.num; dataclass 'num' is frozen.")


@dataclass(init=False, repr=False, eq=False)  # I am not going to explain these b/c they're pretty self explanitory
class ignore_this:  # The program simply forgoes the creation of the dunder method described
    pass


@dataclass(order=True)  # By default set to false; creates dunder methods for <, >, <=, >=, etc.
class YT_comment:  # Reused YT_comment class from before but this time the order is kept
    sort_index: int = field(repr=False, init=False)  # The order is based on the first variable in the class, which is
    # why the sort_index field must be first; needn't be included in the repr not the __init__ function
    order: int
    comment: str

    def __post_init__(self):  # used after initialization
        self.sort_index = self.order


comment1 = YT_comment(1, "I subscribed.")  # Same comments too
comment2 = YT_comment(2, "Bad video, I unsubscribed.")
print(sorted([comment2, comment1]))  # Notice that the comments are input in the wrong order, but are sorted because
# of the sort index. Note that in this scenario the __post_init__ function and the sort_index were not necessary
# because order could simply be the first variable defined, but it is good practice as they may be necessary in
# more complex classes
print(comment2 > comment1)  # Comparison operatos like > and < now work as well
print(comment1 > comment2)

# <BREAK CONTINUE AND PASS>
# break breaks out of a loop, continue will, and pass just ignores the


print("\n\n\n\n---------------\n<BREAK, CONTINUE, AND PASS>")
if skip_input == "n":
    for i in range(10):  # break breaks out of the loop
        break_ = input("Break (yes/no)?")
        if break_ == "yes":
            print("Broken")
            break  # breaks out fo the loop
else:
    print("BREAK SECTION SKIPPED (CONTAINS INPUT)")
for i in range(7):  # continue continues the loop but does not complete the current iteration
    if i % 3 == 0:  # If i is divisible by three
        continue  # continue the loop, but do not print that number
    print(i)
i = 89
if i == 389:  # pass simple means that there is no code and to skip over the loop or if statement
    pass

# <TIME MODULE>
import time

print("\n\n\n\n---------------\n<TIME MODULE>")
print("Seconds since epoch = " + str(time.time()))  # the amount of time since epoch (Jan 1st, 1970)
print("Local time: " + str(time.ctime(time.time())))  # Resembles local time, takes seconds since epoch as argument
time.sleep(2)  # sleeps/stops the program for a certain amount of seconds
localtime = time.localtime(time.time())  # takes seconds since epoch as argument, returns struct time
print(str("Local Year: " + str(localtime.tm_year)))  # you can retrieve many different variables from local time
print(str("Local Day: " + str(localtime.tm_mday)))
print(str("Local Hour: " + str(localtime.tm_hour)))
gmtime = time.gmtime(time.time())  # this does exactly the same thing but in GM time
print(str("GM Day: " + str(gmtime.tm_mday)))
print(str("GM Hour: " + str(gmtime.tm_hour)))

# <COLLECTIONS MODULE>
import collections

# A module that provides different types of data containers
print("\n\n\n\n---------------\n<COLLECTIONS MODULE>")

#:Counter:
print("\n:Counter:")
print(collections.Counter(
    ['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))  # Creates a dictionary w/ how many of each element
# of a list there are; also works with dictionaries and keyworded arguments

#:Default Dictionary:
print("\n:Default Dictionary:")
defdict = collections.defaultdict(
    lambda: "Not Present")  # DefaultDict provides default values for nonexistent keys and never
# raises KeyErrors; takes a function that determines what to return
defdict["a"] = "1"
print(defdict["a"])
print(defdict["b"])

#:Chainmap:
print("\n:Chainmap:")
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
chainmap = collections.ChainMap(d1, d2)  # chainmaps combine dictionaries and return a list of dictionaries
print(chainmap["a"])  # Data values can be accessed as normal with a key
print(chainmap.values())  # All values can be accessed with the .values() or .keys() functions
new_chainmap = chainmap.new_child(d3)  # New_child adds a new dictionary to the function
print(new_chainmap)  # You can also print a chainmap

#:NamedTuple:
print("\n:NamedTuple:")
StudentTuple = collections.namedtuple("Student",
                                      ["name", "age", "grade"])  # Named Tuples are tuples of information that
# allow keyworded data without requiring the creation of a dataclass
ChrisV = StudentTuple("Christopher", 14, "Freshman")  # Very similar to a dataclass
print(ChrisV.grade)
listStudent = ["Gavin-Kai", 15, "Freshman"]
print(StudentTuple._make(listStudent))  # you can use iterables to make named tuples

# Deque:
print("\n:Deque:")
DequeList = collections.deque([1, 2, 3])  # A list that is optimized for append and pop operations
DequeList.append(4)  # append works as normal
DequeList.appendleft(0)  # Appendleft (as expected) appends as the first element of a list
print(DequeList)
DequeList.pop()  # as usual, removes the rightmost element
DequeList.popleft()  # pops the first value
print(DequeList)

# <DATA STRUCTURES>
print("\n\n\n\n---------------\n<DATA MANAGEMENT>")

#:Stacks:
print("\n:Stacks:")
# Stacks are container types in python that follow the LIFO (last in first out) principle; this means that (as described)
# the last item entered into the container is the first one out (most notable describes lists)
stack = []
stack.append("first in")
stack.append("last in")  # this element was the last element to enter the stack
stack.pop()  # after popping an element from the list, the last element to be added is the first to leave
print(stack)

#:Queues:
print("\n:Queues:")
# Queues are container types that follow the FIFO (first in first out) principle; insertion and deletion happends on
# different ends and the first element added is the first to be removed. There is no queue data type in python, but
# queues can be emulated with deque (used in other programming languages)
import collections

queue = collections.deque([])
queue.append("first in")  # this element was the first element to enter the stack
queue.append("last in")
queue.popleft()  # after popping an element from the list, the first element to be added is the first to leave
print(queue)

#:Linked Lists:
print("\n:Linked Lists:")


# Linked lists are lists composed of elements that have two values; an instance to the next value and the value of the
# element itself. Linked lists must be traversed in chronological order and cannot be indexed
# Linked lists are not built into python and tbh idk when they would be used but we can emulate one with a node class
class List_Node():
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class LinkedList():
    def __init__(self):
        self.headval = None  # The head value of a linked list is the first value (all iterations must start there)

    def listprint(self):  # iterates through each element of the list to print itself
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


Linked_List_Days = LinkedList()  # Creating an empty linked list
Linked_List_Days.headval = List_Node("Sunday")  # Assigning the head value
Day2, Day3 = List_Node("Monday"), List_Node("Tuesday")  # Creating Nodes for the subsequent values
Linked_List_Days.headval.nextval = Day2  # Connecting the values
Day2.nextval = Day3
Linked_List_Days.listprint()
# Doubly Linked lists are linked lists in which each node has an instance to both the previous and next value, which
# I will not be displaying simply because it only requires adding an instance to the previous node

#:Hash Tables:
print("\n:Hash Tables:")
# Hash tables are data containers in which the index of an element is generated using a hash function. This makes the
# search and insertion functions significantly quicker as the key value itself becomes the index (via hash function)
# In python, dictionaries can function as hash tables as 1) the order of the data is not fixed and 2) the dictionary
# keys are hashable
dict = {'Name': 'Christopher', 'Age': 14}
print(dict['Name'])  # As shown, values are found not by a number index but a unique key value for each unique element
print(dict['Age'])  # Idk what else to say its literally a regular dictionary

#:Binary Tree:
print("\n:Binary Tree:")


# Trees are nonlinear data structures, unlike lists, arrays, etc. Trees are composed of nodes that are related either
# by a parent or child connection in a heirarchal manner. They are composed of the root (no parent), parent nodes (has
# both a parent and a child/children), and leaf nodes (no children). Each parent node sorts their children to their
# left or right, making search and insertion actions significantly faster because instead of iterating through each
# individual element, half of the data is eliminated with each node that is filtered (left/right).
# A Binary tree is a tree in which each node has no more than 2 children
# There are 3 ways to traverse (print every node in) a tree:
# 1) Pre-Order traversal : root - > left subtree - > right subtree
# 2) In-order traversal : left subtree - > root - > right subtree
# 3) Post-Order traversal : left subtree - > right subtree - > root
class Tree_Node():
    def __init__(self, data):
        self.data = data  # data must be defined
        self.left = None  # may not have child nodes so it is set to None
        self.right = None

    def insert(self,
               data):  # for this example, numbers will be used as data and >/< operations will determine left/right
        # Note that the insertion and search funcitons work pretty much the same
        if self.data:  # in case there is no root node
            if data < self.data:  # If new node is less
                if self.left is None:
                    self.left = Tree_Node(data)  # data is the new left if there is no left value already
                else:  # If the left data is taken
                    self.left.insert(data)  # The process is repeated on the left datapoint
            if data > self.data:
                if self.right is None:
                    self.right = Tree_Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data  # adding root node in case there is no root node

    def find_value(self, val):
        if val < self.data:  # determine which subtree to enter
            if self.left is None:  # if not found
                return str(val) + "not found."
            return self.left.find_value(val)  # recursion to continue down the tree
        elif val > self.data:  # determine which subtree to enter
            if self.right is None:  # if not found
                return str(val) + " not found."
            return self.right.find_value(val)  # recursion to continue down the tree
        else:
            return str(val) + " is found."  # val must be equal to root

    def pre_order_traversal(self, root):
        result = []
        if root:  # checks to see if there is a value to check
            result.append(root.data)  # appends the data
            result = result + root.pre_order_traversal(root.left)  # uses recursion for the root's left children
            result = result + root.pre_order_traversal(root.right)  # uses recursion for the root's right children
        return result

    def in_order_traversal(self, root):
        result = []
        if root:  # checks to see if there is a value to check
            result = result + root.in_order_traversal(root.left)  # recursion for root's left children
            result.append(root.data)  # adds root
            result = result + root.in_order_traversal(root.right)  # recursion for root's right children
        return result

    def post_order_traversal(self, root):
        result = []
        if root:  # checks to see if there is a value to check
            result = result + root.in_order_traversal(root.left)  # recursion for root's left children
            result = result + root.in_order_traversal(root.right)  # recursion for root's right children
            result.append(root.data)  # adds root
        return result


root = Tree_Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.pre_order_traversal(root))
print(root.in_order_traversal(root))  # prints chronologically
print(root.post_order_traversal(root))
print(root.find_value(14))
print(root.find_value(43))
print(root.find_value(27))

# <ALGORITHMS>
print("\n\n\n\n---------------\n<ALGORITHMS>")
# Algorithms are simply proccessess performed in steps to perform a task; in this section, specifically algorithms
# that perform its task on an iterable (sorting algorithms and searching algorithms)
# Time complexity, Big O notation, and optimizing algorithms will also be covered.

#:Big O Notation:
print("\n:Big O Notation:")
# Big O notation is a form of simple notation to quickly communicate the efficiency of a sorting algorithm. It does not
# take into account processing time, rather notes how the speed of an algorithm degrades as the input size gets larger.
# Here is a list of Big O notation runtime complexities from fastest to slowest.
# O(1) : constant : runtime is the same regardless of the input
# O(log n) : logarithmic : the runtime scales linearly while the input scales exponentially (ex: binary search)
# O(n) : linear : runtime scales linearly with the size of the output
# O(n log n) : logarithmic * linear : A logarithmic number of iterations, each iteration performing a linear action
# O(n^2) : quadratic : runtime is a quadratic function of the input (ex: each item must be checked twice in each loop)
# O(2^n) : exponential : extreemely inefficient

#:Search Algorithms:
print("\n:Search Algorithms:")


# ---[BUBBLE SORT]---
# Bubble sort is a method of sorting in which a loop goes through the iterable comparing elements 2 at a time. If the
# comparison is wrong, the elements are swapped, which will naturally "bubble" the greatest element to the top of the
# list with each iteration.
# Bubble sort in a worst case time complexity is O(n^2)
def bubble_sort(list):
    length = len(list)  # length is goign to need to change as it iterates, so a variable is defined
    for num in range(length):
        sort_finished = True  # So that the loop doesn't iterate infinitly
        for index in range(
                length - num - 1):  # As it iterates, less numbers are checked (b/c the greatest are sorted to the top)
            if list[index] > list[index + 1]:  # Compares two numbers
                list[index], list[index + 1] = list[index + 1], list[index]  # Swaps if they are out of order
                sort_finished = False  # Since 2 numbers were out of order, the sort cannot be finished
        if sort_finished:
            break
    return list


print(bubble_sort([8, 4, 7, 24, 9, 2, 0]))


# ---[INSERTION SORT]---
# Insertion sort is an optimized version of bubble sort where the list is iterated one element at a time and each element
# is compared with every element on its left and inserted into the correct position.
# Insertion sort in a worst case time complexity is O(n^2) (but generally faster than bubble sort)
def insertion_sort(list):
    for index in range(1, len(list)):  # start at 1 b/c the first element has nothing to compare to
        key_item = list[index]  # the element that we need to insert
        prev = index - 1  # this will be used to find the correct place for the key item
        while prev >= 0 and list[prev] > key_item:  # compares the key item w/ values to its left
            list[prev + 1] = list[prev]  # If the item to the left is greater, the previous item is moved forward
            prev -= 1  # moving the index back 1
        list[prev + 1] = key_item  # inserting the key item into the correct place
    return list


print(insertion_sort([8, 4, 7, 24, 9, 2, 0]))


# ---[MERGE SORT]---
# Merge sort follows the 'divide and conquer' methodology. The iterable is recursively split in half, solved 2, 4,
# 8, etc. at a time, and merged back together by comparing the starting numbers of the 2 lists and appending the smaller
# one first to a result list. Merge sort is not always the fastest method to sort with, but it has the best worst-case
# scenario (no other algorithm is faster than O(n log n) in a worst case scenario).
# Merge sort in a worst case time complexity is O(n log n)
def merge(left, right):  # This will sort the list given a left and a right section
    if len(left) == 0 or len(right) == 0:  # if array is empty, nothing needs to be merged
        return left + right
    result = []  # to append the sorted elements
    index_left, index_right = 0, 0
    while len(result) < len(left) + len(right):  # going through both arrays until all elements are in the result list
        if left[index_left] <= right[index_right]:  # Deciding which list has the smaller number (append that first)
            result.append(left[index_left])
            index_left += 1  # move onto next number in the list for comparison
        else:
            result.append(right[index_right])
            index_right += 1  # move onto next number in the list for comparison
        if index_right == len(right):  # if the end of a list is reached, you can just append the other one
            result += left[index_left:]
            break
        if index_left == len(left):  # if the end of a list is reached, you can just append the other one
            result += right[index_right:]
            break
    return result


def merge_sort(list):  # Uses merge to sort, this just breaks up the list
    if len(list) < 2:  # If there are less than 2 elements, there is nothing to sort
        return list
    midpoint = len(list) // 2
    return merge(left=merge_sort(list[:midpoint]), right=merge_sort(list[midpoint:]))  # Split input in two halves
    # repeatedly, sort, then merge


print(merge_sort([7, 3, 54, 1, 96, 2, 9]))
# ---[QUICKSORT]---
# Quicksort is a sorting algorithm that also uses the divide and conquer methodology but in a different way. The program
# selects a pivot and sorts numbers into 2 groups; numbers higher and lower than the pivot. This is then applied
# recursively until the entire list is sorted.
# Quicksort in a worst case time complexity is O(n^2)
# It is important to know that pivot is paramount and is generally based on luck. Quicksort is O(n^2) in a worst case
# scenario but can be O(n) in a best case scenario and is usually O(n log n)
import random


def quicksort(list):
    if len(list) < 2:  # If the length is less than 2, there is nothing to sort
        return list
    low, same, high = [], [], []
    pivot = list[random.randint(0, len(list) - 1)]  # random pivot used to avoid bias
    for item in list:  # appending to the right list using the pivot for comparison
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(
        high)  # recur the program w/ quicksort as the sorting algo for the new lists


print(quicksort([67, 2, 9, 43, 6, 12, 23, 8]))


# ---[TIMSORT]---
# Timsort is the default sorting algorithm used in python and case be accessed using the sort() or sorted() built-in
# functions. Timsort functions by spliting the list into section (if necessary), similar to merge sort, then
# uses insertion sort to sort each section, then using merge sort to merge them all together again. Timsort is known
# for beating the best case scenario of merge sort and matching quicksort's best case scenario while simultaneously
# beating quicksort's worst case scenario and matching merge sort's worst case scenario.
# Though simply sort() can be used, a replication will be built for understanding.
# Worst case time complexity O(n log n), best case time complexity O(n)
def modified_insertion_sort(list, left=0, right=None):
    if right is None:  # set right as len(list)-1 b/c we can't do it in the declaration
        right = len(list) - 1
    for index in range(left + 1, right + 1):  # loop each index in the list (except 0 b/c there is nothing to compare)
        key_item = list[index]
        prev = index - 1
        while prev >= left and list[prev] > key_item:  # compare key item to the item on its left
            list[prev + 1] = list[prev]  # move the previous item forward
            prev -= 1  # reduce index to move back in the list
        list[prev + 1] = key_item  # insert original index in the right position
    return list


def merge(left, right):  # Timsort requires merge, so I copied the function here for reference (and copy+paste)
    if len(left) == 0 or len(right) == 0:
        return left + right
    result = []
    index_left, index_right = 0, 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def timsort(list):
    min_run = 32  # size of a list section
    length = len(list)
    for num in range(0, length, 32):  # Every multiple of 32 including 0
        modified_insertion_sort(list, num,
                                min((num + min_run - 1), length - 1))  # list and a range of 32 numbers in the list
    size = min_run
    while size < length:
        for start in range(0, length, size * 2):  # double the size every iteration (b/c you merge lists each iteration)
            midpoint = start + size - 1  # Where the first list ends and the second list starts
            end = min((start + size * 2 - 1), length - 1)  # End of the second list
            merged_list = merge(left=list[start:midpoint + 1], right=list[midpoint + 1:end + 1])  # use merge
            # function to combine the two lists; use start/midpoint/end for left and right
            list[start:start + len(merged_list)] = merged_list  # put merged list back into the original list
        size *= 2  # each iteration doubles the list size
    return list


print(timsort([6, 86, 53, 13, 3, 75, 5, 9]))
# Of course, you can also just use sort().
list = [6, 86, 53, 13, 3, 75, 5, 9]
list.sort()
print(list)

#:Search Algorithms:
print("\n:Searching Algorithms:")
# ---[MEMBERSHIP OPERATORS]---
# Membership operators are best for determining if something is in a list
list = [5, 8, 3, 7, 2]
string = "string string string"
print(5 in list)
print(9 in list)
print("str" in string)
print("bool" in string)


# Membership operators are built in and easy to use but do not give the index of the thing in the iterable; the following
# methods do.
# ---[LINEAR SEARCH]---
# Linear search simply iterates through every element and returns the index and whether it is present
# The big O time complexity for linear search is O(n)
def linear_search(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return index
    return "not found"


print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search([1, 2, 3, 4, 5], 10))


# ---[BINARY SEARCH]---
# Binary search is significantly faster than linear search. but the list must be sorted for it to work. Binary search
# recursively compares the search value with the mid value in the list until it finds (or doesn't find) the value.
# The big O time complexity for binary search is O(log n)
def binary_search(list, value):
    first = 0
    last = len(list) - 1
    result = "Not found."  # this will be the error/not found return value (will not change if not found)
    while first <= last and (result == "Not found."):  # if first > last the whole list has been searched
        mid = (first + last) // 2  # middle of the list
        if list[mid] == value:
            result = mid
        else:
            if value < list[mid]:
                last = mid - 1  # cutting half of the list based on the list value's comparison to the middle
            else:
                first = mid + 1
    return result


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
print(binary_search([4, 4, 4, 4, 4], 4))  # note that if multiple instances of the search result are in the list, binary


# search will not returns the first instance of the result but instead the one closest to the middle.
# ---[JUMP SEARCH]---
# Jump search is another divide and conquer search method that divides the iterable into sqrt(len(iterable)) sized
# sections, then searches the section that contains the desired value via linear search. As with binary search, the list
# must be sorted for jump search.
# Jump search has a time complexity of O(sqrt n); long story short slower than O(log n) and faster than O(n)
def jump_search(list, value):
    length = len(list)
    jump = int(math.sqrt(length))  # idk why sqrt(length) is the best jump length, trust the experts ig
    left, right = 0, 0  # To represent the left and right side of every jump
    while left <= length and list[left] <= value:  # Loop breaks if the whole list is scanned w/ no result
        right = min(length - 1, left + jump)  # Adding the jump, or the end of the list if we are there
        if list[left] <= value and list[right] >= value:
            break
        left += jump  # jump to the next section
    if left >= length or list[left] > value:  # End if value is not found
        return "not found"
    right = min(length - 1, right)  # set right to either end of list or end of current jump (whichever comes first)
    index = left
    while index <= right and list[index] <= value:  # linear search within the section
        if list[index] == value:
            return index
        index += 1
    return "not found"  # if value is not found


jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)


# ---[EXPONENTIAL SEARCH]---
# Exponential search is (yet again) a method that requires a sorted list. Exponential search first determines the range
# where the element we're looking for is likely to be, then uses binary search in that range. It is very simply to
# implement (given you have a binary search function).
# The time complexity for exponential search is O(log n) and works best when the desired element is near the beginning
# of the iterable
def exponential_search(list, value):
    if list[0] == value:  # can't multiply by 0 so we just get it out of the way here
        return 0
    index = 1
    while index <= len(list) and list[index] <= value:  # Check if we have passed the desired value/full list finished
        index *= 2
    print(list[:min(index, len(list))])
    return binary_search(list[:min(index, len(list))], value)  # run binary search w/ the index as the ending point


print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))


# ---[INTERPOLATION SEARCH]---
# Interpolation search uses a formula to find the probable position of a value. Interpolation search trumps binary
# search for lists that are evenly distributed, as the formula proides quicker location of the desired value.
# Formula: index = low + [(val-list[low])*(high-low) / (list[high]-list[low])]
# It's basically binary search but it starts where the desired value would likely be based on the highest and lowest
# value of the iterable.
# Interpolation Search's average time complexity is O(log log n)
def interpolation_search(list, value):
    low = 0
    high = len(list) - 1
    while low <= high and value >= list[low] and value <= list[
        high]:  # checking to make sure the value is between low/high
        index = low + int(((float(high - low) / (list[high] - list[low])) * (value - list[low])))
        if list[index] == value:
            return index
        if list[index] < value:
            low = index + 1
        else:
            high = index - 1
    return "not found"


interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)

#:Timing Algorithms:
print("\n:Timing Algorithms:")


# Algorithms can be timed in multiple ways; in this program a class is used
class TimerError(Exception):  # inherits the exception class (built in to python)
    """"Custom Exception for errors in timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):  # start timer
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")  # self explanitory
        self._start_time = time.perf_counter()  # performance counter function

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")  # self explanitory
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"{elapsed_time:0.4f} seconds")


search_timer = Timer()
search_timer.start()
linear_search([num for num in range(1000000)], 913478)
print("Linear Search:")
search_timer.stop()
search_timer.start()
binary_search([num for num in range(1000000)], 913478)
print("Binary Search:")
search_timer.stop()
search_timer.start()
interpolation_search([num for num in range(1000000)], 913478)
print("Interpolation Search:")
search_timer.stop()

# <CONCURRENCY, THREADING, AND PARALLELISM>
print("\n\n\n\n---------------\n<CONCURRENCY, THREADING, AND PARALLELISM>")
# Concurrency is muiltiple actions happening at the same time; this section is dedicated to writing code to run
# concurrently and get the most out of computer hardware.

#:Threading:
print("\n:Threading:")
import threading


# Threads are essentially queues that run into the same core; they determine which operations are performed in what
# order in which core. Each core has 2 threads (on avg) running into it and even though only 1 can be processed at a
# time, a thread can be left 'hanging' (temporarily stopped mid-process) for another thread to run. Threading generally
# yields performance benefits when other operations can be run while the program is waiting for io (pulling data,
# user input, etc.).

# ---[INSTANTIATING/ORDERING THREADS WITH SLEEP]---

# for reference the main thread is thread 1
def threaded_func(sleep_val):  # this will be the function that gets threaded; for reference this is thread 2
    print("This message is from thread 2.       Sent at start.")
    time.sleep(sleep_val)
    print("This message is from thread 2.       1 second after start.")


thread2 = threading.Thread(target=threaded_func,
                           args=(1,))  # allocate a new thread; name of function (no parenthesis) and pass
# args in a tuple (like a metaclass type)
thread2.start()  # runs the function in the new thread that we defined as x
print("\nThis message is from thread 1.       Sent at start.")  # Shows
# how many threads are active (note; threads active, not threads created)
time.sleep(0.9)  # Note that the running thread is based on sleep time; this sleep is shorter than the sleep time in
# thread 2, so thread 1 will continue running even though it went to sleep.
print("This message is from thread 1.       0.9 seconds after start.")
time.sleep(0.3)  # The running thread now switches to thread 2 because the next action from thread 2 is sooner than the
# next action from thread 1.
print("This message sent from thread 1.     1.5 seconds after start.")

# ---[ORDERING THREADS WITH JOIN]---
# When using threads to access a global variable, sleeps are ususally necessary to let the threads run concurrenty.
# This brings the problem of code following the threads running between the thread's execution times, leading to
# threads not finishing their tasks before the program moves on. This can be fixed with the join() function, which lets
# only certain threads to work before the program continues.

lst = []  # The threads will access a shared global variable


def count(n):  # These two functions access the same list and are both appending 1-5 to it
    for num in range(1, n + 1):
        lst.append(num)
        time.sleep(0.25)  # allows the thread to switch


def count2(n):
    for num in range(1, n + 1):
        lst.append(num)
        time.sleep(0.25)


thread1 = threading.Thread(target=count, args=(5,))  # Instantiating and running both threads
thread1.start()
thread2 = threading.Thread(target=count2, args=(5,))
thread2.start()

thread1.join()  # These two lines stop the code after them from running until both threads finish.
thread2.join()  # Note that thread 2 is not held up by thread 1's join functino because thread2 has already been
# started when thread 1's join function was called; the join function only defines which threads to wait for, not which
# ones to run.

print(lst)

# ---[THREADING METHODS]---

print(f"\nActive threads : {threading.activeCount()}. Current thread : {threading.current_thread()}.")  # These two are
# self explanitory; note that active threads returns the number of threads active, not the number of threads created
print(f"List of all active threads : {threading.enumerate()}.")  # Doesn't include terminated threads and threads that
# have not yet been started, but always includes the main thread
print(f"Main thread : {threading.main_thread()}.")  # Usually the thread from which the interpreter started
print(f"Is thread1 alive : {thread1.is_alive()}.")  # Also self explanitory, checks if a thread is active


# ---[USING FOR LOOPS FOR THREADING]---

def function():
    print("Thread started.")
    time.sleep(1)


threads = []  # we will use a list to make sure that the code does not continue until the for loop ends

for _ in range(5):  # '_' signifies a throwaway variable that is not used in the loop
    thread = threading.Thread(target=function)
    thread.start()
    threads.append(thread)  # Making sure that all threads can be recalled

for thread_ in threads:  # For loop used to make sure that nothing else is run while the threads are sleeping
    thread_.join()

print("Finished.")


# ---[DAEMON THREADS]---
# Daemon threads are threads that run in the background, usually in aid to the main thread. The main distinction between
# daemon threads and regular threads are that if only daemon threads are running, the program finishes. This is
# important because it means that they can run the the background and automatically terminate when the program finishes.

def timer():
    count = 0
    while True:  # Runs the loop ndefinetley
        time.sleep(1)
        count += 1
        print(f"\ntimer_function : time running (counting by 5's) : {count}.\n")


timer = threading.Thread(target=timer, daemon=True)  # You can set it as a daemon thread in the instantiation
timer.setDaemon(False)  # You can also use .setDaemon() to change whether or not it is a daemon thread
timer.setDaemon(True)
# Not going to start the thread because it would make the output for the rest of the script very messy
print(f"Is timer a daemon thread : {timer.isDaemon()}")  # Checks to see if a thread is a daemon thread

import time

#:Concurrent Futures Module:
print("\n:Concurrent Futures Module:")
# Concurrent.futures is a high level interface for asynchronously running tasks; it essentially simplifies threading
# and makes it less syntax heavy while also adding additional functionality.
import concurrent.futures as cf

# ---[EXECUTOR BASICS]---

# There are 2 executors in concurrent.futues; ThreadPoolExecutors and ProcessPoolExecutors. Both stem from the executor
# class and share common methods that stem from said class.
# executor.submit() schedules the callable, fn, to be executed as fn(*args, **kwargs) and returns a Future object
# representing the execution of the callable; this Future object's result can be used with {future object}.result()
# Ignore the ThreadPoolExecutor; ProcessPoolExecutor would function the same way b/c both are Executors
# max_workers is the max amount of processes in the executor at once. If max_workers is None or not given, it will
# default to the number of cores on the machine, multiplied by 5.

with cf.ThreadPoolExecutor(max_workers=1) as executor:  # context managers are used to work with Executors, max_workers
    # is the maximum amount of threads/processes
    future = executor.submit(pow, 3, 2)  # callable comes first, the args and kwargs
    print(future.result())


def wait(sleep_time):
    print(f"Waiting for {sleep_time} seconds...")
    time.sleep(sleep_time)
    return "Done sleeping."


with cf.ThreadPoolExecutor() as executor:  # note that max_workers is not always necessary
    results = [executor.submit(wait, 1) for _ in range(3)]  # list comprehensions can be used, similarly to threading,
    # to schedule multiple of the same function (wait is the function, 1 is the arg)
    for result in cf.as_completed(results):  # as_completed is self explanitory; returns future object as completed
        print(result.result())

# Map can be used to apply a function to an iterable; the format is map(func, *iterables, timeout=None, chunksize=1)
# Map returns the results, not a future object.
# If 1 chunk of the function takes longer than {timeout} seconds a TimeoutError appears.
# Chunksize is how many elements of the iterable are stored in 1 process; with ThreadPoolExecutor, larger chunksizes
# will greatly improve performance w/ larger iterables (with ThreadPoolExecutor, chunksize has no effect)

with cf.ThreadPoolExecutor() as map_executor:
    nums = [1, 2, 3, 4]
    results = map_executor.map(lambda num: num * 2, nums)  # returns individual values, not an iterable
    print([result for result in results])

# Shutdown() forces the executor to finish all pending futures and stop accepting submit() calls thereafter

with cf.ThreadPoolExecutor() as executor:
    future1 = executor.submit(wait, 1)
    executor.shutdown()
    try:
        print("Attempting to submit to executor post-shutdown...")
        future2 = executor.submit(wait, 1)
    except RuntimeError:
        print("Could not submit to executor after shutdown.")

# ---[FUTURES OBJECTS]---

with cf.ThreadPoolExecutor() as executor:
    num = executor.submit(lambda x: x + 69, 420)  # random example function
    print(num.cancel)  # attempts (note: **attempts**) to cancel the future. printing it returns True or False based on
    # whether the future was able to be cancelled
    print(num.cancelled())  # self explanitory; whether or not a future was cancelled
    wait_ = executor.submit(wait, 1)
    print(wait_.running())  # prints whether or not a future is running
    time.sleep(1.1)
    print(wait_.done())  # prints whether or not a future is finished

# ---[THREADPOOLEXECUTOR]---

# The ThreadPoolExecutor is similar to threading (in that you need a callable) but is different in that each thread
# you submit to the pool starts automatically and the pool must finish all threads before continuing. This has already
# been showcased, but here is an example in which the program must connect to the web, a situation in which the
# program must wait for the site to respond and can therefore use threading to call the next request while the
# first request is still pending.

import urllib.request as url_req

URLS = ['http://www.foxnews.com/', 'http://www.cnn.com/', 'http://europe.wsj.com/', 'http://www.bbc.co.uk/',
        'exception_example.com']  # Notice that the last link is not valid, and europe.wsj is forbidden


def load_url(url, timeout):  # Retrieve a single page and report the URL and contents
    with url_req.urlopen(url, timeout=timeout) as page:  # Opens the url, sets a timeout in case it doesn't work
        return page.read()


with cf.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}  # mark each URL by future in a dictionary
    for future in cf.as_completed(future_to_url):  # loop over each link as the future is completed
        url = future_to_url[future]
        try:
            data = future.result()  # try to assign data (wont work if there is none)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))  # if not possible print exception message
        else:
            print('%r page is %d bytes' % (url, len(data)))  # if it worked print the url and length


# Deadlocks are situations in which multiple functions are waiting on output from one another, leading to neither
# function finishing execution

def wait_on_b():
    time.sleep(0.5)  # give time for the other function to run
    print(b.result())
    return 42069  # throwaway return value


def wait_on_a():
    time.sleep(0.5)
    print(a.result())
    return 42069


if 42069 == 69420:  # Not running this for obvious reasons
    executor = cf.ThreadPoolExecutor(max_workers=2)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)


# This is also possible if a function uses it's own result and there is only 1 worker thread

def wait_on_future():
    f = executor.submit(pow, 5, 2)
    print(f.result())


if 69420 == 42069:
    executor = cf.ThreadPoolExecutor(max_workers=1)
    executor.submit(wait_on_future)

# ---[PROCESS POOL EXECUTOR]---

# The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously.
# ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock but also
# means that only picklable objects can be executed/returned (most notably no lambda functions).
# Calling Executor or Future methods from a callable submitted to a ProcessPoolExecutor will result in deadlock.
# Format: ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=()
# max_workers is, by default, the number of cores on the machine and must be less than 61. mp_context allows you to
# enter a multiprocessing context (as seen in the multiprocessing module) and is set to the default multiprocessing
# context if not entered. Initializer is an optional callable run at the beginning of each process, and initargs are
# the arguments for said callable.
# ProcessPoolExecutor, since it uses multiprocessing (and therefore multiple cores), is best for cpu bound processes.

prime_nums = [100003, 131071, 198733, 237895]


def is_prime(n):  # Function to find primes (not important u can ignore this)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# ProcessPoolExecutor, because of it's use of multiprocessing, requires the code to be guarded by if
# __name__=="__main__"; this messes with the code outside of __main__'s scope, so I will not be running the following
# code by putting and 0==1 after the __name__=="__main__" statement.
if __name__ == "__main__" and 0 == 1:
    with cf.ProcessPoolExecutor() as executor:  # same as ThreadPoolExecutor
        for number, prime in zip(prime_nums, executor.map(is_prime, prime_nums)):  # Also same as ThreadPoolExecutor
            print(f"{number} is prime: {prime}")

    with cf.ProcessPoolExecutor() as executor:  # Example of the implementation with chunksize (use w/ big iterables)
        for number, prime in zip(prime_nums, executor.map(is_prime, prime_nums, chunksize=2)):
            print(f"{number} is prime: {prime}")

#:Multiprocessing:
print("\n:Multiprocessing:")
import multiprocessing
# The multiprocessing module uses similar api to the threading module but is different in that it allows the use of
# multiple cores during processing (instead of multiple threads).
# As stated before, multiprocessing requires code to be guarded by if __name__=="__main__", and this messes with the
# code outside of __main__'s scope, so I will not be running the following code by putting and 0==1 after the
# __name__=="__main__" statement.

# ---[OS/MULTIPROCESSING FUNCTIONS]---
# This section is for getting values from the system about processes / multiprocessing data
# Some of these values are obtained from the os module
import os

print(f"Module name : {__name__}")  # Gets name of the file running
print(f"Parent process id : {os.getppid()}")  # Gets the parent process id of the current process
print(f"Process id : {os.getpid()}")  # Gets the process name of the current id
print(f"Cpu cores : {multiprocessing.cpu_count()}")  # number of cpu cores
print(f"Current Process : {multiprocessing.current_process()}")  # Gets name and parent of current process along with
# whether it has started or not
if 0 == 1:  # not running because there is no thread to check but this checks if a thread is running
    print(f"Thread is alive : {example_thread.is_alive()}.")


# whether or not it has started or not

# ---[PROCESS AND POOL]---
# Processes in multiprocessing are formed by creating a Process object and calling it's start method. It is similar
# to threading in concept and syntax. Pools are similar in functionality to concurrent.future's ProcessPoolExecutor.
# Pool allows the input of Pool(processes, initializer, init_args, maxtasksperchild). As a reminder, Initializer is an
# optional callable run at the beginning of each process, and initargs are the arguments for said callable. Proesses
# is the amount of cores the pool will use and maxtasksperchild is self explanitory.

def hello(name):
    print(f"Hello, {name}.")


def return_hello(name):
    return f"hello, {name}."


if __name__ == "__main__" and 0 == 1:
    process = multiprocessing.Process(target=hello, args=("Christopher",))
    process.start()
    process.join()

    with multiprocessing.Pool() as pool:  # once again, context managers are used
        pool.map(hello, ["Christopher", "Gavin-Kai"])  # map is the same syntax wise

    with multiprocessing.Pool() as pool:  # return values for map are returned as an iterable
        results = pool.map(return_hello, ["Christopher", "Gavin-Kai"])
        for result in results:
            print(result)

    with multiprocessing.Pool() as pool:  # map_async does not wait for the pool to finish; same as not using .join()
        pool.map_async(hello, ["Christopher", "Gavin-Kai"])


# ---[SHARING DATA BETWEEN PROCESSES]---
# There are two ways to share processes between processes; a queue (FIFO, pretty much the same as queue.Queue and
# similar to collections.deque) and a pipe (an object with a two-way connection between proecesses)

def put_items_in_queue(queue):
    queue.put(True)  # Queue uses the 'put()' function to accept values
    queue.put([42, None, "hello"])  # Also accepts lists


if __name__ == "__main__" and 0 == 1:
    qq = multiprocessing.Queue()
    process = multiprocessing.Process(target=put_items_in_queue, args=(qq,))
    process.start()
    print(qq.get())  # fetches first queue value
    process.join()


# The best way to demonstrate how a queue can be used is through a reader and writer function
def writer(count, queue):  # self explanitory; adds number to queue based on a count
    for num in range(count):
        queue.put(num)
    queue.put("DONE")


def reader(queue):  # also self explanitory; reads queue indefinetley until it recieves a "DONE" argument
    while True:
        num = queue.get()
        print(num)
        if num == "DONE":
            break


if __name__ == "__main__" and 0 == 1:
    qq = multiprocessing.Queue()
    reader_process = multiprocessing.Process(target=reader, args=(qq,))
    reader_process.daemon = True  # makes sure that the reader_process doesn't terminate when writer_process start
    reader_process.start()
    writer_process = multiprocessing.Process(target=writer, args=(3, qq))
    writer_process.start()
    reader_process.join()  # makes sure that the reader process doesn't terminate after the program ends and can complete
    # it's loop (because we assigned it as a daemon)


# Pipe shown below

def send_info(connection):
    connection.send("Example string")  # .send() is used to send data
    connection.send([42, None, "Hello"])  # data can also be sent in an iterable
    connection.close()  # run automatically when garbage data is collected but good practice to do it manually


if __name__ == "__main__" and 0 == 1:
    parent_connection, child_connection = multiprocessing.Pipe()  # If duplex=True (default) then info can be sent both
    # ways. If duplex is False then conn1 can only be used for receiving messages and conn2 can only be used for
    # sending messages.
    process = multiprocessing.Process(target=send_info, args=(child_connection,))
    process.start()
    print(f"Parent connection data : {parent_connection.recv()}")  # recieves the least recent data sent (FIFO)
    print(f"Parent connection data : {parent_connection.recv()}")  # Note that if there is no data to be received, the
    # connection will wait for more data to be sent
    print(f"Data in pipe : {parent_connection.poll()}")  # Returns a boolean based on if there is data left in the pipe
    process.join()


# ---[VALUE SHARED DATATYPE]---

# Multiprocessing offers shared datatypes in the form of multiprocessing.Value. Values need to be identified by their
# typecode; type codes are identified by this website https://www.educative.io/answers/what-are-type-codes-in-python
# but will also be shown here: 'c' = character, 'i' = int, 'f' = float, 'd' = dobule

def add(val, addend):
    val.value = val.value + addend  # val itself is just a wrapper, val.value is necessary to access the value


if __name__ == "__main__":
    value = multiprocessing.Value("d", 0)  # format is multiprocessing.Value("typecode", value)
    for _ in range(2):  # running the process twice to show that the variable is universally accessible
        process = multiprocessing.Process(target=add, args=(value, 2))
        process.start()
        process.join()  # make sure that the value has changed before the next process uses it
    print(value.value)


# ---[LOCKS]---
# Locks can be used to force the program to focus on one process at a given time.

def hello(lock, num):
    lock.acquire()  # starts the lock and prevents other processes from running
    try:
        print(f"Hello {num}")
    finally:
        lock.release()  # releases the lock and allows other processes to run


if __name__ == "__main__" and 0 == 1:
    lock = multiprocessing.Lock()  # note that lock takes no parameters
    for num in range(3):
        multiprocessing.Process(target=hello, args=(lock, num)).start()  # defining/starting process in the same line

# Note that in the process above, the output is liable to getting mixed up (out of order) if they are run in different
# cores, as some cores might end up running the process faster even if the process is submitted later.

# :Async IO:
print("\n:Async IO:")
# Async IO is a module that is used to maximise the usage of a single thread by handling I/O asynchronously using
# coroutines. A coroutine is a specialized generator function which can be suspended itself during execution, allowing
# another coroutine to gain control. Async IO use cases are similar to threading.

import asyncio


# ---[ASYNC/AWAIT]---
# The most simple illustration of asyn io functionality is this function, similar to ThreadPoolExecutor from
# concurrent.futures and threaded for loops. Main point here is to notice the different syntax. The term 'event
# loop' will be mentioned here; the event loop waits for and dispatches events in a program. Event loops are created
# with the asyncio.run() function.

async def count():  # the keyword 'async' defines an function with asynchronous functionality (a coroutine); note that
    # 'async for' and 'async with' are also valid. asynchronous functions, when called, do not run but return a
    # coroutine object similar to a future.
    print("One")
    await asyncio.sleep(1)  # the keyword 'await' suspends the execution of the current coroutine and passes control
    # back to the event loop. this coroutine will regain control when the function after the 'await' keyword finishes
    # In order for an object to be placed after an 'await' keyword, it must be awaitable. Awaitable objects are either
    # another coroutine or an object defining an .__await__() dunder method that returns an iterator (usually the
    # first). Note that the await keyword is necessary to run asynchronous functions, and the await keyword can only
    # be placed within another asynchronous function.
    print("Two")


async def main():
    await asyncio.gather(count(), count())  # gather is similar to map/pool and can be used to run multiple coroutines


asyncio.run(main())  # notice that since there is no parallelism, no guard is necessary (if __name__=="__main__"). This


# run function creates an event loop to run the asynchronous functions.


async def variable(example_variable):
    return_val = await made_up_function(example_variable)  # you can assign await values like you can normal ones
    return return_val


# ---[CREATE TASK]---
# You can create a task to stop further lines of code from being blocked by the current line; if the task is waiting
# on i/o, further lines of code will continue running (same thing as before but within the same coroutine)

async def func():
    print("Started (inner) function.")
    await asyncio.sleep(1)


async def wrapper():
    print("Started wrapper function.")
    await func()  # notice that even though both function are asynchronous, the wrapper function waits for the inner
    # function because it has been told to do so by the await keyword
    print("Finished wrapper function.")


asyncio.run(wrapper())


async def wrapper2():
    print("Started wrapper2 function.")
    task = asyncio.create_task(func())  # create tasks is different in that it creates a task object that is run
    # asynchronously with the rest of the coroutine; note that it won't start until the coroutine itself passes control
    # back to the event loop, so the 'finished' print statement will actually run before the inner function
    print("Finished wrapper2 function.")


asyncio.run(wrapper2())


# The await keyword can also be used to ensure that created tasks finish running before code continues, similar to
# .join() from multiprocessing/concurrent.futures

async def fetch_data():  # returns data after 1 second
    await asyncio.sleep(1)
    return {'data': 1}


async def print_numbers():  # prints 1 number incrementally every 0.25 seconds for 1.5 seconds
    for i in range(6):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())  # 2 tasks are made so that the functions run asynchronously
    task2 = asyncio.create_task(print_numbers())
    value = await task1  # await is used to make sure that the return value is ready before it is printed
    print(value)
    await task2  # await is used to make sure that the second coroutine is finished


asyncio.run(main())

# ---[USING A QUEUE]---
# Using a queue is illustrated below with a simulation of producers and consumers; the producers create a 'product'
# (a random hex) and consumers recieve those 'products', both adding and drawing from the same queue. Once you
# understand the purpose of each function the important thing to note is how the queue functions syntax wise (very
# similar to the queue from multiprocessing).

import os


async def makeitem(size=5):  # Makes a random 'product' (hex value)
    return os.urandom(size).hex()


async def randsleep(caller):  # self explanitory, sleeps for a random number of seconds
    sleep_time = random.randint(0, 3)
    print(f"{caller} sleeping for {sleep_time} seconds.")
    await asyncio.sleep(sleep_time)


async def produce(name, queue):  # produces a random number of
    num = random.randint(0, 5)  # how many producers are made
    for _ in itertools.repeat(None, num):  # loops to create multiple producers
        await randsleep(caller=f"Producer {name}")
        item = await makeitem()  # new item is made, and another producer is started while it is made
        await queue.put((item))  # queue syntax is similar to multiprocessing
        print(f"[NEW ITEM] Producer {name} added <{item}> to queue.")


async def consume(name, queue):
    while True:  # continuously checks for new products
        await randsleep(caller=f"Consumer {name}")  # consumer only checks the queue once every couple of seconds
        item = await queue.get()  # Consumer obtains product from the queue (if it exists)
        print(f"[ITEM BOUGHT] Consumer {name} got element <{item}>")
        queue.task_done()  # is used to support queue.join()


async def main(number_of_producers, number_of_consumers):
    queue = asyncio.Queue()  # instantiate new queue
    producers = [asyncio.create_task(produce(name, queue)) for name in
                 range(number_of_producers)]
    consumers = [asyncio.create_task(consume(name, queue)) for name in range(number_of_consumers)]  # same here
    await asyncio.gather(*producers)  # gathers and runs all producers
    await queue.join()  # Awaits consumers and producers to finish
    for consumer in consumers:  # once the producers and consumers have finished, consumer proccesses are cancelled
        consumer.cancel()


start = time.perf_counter()
asyncio.run(main(3, 5))  # runs the function asynchronously
elapsed = time.perf_counter() - start
print(f"Program completed in {elapsed:0.5f} seconds.")

# <NUMPY>
print("\n\n\n\n\nNUMPY")
# NumPy, Numper Python, is a C based module that allows for faster mathematical / array processing; it is the base
# for not only other data science modules but data science itself in python.
# NOTE THAT THIS IS A SHALLOW VIEW OF NUMPY AND FOR MORE ADVANCED FUNCTIONALITY YOU SHOULD REFER TO THE FULL
# DOCUMENTATION HERE https://numpy.org/
import numpy

# :Array Basics:
print("\n:Array Basics:")

array1 = numpy.array([1, 2, 3])  # arrays are instantiated with numpy.array
array2 = numpy.array([[4, 5, 6], [7, 8, 9]])  # 2d/3d etc. arrays are also possible
print(f"Array1 dimension : {array1.ndim}. Array2 dimension : {array2.ndim}.")  # how many dimensions the array has
print(f"Array1 size : {array1.size}. Array2 size : {array2.size}.")  # number of elements in the array
print(f"Array1 shape : {array1.shape}. Array2 shape : {array2.shape}.")  # returns dimensions (height, width, etc.) of
# the array as a tuple

int16, floats = numpy.array([1, 2, 3], dtype="int16"), numpy.array([1, 2, 3], dtype="float")  # datatypes can
# be defined with the dtype parameter and checked with the dtype attribute shown below
print(f"Int16 array datatype : {int16.dtype}. Float array datatype : {floats.dtype}")
print(f"Int16 array item size and total size : {int16.itemsize}, {int16.nbytes}. Float array item size and"
      f"total size : {floats.itemsize}, {floats.nbytes}")  # itemsize returns the amount of memory each item takes up,
# while nbytes returns the amount of memeory the whole array takes up (both returned in bytes)

# :Slicing and Indexing:
print("\n:Slicing and Indexing:")

array3 = numpy.array([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10]])
print(f"[0, 1] : {array3[0, 1]}. [1, 3] : {array3[1, 3]}")  # [row, column] is the most common array indexing format
print(f"[1, -2] : {array3[1, -2]}")  # negative indexing also works
print(f"[0, ::-1] : {array3[0, ::-1]}. [1, 2::2] : {array3[1, 2::2]}")  # list splicing also works as normal
print(f"[1, :] : {array3[1, :]}. [:, 2] : {array3[:, 2]}")  # remember that : means all which can be used to get full
# row or column
array3[0, 4] = 10  # values can be changes as usual
print(array3)
array3[:, 0] = 10  # values changing can use list splicing
array3[:, 2] = 25, 30  # they can be spliced and set as values individually
print(array3)
# Note that for arrays with more dimensions, the indices are input from largest to lowerst scope
array4 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array4[[1, 2, 8]])  # you can also index with another list, this is expanded on in :Conditionals:

# :Instantiating Arrays:
print("\n:Instantiating Arrays:")

zeros = numpy.zeros(5)  # creates an array of all zeros
threeD_zeros = numpy.zeros((2, 2, 3), dtype="int16")  # additional elements will be the length of the next dimension
# (make sure to input dimensions in a tuple). you can also specify datatype
threeD_ones = numpy.zeros((2, 2, 3), dtype="int16")  # same can be done with ones, not going to print this cause its the
# same thing
threeD_num = numpy.full((2, 2, 3), 3.1415, dtype="float32")  # full does the same but takes a parameter for what number
# you want to use; also not going to print this one
threeD_copy = numpy.full_like(threeD_zeros, 5, dtype="int16")  # other arrays are taken as size parameters w/ full_like
print(zeros)
print(threeD_zeros)

random_array = numpy.random.rand(2, 3)  # prints a random array of floats given a size
print(random_array)
print(numpy.random.random_sample(random_array.shape))  # random_sample is used if you want to use another
# array as a size parameter (in this instance you need to use the array's .shape attribute)
print(numpy.random.randint(5, 10, size=(2, 3)))  # since you can't input the desired datatype, randint is used to
# generate integers; the first two numbers are the range (0-param if only 1 is given) and the size is self explanitory
print(numpy.identity(3))  # an identity matrix takes 1 parameter and forms a matrix of (param x param) size, where the
# main diagonal (top left -> bottom right) is comprised of ones and all else is a zero.
array = numpy.array([[1, 2, 3]])  # array stored within another array to make the 0th axis the vertical axis
print(numpy.repeat(array, repeats=3, axis=0))  # repeat an array (repeat) times along the (axis)th axis

# :Mathematical Operations:
print("\n:Mathematical Operations:")
array5 = numpy.array([1, 2, 3, 4])
print(array5 + 2)  # using numpy, mathematical operations can be performed directly on the array
print(array5 * 2)  # map is not necessary
array6 = numpy.array([1, 0, 1, 0])
print(array5 + array6)  # you can also perform mathematical operations with two arrays
print(array5 * numpy.array([num + 1 for num in range(4)]))  # comprehensions can be used as well

# IMPORTANT RESOURCE : OTHER MATHEMATICAL ROUTINES ARE DOCUMENTED IN THIS LINK:
# https://numpy.org/doc/stable/reference/routines.math.html

# :Statistics:
print("\n:Statistics:")
array7 = numpy.array([[3, 1, 5],
                      [4, 2, 6]])
print(f"Array6 minimum : {numpy.min(array7)}. Array6 maximum : {numpy.max(array7)}.")  # self explanitory, smallest and
# largest value. Note that the axes on which you want to operate can be defined by the axis= parameter for almost all
# statistical analyses.
print(f"Array 6 minimum and maximums by row : {numpy.min(array7, axis=0)}, {numpy.max(array7, axis=1)}")
print(f"Array6 sum, Array6 sum by row, Array6 sum by column : {numpy.sum(array7)}, {numpy.sum(array7, axis=1)}, "
      f"{numpy.sum(array7, axis=0)}.")  # self explanitory
array8 = [2, 4, 8, 14, 22, 34]
print(f"Array7's mean/median : {numpy.average(array8)}/{numpy.median(array8)}.")  # self explanitory
print(f"Array7's standard deviation / variance : {numpy.std(array8)}, {numpy.var(array8)}")  # standard deviation is
# self explanitory, variance is the squared expected deviation

# IMPORTANT RESOURCE : OTHER STATISTICAL ROUTINES ARE DOCUMENTED IN THIS LINK:
# https://numpy.org/doc/stable/reference/routines.statistics.html

#:Regoranization:
print("\n:Reorganization:")
stack1 = numpy.array([[1, 2], [3, 4]])
stack2 = numpy.array([[5, 6], [7, 8]])
array9 = numpy.vstack([stack1, stack2])  # vstack (vertical stack) stacks arrays on top of each other
print(array9)
print(numpy.hstack([stack1, stack2]))  # hstack (horizontal stack) does the same but stacks horizontally
print(array9.reshape(2, 2, 2))  # reshape can be used to change the structure of an array

# :Conditionals:
print("\n:Conditionals:")
nums = numpy.array([1, 13, 21, 11, 196, 3, 298, 34, 6, 98, 123, 154])
print(nums)
print(nums > 50)  # conditionals in numpy will return a list of all elements where the conditional is true
print(nums[nums > 50])  # in numpy you can index with another list, so this can be used to generate a new list where
# only values that fill a preducate are used
print((nums > 50) & (nums < 100))  # numpy uses the '&' instead of 'and' when chaining conditionals
print(~(nums < 100))  # the '~' symbol is equivalent to 'not'
print(nums[~(nums < 100) & (nums < 200)])  # when chaining conditionals, they must be within parenthesis
