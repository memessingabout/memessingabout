---

# AUTOMATE THE BORING STUFF WITH PYTHON  
*By Al Sweigart*

<details>
<summary>Table of Contents</summary>

- [Introduction](#introduction)
- [Part I: Python Programming Basics](#part-i-python-programming-basics)
  - [Chapter 1: Python Basics](#chapter-1-python-basics)
  - [Chapter 2: Flow Control](#chapter-2-flow-control)
  - [Chapter 3: Functions](#chapter-3-functions)
  - [Chapter 4: Lists](#chapter-4-lists)
  - [Chapter 5: Dictionaries and Structuring Data](#chapter-5-dictionaries-and-structuring-data)
  - [Chapter 6: Manipulating Strings](#chapter-6-manipulating-strings)
- [Part II: Automating Tasks](#part-ii-automating-tasks)
  - [Chapter 7: Pattern Matching with Regular Expressions](#chapter-7-pattern-matching-with-regular-expressions)
  - [Chapter 8: Reading and Writing Files](#chapter-8-reading-and-writing-files)
  - [Chapter 9: Organizing Files](#chapter-9-organizing-files)
  - [Chapter 10: Debugging](#chapter-10-debugging)
  - [Chapter 11: Web Scraping](#chapter-11-web-scrapping)
  - [Chapter 12: Working with Excel Spreadsheets](#chapter-12-working-with-excel-spreadsheets)
  - [Chapter 13: Working with PDF and Word Documents](#chapter-13-working-with-pdf-and-word-documents)
  - [Chapter 14: Working with CSV Files and JSON Data](#chapter-14-working-with-csv-files-and-json-data)
  - [Chapter 15: Keeping Time, Scheduling Tasks, and Launching Programs](#chapter-15-keeping-time-scheduling-tasks-and-launching-programs)
  - [Chapter 16: Sending Email and Text Messages](#chapter-16-sending-email-and-text-messages)
  - [Chapter 17: Manipulating Images](#chapter-17-manipulating-images)
  - [Chapter 18: Controlling the Keyboard and Mouse with GUI Automation](#chapter-18-controlling-the-keyboard-and-mouse-with-gui-automation)
</details>

---

## Introduction  
**Programming** is the act of entering instructions for the computer to perform.  
**Source code** consists of programming instructions.  
**Python** refers to the *Python programming language* and the *Python interpreter software* that reads source code and executes its instructions. The name Python comes from the surreal British comedy group **Monty Python**. Python programmers are affectionately called **Pythonistas**.  

**Debugging programs** involves finding and fixing errors.  
**The more you program, the better you'll become**.  
**Interactive shell** allows you to type instructions for the Python interpreter to execute. A **shell** is a program that lets you interact with the computer by entering commands.  

### Asking Smart Programming Questions  
- Explain your goal, not just your actions. This helps others understand if you're on the right track.  
- Specify where the error occurs—whether at the start of the program or after a specific action.  
- Share the entire error message and your code using tools like [Pastebin](http://pastebin.com/) or [GitHub Gist](http://gist.github.com/).  
- Describe what you've already tried to resolve the issue.  
- Mention your Python version, operating system, and its version.  
- If the error followed a code change, detail exactly what you modified.  

---

## Part I: Python Programming Basics  

### Chapter 1: Python Basics  
Python features a wide range of **syntactical constructions**, **standard library functions**, and **interactive development tools**.  

**Expressions** consist of *values* and *operators*, evaluating to a single value.  

#### Math Operators (Precedence from Highest to Lowest)  
| Operator | Operation        | Example   | Result |  
|----------|-----------------|-----------|--------|  
| `**`     | Exponent        | `2 ** 3`  | `8`    |  
| `%`      | Modulus         | `22 % 8`  | `6`    |  
| `//`     | Integer Division| `22 // 8` | `2`    |  
| `/`      | Division        | `22 / 8`  | `2.75` |  
| `*`      | Multiplication  | `3 * 5`   | `15`   |  
| `-`      | Subtraction     | `5 - 2`   | `3`    |  
| `+`      | Addition        | `2 + 2`   | `4`    |  

Parentheses override precedence when needed.  

#### Data Types  
- **Integer (`int`)**: Whole numbers.  
- **Floating-point (`float`)**: Numbers with decimal points.  
- **String (`str`)**: Text, enclosed in single (`' '`) or double (`" "`) quotes.  
  - A **blank string** contains no characters (`''`).  

The `+` operator concatenates strings, while `*` replicates strings when combined with an integer.  

#### Variables  
- Store single values.  
- **Rules for naming**:  
  1. Must be one word.  
  2. Can use letters, numbers, and underscores (`_`).  
  3. Cannot start with a number.  
- Names are case-sensitive.  

#### Functions  
- `print()`: Displays values.  
- `input()`: Reads user input (returns a string).  
- `len()`: Returns the length of a string.  
- `str()`, `int()`, `float()`: Convert values to strings, integers, or floats.  

---

### Chapter 2: Flow Control  
**Flow control statements** determine which instructions execute under specific conditions.  

#### Boolean Values  
- `True` or `False`.  
- **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`.  
- **Boolean Operators**: `and`, `or`, `not`.  

#### Conditional Statements  
- **`if`**: Executes a block if the condition is `True`.  
- **`else`**: Executes if the `if` condition is `False`.  
- **`elif`**: Checks additional conditions if prior ones are `False`.  

#### Loops  
- **`while`**: Repeats a block while the condition is `True`.  
- **`for`**: Iterates over a sequence (e.g., `range()`).  
- **`break`**: Exits the loop immediately.  
- **`continue`**: Skips to the next iteration.  

#### Modules  
- Use `import` to include modules (e.g., `sys` for `sys.exit()`).  

---

### Chapter 3: Functions  
**Functions** are reusable blocks of code.  
- Defined with `def`.  
- **Parameters**: Variables that store arguments.  
- **Return values**: Results of a function (use `return`).  
- **Scope**: Local vs. global variables.  

#### Exception Handling  
- Use `try` and `except` to manage errors.  

---

### Chapter 4: Lists  
**Lists** store ordered sequences of values.  
- **Indexing**: Starts at `0`.  
- **Slicing**: Extract sublists with `[start:end]`.  
- **Methods**:  
  - `append()`, `insert()`: Add items.  
  - `remove()`, `pop()`: Remove items.  
  - `sort()`, `reverse()`: Reorder items.  

#### Tuples  
- Immutable sequences, defined with parentheses.  

---

### Chapter 5: Dictionaries  
**Dictionaries** store key-value pairs.  
- **Methods**:  
  - `keys()`, `values()`, `items()`: Retrieve keys, values, or pairs.  
  - `get()`: Safely access values.  
  - `setdefault()`: Set a default value for a key.  

---

## Part II: Automating Tasks  
*(Chapters 6–18 remain as in the original document.)*  

---

<sup>Made with ❤️ by **Emillio**</sup><br>  
<sup>**Love all, trust none.**</sup>  

---