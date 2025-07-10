# AUTOMATE THE BORING STUFF WITH PYTHON By `Al Sweigart`
- [Introduction](#introduction)
- [Chapter 1: Python Basics](#chapter-1-python-basics)
- [Chapter 2: Flow Control](#chapter-2-flow-control)
- [Chapter 3: Functions](#chapter-3-functions)
- [Chapter 4: Lists](#chapter-4-lists)
- [Chapter 5: Dictionaries and Structuring Data](#chapter-5-dictionaries-and-structuring-data)
- [Chapter 6: Manipulating Strings](#chapter-6-manipulating-strings)
- [Chapter 7: Pattern Matching with Regular Expressions](#chapter-7-pattern-matching-with-regular-expressions)
- [Chapter 8: Reading and Writing Files](#chapter-8-reading-and-writing-files)
- [Chapter 9: Organizing Files](#chapter-9-organizing-files)
- [Chapter 10: Debugging](#chapter-10-debugging)
- [Chapter 11: Web Scraping](#chapter-11-web-scraping)
- [Chapter 12: Working with Excel Spreadsheets](#chapter-12-working-with-excel-spreadsheets)
- [Chapter 13: Working with PDF and Word Documents](#chapter-13-working-with-pdf-and-word-documents)
- [Chapter 14: Working with CSV Files and JSON Data](#chapter-14-working-with-csv-files-and-json-data)
- [Chapter 15: Keeping Time, Scheduling Tasks, and Launching Programs](#chapter-15-keeping-time-scheduling-tasks-and-launching-programs)
- [Chapter 16: Sending Email and Text Messages](#chapter-16-sending-email-and-text-messages)
- [Chapter 17: Manipulating Images](#chapter-17-manipulating-images)
- [Chapter 18: Controlling the Keyboard and Mouse with GUI Automation](#chapter-18-controlling-the-keyboard-and-mouse-with-gui-automation)

# Introduction
**Programming** is the act of entering instructions for the computer to perform.<br>
**Source code** is programming instructions.<br>
**Python** refers to the *Python programming language* and the *Python interpreter software* that reads source code and performs its instructions.
The name Python comes from the surreal British comedy group **Monty Python**.<br>
Python programmers are affectionately called **Pythonistas**.

**Debugging programs** refers to finding and fixing errors.<br>
**The more you program, the better you'll become**.<br>
**Interactive shell** lets you type instructions for the Python interpreter software to run.
A **shell** is a program that lets you type instructions into the computer.

#### Asking smart programming questions
- Explain what you are trying to do, not just what you did. This lets your helper know if you are on the wrong track.
- Specify the point at which the error happens. Does it occur at the very start of the program or only after you do a certain action?
- Copy and paste the entire error message and your code to [pastebin](http://pastebin.com/) or [gist-github](http://gist.github.com/).
- Explain what you've already tried to do to solve your problem.                 
- List the version of Python you're using, and which operating system and version you're running.
- If the error came up after you made a change to your code, explain exactly what you changed.

# Chapter 1: Python Basics
The Python programming language has a wide range of **syntactical constructions**, **standard library functions**, and **interactive development environment** features.

**Expression** consists of *values* and *operators*, and they can always *evaluate* down to a single value.

**Math operators from highest to lowest precedence**
| Operator | Operation |
|------|----|
| ** | Exponent |
| % | Modulus/remainder |
| // | Integer division/floored quotient |
| / | Division |
| * | Multiplication |
| - | Subtraction |
| + | Addition |

The `**` operator is evaluated first; the `*`, `/`, `//`, and `%` operators are evaluated next, from left to right; and the `+` and `-` operators are evaluated. Parentheses can be used to override the usual precedence if needed.

### Data types
A **data type** is a category for values, and every value belongs to exactly one data type.
- **integer(int)** data type indicates values that are whole number.
- **floating-point numbers(floats)** are numbers with a decimal point.
- **strings(str)** are text values and should always be surrounded in single(' ') or double(" ") quotes.
- You can have a string with no characters in it, ' ', called a **blank string**.

When it operates on two integers or floats, + is the addition operator. 
When + is used on two string values, it joins the strings as the **string concatenation** operator.<br>
The * operator can be used with only two numeric values for multiplication or one string value and one integer value for **string replication**.

A **variable** can be used to store a single values.
An **assignment statement** consists of a variable name, an equal sign, called the assignment operator, and the value to be stored.<br>
A variable is *initialised* the first time a value is stored in it. When a variable is assigned a new value, the old value is forgotten, called *overwriting* the variable.
variable names can be anything but must follow these 3 rules:
1. It can only be one word.
2. It can use only letters, numbers, and the underscore(_) character,
3. It cannot begin with a number.

Variable names are case-sensitive.<br>
A good variable name describes the data it contains.

**Comments** are ignored by Python, and can be used to write notes or comment out code. The hash mark(#) can be used for a single line comment, and three quotes(''' ''') can be used for multi-line comments.

The `print()` function displays the value inside the parentheses on the screen.
A value that is passed to a function call is an **argument**.<br>
When writing a function name, the opening and closing parenthesis at the end identify it as the name of a function.

The `input()` function waits for the user to type some text on the keyboard and press ENTER. It evaluates to a string equal to the user's text. 

The `len()` function can be passed a string value or a variable containing a string and it evaluates to the integer value of the number of characters in that string.

The `str()`, `int()` and `float()` functions will evaluate to the string, integer and floating-point forms of the value passed, respectively.


## Chapter 2: Flow Control
**Flow control statements** can decide which Python instructions to execute under which conditions.

**Boolean** data type has only two values: `True` and `False`.
Boolean values are used in expressions and can be stored in variables.
Boolean is capitalised because the data type is named after mathematician **George Boole**.

**Comparison operators** compare two values and evaluate down to a single Boolean value.
| Operator | Meaning |
|------|-------|
| == | Equal to |
| != | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

These operators evaluate to True or False depending on the values passed.
The <, >, <= and >= operators work properly only with integer and floating-point values.
> The == operator (equal to) asks whether two values are the same as each other.
> The = operator (assignment) puts the value on the right into the variable on the left.

**Boolean operators** (`and`, `or` and `not`) are used to compare Boolean values. They evaluate the expressions down to a Boolean value.<br>
The *and* and *or* operators take two Boolean values or expressions, so they are considered *binary* operators.
The and operator evaluates an expression to True if *both* Booleans values are True; otherwise, it evaluates to False.<br>
The or operator evaluates an expression to true if either of the two Boolean values is True. If both are false, it evaluates to false.
The not operator evaluates to the opposite Boolean value, and it can be nested.

Comparison operators can be used in expressions with Boolean operators.
After any math and comparison operator evaluate, Python evaluates the not operators first, then the and operators, and then the or operators.

### Elements of flow control
Flow control statements often start with a part called the **conditional**, and all are followed by a block of code called the **clause**.
**Condition** is a more specific name in the context of flow control statements. Boolean expressions could be considered conditions, which are the same thing as expressions.
A flow control statement decides what to do based on whether its condition is True or False.

Lines of Python code can be grouped together in *blocks*, which can be distinguished by the indentation. Rules for blocks:
1. Blocks begin when the indentation increases.
2. Blocks can contain other blocks.
3. Blocks end when the indentation decreases to zero or to a containing block's indentation.
> The program execution is a term for the current instruction being executed.

### if Statements
An **if** statement's clause will execute if the statement's condition is *True*. The clause is skipped if the condition is *False*. In Python, an if statement consists of the following:
- The if keyword
- A condition
- A colon
- starting on the next line, an indented block of code -**if clause**

### else Statements
An if statement can optionally be followed by an **else** statement. The else clause is executed only when the if statement's condition is False. An else statement does not have a condition, and in Python an else statement always consists of:
- The else keyword
- A colon
- Starting on the next line, an indented block of code -**else clause**

### elif Statements
The **elif** statement is an "else if" statement that always follows an if or another elif statement. It provides another condition that is checked only if any of the previous conditions were False. In code, an elif statement always consists of the following:
- An elif keyword
- A condition
- A colon
- starting on the next line, an indented block of code -**elif clause**

When there is a chain of elif statements, only one or none of the clauses will be executed. Once one of the statements' condition is found to be True, the rest of the elif clauses are automatically skipped.

### while Loop Statements
A **while** statement is used to make a block of code execute over and over again. The code in a while clause will be executed as long as the while statement's condition is True. In code, a while statement always consists of:
- The while keyword
- A condition
- Starting on the next line, an indented block of code -**while clause**

The while clause is often called the *while loop* or just the *loop*. In a while loop, the condition is always checked at the start of each iteration.

### break Statements
If the execution of program reaches a **break** statement, it immediately exits the while loop's clause. In code, a break statement simply contains the `break` keyword.

### continue Statements
When the program execution reaches a `continue` statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop's condition.
> CTRL-C sends a KeyboardInterrupt error to a program and cause it to stop immediately.

> When used in conditions, 0, 0.0 and '' are considered False, while all other values are considered True.

### for Loops and the range() Function
A **for** loop executes a block of code only a certain number of times. In code, a for loop statement includes:
- The for keyword
- A variable name
- The in keyword
- A call to the `range()` method with up to three integers passed to it
- A colon
- Starting on the next line, an indented block of code -**for clause**
> You can use continue and break statements only inside while and for loops.

### The starting, Stopping and Stepping arguments to range()
The range() function can be called with multiple arguments separated by a comma. this lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.<br>
The first argument will be where the for loop's variable starts, and the second argument will be up to, but not including, the number to stop at.

The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the *step argument*. The step is the amount that the variable is increased by after each iteration.
Negative number can be used for the step argument to make the for loop count down instead of up.

### importing Modules
All python programs can call a basic set of functions called *built-in functions*.
Python also comes with a set of modules called the *standard library*. Each module is a python program that contains a related group of functions that can be embedded in programs. 

Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:
- The import keyword
- the name of the module
- optionally, more module names, as long as they are separated by commas

An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star *. with this form of import statement, calls to functions will not need the function module prefix.

A program can be caused to terminate by calling the `sys.exit()` function.

## Chapter 3: Functions
A function is like a mini-program within a program.

## Chapter 4: Lists

## Chapter 5: Dictionaries and Structuring Data

## Chapter 6: Manipulating Strings

## Chapter 7: Pattern Matching with Regular Expressions

## Chapter 8: Reading and Writing Files

## Chapter 9: Organizing Files

## Chapter 10: Debugging

## Chapter 11: Web Scraping

## Chapter 12: Working with Excel Spreadsheets

## Chapter 13: Working with PDF and Word Documents

## Chapter 14: Working with CSV Files and JSON Data

## Chapter 15: Keeping Time, Scheduling Tasks, and Launching Programs

## Chapter 16: Sending Email and Text Messages

## Chapter 17: Manipulating Images

## Chapter 18: Controlling the Keyboard and Mouse with GUI Automation