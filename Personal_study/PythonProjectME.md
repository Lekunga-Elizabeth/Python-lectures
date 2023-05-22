Python Indentation:
- Indentation refers to the spaces at the beginning of a code line.
- Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
- Python uses indentation to indicate a block of code.

Python Variables
- Variables are containers for storing data values.
- In Python, variables are created when you assign a value to it:
- for example, x = 5 where '5' is the value assign to the varialbe 'x'
- Python has no command for declaring a variable.
- The variable name cannot start wit a number and it is alway writtin using underscore in place of space. 
- For example of line 10. don"t do this '2my-name-first' instead do 'my_name_first'

Variable Names
- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

Multi Words Variable Names
- Variable names with more than one word can be difficult to read.
- There are several techniques you can use to make them more readable:

1. Camel Case
- Each word, except the first, starts with a capital letter:
- myVariableName = "John"

2. Pascal Case
- Each word starts with a capital letter:
- MyVariableName = "John"

3. Snake Case
- Each word is separated by an underscore character:
- my_variable_name = "John"
- This method is the most frequently used method 

Unpack a Collection
- If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

Comments in Python 
- Python has commenting capability for the purpose of in-code documentation.
- Comments start with a #, and Python will render the rest of the line as a comment:
- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.
- if you whant to comment multiline strings use the multiline comment which is """ instead of the single line comment of #
- Comments can be placed at the end of a line, and Python will ignore the rest of the line: eg. print("Hello, World!") #This is a comment
- A comment does not only  have to be text a that explains the code, but it can also be used to prevent Python from executing the code:

Multiline Comments
- Python does not really have a syntax for multiline comments.
- To add a multiline comment you could insert a # for each line or you can use a multiline string.
- Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
- example of multiline strings for commenting 
"""
This is a comment
written in
more than just one line
"""

Casting
- If you want to specify the data type of a variable, this can be done with casting.

Get the Data Type
- You can get the data type of a variable with the type() function.

Single or Double Quotes?
- String variables can be declared either by using single or double quotes: example
x = "John"
# is the same as
x = 'John'

Case-Sensitive
- Variable names are case-sensitive.
Example
This will create two variables:
a = 4
A = "Sally"
#A will not overwrite a

Output Variables
- The Python print() function is often used to output variables.

Global Variables
- Variables that are created outside of a function (as in all of the examples above) are known as global variables.
- Global variables can be used by everyone, both inside of functions and outside.


Python Data Types
1. Built-in Data Types
- In programming, data type is an important concept.
- Variables can store data of different types, and different types can do different things.
- Python has the following data types built-in by default, in these categories:

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

Getting the Data Type
- You can get the data type of any object by using the type() function:
Use the image below to see the result you get 