### Python Learning Roadmap for Computer Science
### Roadmap Overview


| Phase | Topics | Duration |
|-------|--------|----------|
| Foundations | - History \n - setup, - variables, - data types, - operators, - control flow, - loops, - functions, - basic data structures (lists, tuples, dictionaries, sets), and - file I/O. | Weeks 1–4, 20 days |
| Intermediate Concepts | Modules, packages, error handling, advanced data structures (stacks, queues, linked lists), regular expressions, and working with libraries (e.g., math, datetime).  | Weeks 5–8, 20 days |
| Object-Oriented Programming (OOP) & Design | Classes, objects, inheritance, polymorphism, encapsulation, design patterns, and basic testing (unit tests). | Weeks 9–12, 20 days |
| Advanced Topics | Decorators, generators, iterators, context managers, concurrency (threading, multiprocessing, asyncio), web scraping, APIs, databases (SQL with SQLite), and data analysis (pandas, NumPy). | Weeks 13–18, 30 days |
| Professional Development & Projects | Building a portfolio project (e.g., web app, data pipeline, or automation script), version control (Git), deployment, CI/CD basics, Python frameworks (Flask/Django), and career guidance (software engineering, data science, DevOps)  | Weeks 19–24, 30 days |


#### Tests
- **Test 1**: Week 2, Saturday – Basics (syntax, control flow, functions).
- **Test 2**: Week 4, Saturday – Data structures and file handling.
- **Test 3**: Week 6, Saturday – Modules, packages, and error handling.
- **Test 4**: Week 8, Saturday – Advanced data structures and library usage.
- **Test 5**: Week 10, Saturday – OOP basics and inheritance.
- **Test 6**: Week 12, Saturday – Advanced OOP and design patterns.
- **Test 7**: Week 14, Saturday – Decorators, generators, and iterators.
- **Test 8**: Week 16, Saturday – Concurrency and web scraping.
- **Test 9**: Week 18, Saturday – Databases and data analysis.
- **Test 10**: Week 20, Saturday – Project design and Git.
- **Final Project & Test**: Week 24, Saturday – Complete a capstone project and comprehensive exam.

---

### Daily Structure
- **10 minutes**: Conceptual overview of the day’s topic.
- **30 minutes**: Code examples and guided practice.
- **15 minutes**: Hands-on exercise or mini-project.
- **5 minutes**: Summary and preview of the next topic.
- **Homework**: Short coding tasks to reinforce the day’s learning (15–30 minutes).

---

### Day 1: History of Pyton
Python was created by **Guido van Rossum** in the late 1980s, with the first release (Python 0.9.0) in **February 1991**. The language was inspired by ABC, a language Guido worked on, but designed to be more practical and extensible. The name “Python” comes from Monty Python’s Flying Circus, reflecting Guido’s preference for a lighthearted name.

**Key Milestones**:
- **Python 1.0 (1994)**: Introduced basic features like lambda, map, filter, and reduce.
- **Python 2.0 (2000)**: Added list comprehensions, garbage collection, and Unicode support.
- **Python 3.0 (2008)**: A major overhaul to fix design flaws, introducing breaking changes (e.g., print as a function, not a statement). Python 2 was phased out in 2020.
- **Modern Python (2025)**: Python 3.12 and 3.13 are widely used, with improvements in performance (faster CPython), type hints, and pattern matching.

**Philosophy (The Zen of Python)**:
Run `import this` in Python to see the guiding principles, emphasizing readability, simplicity, and explicitness. Key tenets:
- “Simple is better than complex.”
- “Readability counts.”
- “There should be one—and preferably only one—obvious way to do it.”

**Why Python?**
- **Versatility**: Used in web development (Django, Flask), data science (pandas, NumPy), AI/ML (TensorFlow, PyTorch), automation, and more.
- **Ease of Learning**: Clean syntax resembling pseudocode.
- **Community**: Vast ecosystem of libraries and active support.
- **Career Relevance**: High demand in software engineering, data science, and DevOps.

#### Explicit and implicit

- **Explicit**: Code clearly states what it does, with no hidden or assumed behavior. It prioritizes readability and transparency, making the intent obvious to anyone reading the code.
- **Implicit**: Code relies on assumptions or hidden behaviors that are not immediately clear from reading it. This can make code harder to understand or maintain, as the reader must know the underlying rules or context.

The Zen of Python emphasizes explicitness to ensure code is maintainable, especially in collaborative or long-term projects. However, implicit behaviors exist in Python and can be useful when they align with common conventions.

---

### Examples in Python

#### 1. Explicit vs. Implicit in Variable Declaration
- **Explicit**: You clearly define the type or purpose of a variable.
  ```python
  # Explicit: Using type hints to clarify the expected type
  age: int = 25
  name: str = "Alice"
  ```
  Here, the type hints (`: int`, `: str`) make it clear what kind of data is expected, improving readability.

- **Implicit**: Python’s dynamic typing allows variables without explicit type declaration.
  ```python
  # Implicit: Type is inferred at runtime
  age = 25  # Assumed to be an integer, but not stated
  name = "Alice"  # Assumed to be a string
  ```
  While concise, this relies on the reader inferring the type from context, which can be unclear in complex code.

#### 2. Explicit vs. Implicit in Function Behavior
- **Explicit**: Clearly state what a function does through documentation or explicit return statements.
  ```python
  def add_numbers(a: float, b: float) -> float:
      """Add two numbers and return their sum."""
      return a + b
  result = add_numbers(3.5, 4.2)  # Clear intent
  ```
  The function’s purpose, inputs, and output are explicitly defined with type hints and docstring.

- **Implicit**: Rely on Python’s default behaviors without clarification.
  ```python
  def add(a, b):
      return a + b
  result = add(3, 4)  # Works for numbers, strings, or lists, but intent is unclear
  ```
  This function implicitly handles multiple types (numbers, strings, etc.) via Python’s operator overloading, but the lack of documentation or type hints makes its purpose ambiguous.

#### 3. Explicit vs. Implicit in Imports
- **Explicit**: Import only what you need and use clear names.
  ```python
  from math import pi
  print(pi)  # Clearly using math.pi
  ```
  The import explicitly brings in `pi`, and it’s obvious where it comes from.

- **Implicit**: Using wildcard imports that obscure the source of names.
  ```python
  from math import *
  print(pi)  # Works, but where does 'pi' come from?
  ```
  Wildcard imports implicitly bring in all names from the module, which can lead to naming conflicts or confusion in larger projects.

#### 4. Explicit vs. Implicit in Control Flow
- **Explicit**: Clearly state conditions or logic.
  ```python
  if user_input is None:
      print("No input provided.")
  ```
  The check for `None` is explicit, making the logic clear.

- **Implicit**: Rely on Python’s truthy/falsy behavior.
  ```python
  if user_input:
      print("Input provided.")
  ```
  This implicitly evaluates `user_input` as truthy or falsy (e.g., `None`, `0`, or empty strings are falsy). While concise, it may confuse readers unfamiliar with Python’s truth evaluation rules.

---

### Why “Explicit is Better Than Implicit”?
- **Readability**: Explicit code is easier to understand, especially for beginners or when revisiting code later.
- **Maintainability**: In professional settings, explicit code reduces bugs and makes collaboration smoother.
- **Debugging**: Explicit code makes it easier to spot errors, as behaviors aren’t hidden.
- **Scalability**: Large projects benefit from explicitness, as implicit assumptions can lead to conflicts or unexpected behavior.

However, **implicit behaviors** can be useful for:
- Conciseness in simple scripts or prototyping.
- Leveraging Python’s built-in conventions (e.g., truthy/falsy evaluations) when they’re widely understood.

---

### Practical Exercise (15 minutes)
To reinforce today’s learning, let’s apply explicit vs. implicit concepts to a small coding task:
1. Write two versions of a Python script that calculates the square of a number provided by the user:
   - **Explicit Version**: Use type hints, a docstring, and clear variable names.
   - **Implicit Version**: Rely on Python’s dynamic typing and minimal documentation.
2. Compare the two scripts and note which is easier to understand.

**Example Solution**:
- **Explicit**:
  ```python
  def square_number(number: float) -> float:
      """Calculate the square of a given number."""
      return number * number

  user_input: str = input("Enter a number to square: ")
  try:
      num: float = float(user_input)
      result: float = square_number(num)
      print(f"The square of {num} is {result}")
  except ValueError:
      print("Please enter a valid number.")
  ```

- **Implicit**:
  ```python
  def square(n):
      return n * n

  x = input("Enter a number: ")
  print(square(float(x)))
  ```
  Note: The implicit version assumes valid input and lacks error handling, making it less robust but shorter.

**Task**: Run both scripts, test with valid (e.g., `5`) and invalid (e.g., `abc`) inputs, and reflect on which version is clearer and more reliable.

---

### Summary & Tie to Python’s History
The principle of “Explicit is better than implicit” emerged from Python’s design goal to prioritize readability, a key reason for its popularity since Guido van Rossum’s early work. Explicit code aligns with Python’s use in professional domains like data science and web development, where clarity is critical. Implicit code, while sometimes convenient, can lead to errors in complex projects.

### Day 2: Setting Up a Python Development Environment

#### Objective
Learn how to set up a professional Python development environment, including an Integrated Development Environment (IDE), virtual environments, and best practices for organizing Python projects. This foundational step ensures you can write, debug, and manage Python code efficiently, preparing you for both learning and professional work.

---

#### Lecture (10 minutes)
A well-configured development environment is critical for writing Python code effectively. It streamlines coding, debugging, and dependency management, which are essential for professional workflows. Today, we’ll cover:
- **Integrated Development Environments (IDEs)**: Tools like VS Code, PyCharm, or IDLE that provide code editing, debugging, and project management features.
- **Virtual Environments**: Isolated spaces to manage dependencies for different projects.
- **Best Practices**: File organization, naming conventions, and basic project setup.

**Why This Matters**:
- IDEs improve productivity with features like autocompletion, linting, and integrated terminals.
- Virtual environments prevent dependency conflicts (e.g., different projects needing different versions of a library).
- Proper setup aligns with professional standards, making your code portable and maintainable.

**Tools We’ll Use**:
- **Python 3.12+**: Ensure it’s installed (from Day 1).
- **VS Code**: A lightweight, customizable IDE (PyCharm is an alternative for advanced users).
- **pip**: Python’s package manager, included with Python.
- **venv**: Python’s built-in module for virtual environments.

---

#### Code Examples & Guided Practice (30 minutes)

1. **Install and Configure VS Code**:
   - Download and install [VS Code](https://code.visualstudio.com/).
   - Install the **Python extension** (by Microsoft):
     - Open VS Code, go to Extensions (Ctrl+Shift+X or Cmd+Shift+X on Mac), search for “Python,” and install.
   - Set the Python interpreter:
     - Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
     - Type `Python: Select Interpreter` and choose your Python 3.12+ installation (run `python3 --version` in a terminal to confirm the path).

2. **Create a Virtual Environment**:
   - Open a terminal in VS Code (Terminal > New Terminal).
   - Create a project folder:
     ```bash
     mkdir python_learning
     cd python_learning
     ```
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On Mac/Linux: `source venv/bin/activate`
     - You’ll see `(venv)` in the terminal, indicating the environment is active.
   - Verify the isolated Python:
     ```bash
     python --version
     pip list  # Shows only basic packages (pip, setuptools)
     ```

3. **Install a Package**:
   - Install the `requests` library to test dependency management:
     ```bash
     pip install requests
     ```
   - Check installed packages:
     ```bash
     pip list  # Now includes requests
     ```

4. **Write and Run a Sample Script**:
   - Create a file `test_env.py` in VS Code:
     ```python
     import requests
     import sys

     print(f"Python version: {sys.version}")
     response = requests.get("https://api.github.com")
     print(f"GitHub API status: {response.status_code}")
     ```
   - Run the script:
     - In VS Code, click the “Run” button (triangle) or use the terminal: `python test_env.py`.
     - Expected output: Python version and HTTP status code (200 if successful).

5. **Project Structure Best Practices**:
   - Organize your project:
     ```
     python_learning/
     ├── venv/               # Virtual environment
     ├── scripts/            # Python scripts (e.g., test_env.py)
     ├── README.md           # Project description
     └── requirements.txt    # List of dependencies
     ```
   - Create `requirements.txt` to track dependencies:
     ```bash
     pip freeze > requirements.txt
     ```
   - View `requirements.txt`:
     ```
     requests==2.31.0
     # Other dependencies
     ```

---

#### Hands-On Exercise (15 minutes)
1. Set up a new project folder called `day2_project`.
2. Create and activate a virtual environment named `env`.
3. Install the `numpy` package (`pip install numpy`).
4. Write a script `matrix.py` that:
   - Imports `numpy`.
   - Creates a 2x2 matrix (e.g., `[[1, 2], [3, 4]]`).
   - Prints the matrix and its transpose.
   - Example:
     ```python
     import numpy as np
     matrix = np.array([[1, 2], [3, 4]])
     print("Original Matrix:\n", matrix)
     print("Transposed Matrix:\n", matrix.T)
     ```
5. Save the script, run it in VS Code, and verify the output.
6. Create a `requirements.txt` file for the project.

**Expected Output**:
```
Original Matrix:
 [[1 2]
  [3 4]]
Transposed Matrix:
 [[1 3]
  [2 4]]
```

---

#### Summary & Preview (5 minutes)
Today, you set up a professional Python development environment using VS Code, virtual environments, and best practices for project organization. This setup ensures you can manage dependencies and write clean, reproducible code—a critical skill for professional development. Tomorrow, we’ll explore **variables and data types**, diving into Python’s core building blocks.

#### Homework
- Create a new project folder with a virtual environment and install the `pandas` package.
- Write a script that imports `pandas`, creates a simple DataFrame (e.g., with names and ages), and prints it.
- Read about [virtual environments](https://docs.python.org/3/library/venv.html) (first two sections).
- Experiment with VS Code features (e.g., autocompletion, debugging) by modifying `test_env.py` to fetch and print data from another API (e.g., `https://api.openweathermap.org`).

---

### Day 3: Variables and Data Types in Python

#### Objective
Understand Python’s variables and core data types, including how to declare, use, and manipulate them. This foundational topic builds your ability to store and process data, a critical skill for programming. We’ll also reinforce the principle of explicitness from Day 1 and the development environment setup from Day 2.

---

#### Lecture (10 minutes)
In Python, **variables** are names that reference data stored in memory. Python is **dynamically typed**, meaning you don’t explicitly declare a variable’s type—it’s inferred at runtime. However, using clear variable names and optional type hints aligns with Python’s “explicit is better than implicit” philosophy.

**Core Data Types**:
- **Numeric**: `int` (e.g., `42`), `float` (e.g., `3.14`), `complex` (e.g., `3+4j`).
- **Strings**: `str` (e.g., `"Hello"`), used for text.
- **Boolean**: `bool` (e.g., `True`, `False`), used for logical operations.
- **NoneType**: `None`, representing the absence of a value.

**Key Concepts**:
- Variables are created when assigned a value (e.g., `x = 10`).
- Use descriptive names (e.g., `student_age` instead of `x`) for clarity.
- Type hints (e.g., `age: int = 25`) improve readability and catch errors in IDEs.
- Python’s built-in `type()` function checks a variable’s type.
- Variables can change types dynamically (e.g., `x = 10; x = "hello"`), but this should be used cautiously to maintain clarity.

**Why This Matters**:
Understandingქ

Understanding variables and data types is the foundation for all Python programming, from simple scripts to complex applications. In professional settings, clear variable naming and type usage ensure maintainable code.

---

#### Code Examples & Guided Practice (30 minutes)

1. **Variable Declaration and Naming**:
   - Create and name variables explicitly:
     ```python
     # Explicit variable names with type hints
     student_age: int = 20
     student_name: str = "Alice"
     is_enrolled: bool = True
     print(f"{student_name} is {student_age} years old. Enrolled: {is_enrolled}")
     ```
   - Run in your VS Code environment (from Day 2).

2. **Numeric Types**:
   - Work with `int` and `float`:
     ```python
     x: int = 10
     y: float = 3.14
     z: float = x + y  # Type coercion to float
     print(f"Sum: {z}, Type: {type(z)}")  # Output: Sum: 13.14, Type: <class 'float'>
     ```

3. **Strings**:
   - Manipulate strings:
     ```python
     greeting: str = "Hello"
     name: str = "World"
     message: str = greeting + ", " + name + "!"  # Concatenation
     print(message)  # Output: Hello, World!
     print(f"Uppercase: {message.upper()}")  # Output: Uppercase: HELLO, WORLD!
     ```

4. **Booleans and None**:
   - Use booleans and `None`:
     ```python
     is_active: bool = True
     no_value: None = None
     print(f"Active: {is_active}, Value: {no_value}")  # Output: Active: True, Value: None
     print(f"Is None falsy? {not no_value}")  # Output: Is None falsy? True
     ```

5. **Type Checking and Conversion**:
   - Check and convert types:
     ```python
     user_input: str = input("Enter a number: ")
     number: float = float(user_input)  # Convert string to float
     print(f"Type: {type(number)}, Value: {number * 2}")  # Doubles the input
     ```

---

#### Hands-On Exercise (15 minutes)
Create a script `data_types.py` in your `day2_project` folder (from Day 2) that:
1. Prompts the user for their name (string), age (integer), height in meters (float), and whether they are a student (boolean).
2. Stores these in appropriately named variables with type hints.
3. Prints a summary, including:
   - The user’s name in uppercase.
   - Their age doubled.
   - Their height in centimeters (height * 100).
   - Their student status.
4. Handles potential errors (e.g., non-numeric input for age or height).

**Example Solution**:
```python
def collect_user_info() -> None:
    """Collect and display user information with type hints."""
    try:
        name: str = input("Enter your name: ")
        age: int = int(input("Enter your age: "))
        height: float = float(input("Enter your height in meters: "))
        is_student: bool = input("Are you a student? (yes/no): ").lower() == "yes"
        
        print(f"Name: {name.upper()}")
        print(f"Age doubled: {age * 2}")
        print(f"Height in cm: {height * 100}")
        print(f"Student: {is_student}")
    except ValueError:
        print("Error: Please enter valid numeric values for age and height.")

collect_user_info()
```

**Task**:
- Run the script with valid inputs (e.g., “Alice”, “20”, “1.75”, “yes”).
- Test with invalid inputs (e.g., “abc” for age) to verify error handling.
- Check the output in VS Code’s terminal.

**Expected Output** (for valid inputs):
```
Enter your name: Alice
Enter your age: 20
Enter your height in meters: 1.75
Are you a student? (yes/no): yes
Name: ALICE
Age doubled: 40
Height in cm: 175.0
Student: True
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to declare and use variables with Python’s core data types (`int`, `float`, `str`, `bool`, `None`). You practiced explicit naming and type hints, aligning with Python’s philosophy, and used your development environment to run scripts. Tomorrow, we’ll cover **operators and expressions**, exploring how to manipulate data with arithmetic, comparison, and logical operations.

#### Homework
- Modify `data_types.py` to include:
  - A check if the user’s age is above 18 and print whether they are an adult.
  - A calculation of the user’s height in feet (height * 3.281).
- Experiment with type conversion errors:
  - Try converting a non-numeric string to an integer (e.g., `int("abc")`) and observe the `ValueError`.
- Read the [Python documentation on built-in types](https://docs.python.org/3/library/stdtypes.html) (sections on numeric types and strings, ~5 minutes).
- Reflect on how explicit type hints in today’s exercise improved code clarity compared to implicit typing.

---


### Day 4: Operators and Expressions in Python

#### Objective
Learn how to use Python’s operators to manipulate data and create expressions. This topic builds on Day 3’s variables and data types, enabling you to perform calculations, comparisons, and logical operations—essential for problem-solving and professional programming tasks.

---

#### Lecture (10 minutes)
**Operators** are symbols or keywords that perform operations on variables and values, creating **expressions** that evaluate to a result. Python’s operators are intuitive and align with its emphasis on readability, but explicit usage (e.g., clear variable names and avoiding ambiguous operations) enhances code clarity.

**Main Operator Categories**:
1. **Arithmetic Operators**: Perform mathematical operations.
   - `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulus), `**` (exponentiation).
2. **Comparison Operators**: Compare values, returning `True` or `False`.
   - `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`.
3. **Logical Operators**: Combine boolean expressions.
   - `and`, `or`, `not`.
4. **Assignment Operators**: Assign values to variables.
   - `=`, `+=`, `-=`, `*=`, `/=`, etc.
5. **Other Operators**:
   - Membership: `in`, `not in` (test if a value is in a sequence).
   - Identity: `is`, `is not` (test if objects are identical).

**Key Concepts**:
- **Precedence**: Operators have a defined order (e.g., `**` before `+`). Use parentheses `()` for explicit grouping.
- **Type Safety**: Ensure operands are compatible (e.g., adding a string and integer requires conversion).
- **Explicitness**: Use clear variable names and avoid overly complex expressions.

**Why This Matters**:
Operators are the building blocks of computation in Python, used in everything from data analysis to web development. Understanding them prepares you for control flow (Day 5) and professional coding practices.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code.

1. **Arithmetic Operators**:
   ```python
   # Basic calculations with type hints
   a: int = 10
   b: float = 3.5
   print(f"Addition: {a + b}")  # 13.5 (float)
   print(f"Floor Division: {a // b}")  # 2.0 (float)
   print(f"Exponentiation: {a ** 2}")  # 100
   print(f"Modulus: {a % 3}")  # 1
   ```

2. **Comparison Operators**:
   ```python
   x: int = 5
   y: int = 8
   print(f"Equal: {x == y}")  # False
   print(f"Greater or Equal: {x >= y}")  # False
   print(f"Less: {x < y}")  # True
   ```

3. **Logical Operators**:
   ```python
   is_adult: bool = True
   has_id: bool = False
   can_enter: bool = is_adult and has_id
   print(f"Can enter: {can_enter}")  # False
   print(f"Can try again: {not can_enter}")  # True
   ```

4. **Assignment Operators**:
   ```python
   total: float = 100.0
   total += 50.5  # Equivalent to total = total + 50.5
   print(f"Updated total: {total}")  # 150.5
   ```

5. **Membership and Identity**:
   ```python
   fruits: list = ["apple", "banana"]
   print(f"Apple in list: {'apple' in fruits}")  # True
   x: int = 1000
   y: int = 1000
   print(f"Same object: {x is y}")  # May be False (depends on Python's integer caching)
   ```

6. **Combining Operators in Expressions**:
   ```python
   # Calculate discounted price
   price: float = 200.0
   discount: float = 0.2
   final_price: float = price * (1 - discount)
   is_affordable: bool = final_price <= 150.0
   print(f"Final price: {final_price}, Affordable: {is_affordable}")  # Final price: 160.0, Affordable: False
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `operators.py` in your `day2_project` folder that:
1. Prompts the user for:
   - Their budget (float).
   - The price of an item (float).
   - The quantity they want to buy (integer).
2. Calculates:
   - The total cost (price * quantity).
   - The remaining budget after purchase.
   - Whether the purchase is affordable (total cost <= budget).
3. Uses type hints, error handling, and explicit variable names.
4. Prints a summary of the results.

**Example Solution**:
```python
def calculate_purchase() -> None:
    """Calculate purchase details based on user input."""
    try:
        budget: float = float(input("Enter your budget: "))
        price: float = float(input("Enter item price: "))
        quantity: int = int(input("Enter quantity: "))
        
        total_cost: float = price * quantity
        remaining_budget: float = budget - total_cost
        is_affordable: bool = total_cost <= budget
        
        print(f"Total cost: {total_cost:.2f}")
        print(f"Remaining budget: {remaining_budget:.2f}")
        print(f"Affordable: {is_affordable}")
    except ValueError:
        print("Error: Please enter valid numeric values.")

calculate_purchase()
```

**Task**:
- Run the script with inputs (e.g., budget=100.0, price=20.0, quantity=4).
- Test with invalid inputs (e.g., “abc” for price) to verify error handling.
- Add a check to print if the remaining budget is enough for another item (remaining_budget >= price).

**Expected Output** (for budget=100.0, price=20.0, quantity=4):
```
Enter your budget: 100.0
Enter item price: 20.0
Enter quantity: 4
Total cost: 80.00
Remaining budget: 20.00
Affordable: True
Can buy another: True
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to use Python’s operators (arithmetic, comparison, logical, etc.) to build expressions, reinforcing explicit coding practices. You applied these in a practical script, using your development environment. Tomorrow, we’ll explore **control flow** (if statements, loops), which builds on operators to control program execution.

#### Homework
- Modify `operators.py` to:
  - Add a discount percentage input (e.g., 10% = 0.1).
  - Calculate the discounted total cost.
  - Print whether the purchase saves money (discount reduces cost by >0).
- Experiment with operator precedence:
  - Write an expression like `5 + 3 * 2` and test with/without parentheses (e.g., `(5 + 3) * 2`).
  - Predict and verify the results.
- Read the [Python documentation on operators](https://docs.python.org/3/reference/expressions.html) (sections on arithmetic and comparison operators, ~5 minutes).
- Reflect on how explicit variable names and type hints in today’s exercise improved code clarity.

---

### Day 5: Control Flow in Python

#### Objective
Learn how to control the flow of a Python program using conditional statements (`if`, `elif`, `else`) and loops (`for`, `while`). Building on Day 4’s operators and Day 3’s variables, control flow allows you to make decisions and repeat actions, key skills for solving complex problems and writing dynamic programs in professional settings.

---

#### Lecture (10 minutes)
**Control flow** determines the order in which a program’s statements are executed. Python provides two main mechanisms:
1. **Conditional Statements**: Execute code based on conditions.
   - `if`, `elif`, `else`: Test conditions using boolean expressions (from Day 4’s operators).
2. **Loops**: Repeat code blocks.
   - `for`: Iterate over a sequence (e.g., list, range).
   - `while`: Repeat until a condition is false.
   - Control statements: `break` (exit loop), `continue` (skip to next iteration), `pass` (placeholder).

**Key Concepts**:
- Conditions use comparison and logical operators (e.g., `x > 0 and y < 10`).
- Indentation (4 spaces) defines code blocks in Python, enforcing readability.
- Explicit conditions and clear loop logic align with “explicit is better than implicit.”
- Avoid infinite loops in `while` by ensuring conditions eventually become false.

**Why This Matters**:
Control flow is essential for decision-making and iteration in real-world applications, like processing data, handling user input, or automating tasks. It’s a cornerstone of programming logic used in software development and data science.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code.

1. **Conditional Statements (`if`, `elif`, `else`)**:
   ```python
   # Check age for access
   age: int = int(input("Enter your age: "))
   if age >= 18:
       print("Access granted: Adult")
   elif age >= 13:
       print("Access granted: Teen")
   else:
       print("Access denied: Minor")
   ```

2. **Nested Conditions**:
   ```python
   # Check eligibility for a discount
   is_student: bool = input("Are you a student? (yes/no): ").lower() == "yes"
   total_purchase: float = float(input("Enter purchase amount: "))
   if is_student:
       if total_purchase > 50.0:
           print("You get a 10% student discount!")
       else:
           print("Student, but purchase too low for discount.")
   else:
       print("No discount: Not a student.")
   ```

3. **For Loops**:
   ```python
   # Iterate over a range
   for i in range(5):  # 0 to 4
       print(f"Iteration {i}: {i * 2}")
   # Iterate over a list
   fruits: list = ["apple", "banana", "orange"]
   for fruit in fruits:
       print(f"Fruit: {fruit.upper()}")
   ```

4. **While Loops**:
   ```python
   # Count down from user input
   count: int = int(input("Enter a number to count down from: "))
   while count > 0:
       print(f"Countdown: {count}")
       count -= 1
   print("Blast off!")
   ```

5. **Control Statements**:
   ```python
   # Break and continue
   for num in range(10):
       if num == 5:
           break  # Exit loop
       if num % 2 == 0:
           continue  # Skip even numbers
       print(f"Odd number: {num}")
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `control_flow.py` in your `day2_project` folder that:
1. Prompts the user for:
   - Their hourly wage (float).
   - Hours worked this week (integer).
   - Whether they’re a full-time employee (yes/no).
2. Calculates:
   - Total weekly pay (wage * hours).
   - Overtime pay (1.5x wage for hours > 40, only for non-full-time employees).
   - Tax rate: 20% if total pay > $500, else 10%.
3. Uses conditionals and loops to:
   - Compute the final pay after tax.
   - Print a pay breakdown (hours, wage, overtime, tax, final pay).
4. Includes type hints, error handling, and explicit variable names.

**Example Solution**:
```python
def calculate_pay() -> None:
    """Calculate weekly pay with overtime and tax."""
    try:
        wage: float = float(input("Enter hourly wage: "))
        hours: int = int(input("Enter hours worked: "))
        is_full_time: bool = input("Full-time employee? (yes/no): ").lower() == "yes"
        
        regular_pay: float = wage * min(hours, 40)
        overtime_pay: float = 0.0
        if not is_full_time and hours > 40:
            overtime_pay = (hours - 40) * wage * 1.5
        
        total_pay: float = regular_pay + overtime_pay
        tax_rate: float = 0.2 if total_pay > 500 else 0.1
        tax: float = total_pay * tax_rate
        final_pay: float = total_pay - tax
        
        print("Pay Breakdown:")
        for item, value in [
            ("Hours worked", hours),
            ("Hourly wage", f"${wage:.2f}"),
            ("Regular pay", f"${regular_pay:.2f}"),
            ("Overtime pay", f"${overtime_pay:.2f}"),
            ("Tax rate", f"{tax_rate*100:.0f}%"),
            ("Tax", f"${tax:.2f}"),
            ("Final pay", f"${final_pay:.2f}")
        ]:
            print(f"{item}: {value}")
    except ValueError:
        print("Error: Please enter valid numeric values for wage and hours.")

calculate_pay()
```

**Task**:
- Run the script with inputs (e.g., wage=15.0, hours=45, full-time=no).
- Test with invalid inputs (e.g., “abc” for hours) to verify error handling.
- Add a loop to ask if the user wants to calculate pay for another employee (repeat until they enter “no”).

**Expected Output** (for wage=15.0, hours=45, full-time=no):
```
Enter hourly wage: 15.0
Enter hours worked: 45
Full-time employee? (yes/no): no
Pay Breakdown:
Hours worked: 45
Hourly wage: $15.00
Regular pay: $600.00
Overtime pay: $112.50
Tax rate: 20%
Tax: $142.50
Final pay: $570.00
```

---

#### Summary & Preview (5 minutes)
Today, you mastered control flow using `if`, `elif`, `else`, `for`, and `while`, enabling dynamic program behavior. You applied these in a practical payroll script, reinforcing explicit coding practices. Tomorrow, we’ll cover **functions**, learning how to modularize code for reusability and clarity, a key skill for professional programming.

#### Homework
- Modify `control_flow.py` to:
  - Add a check if the final pay is above a user-defined minimum wage threshold (e.g., $400).
  - Use a `while` loop to validate that hours are non-negative.
- Experiment with control flow:
  - Write a script that prints all even numbers from 1 to 20 using a `for` loop and `continue`.
  - Test a `while` loop that doubles a number until it exceeds 1000, starting from user input.
- Read the [Python documentation on control flow](https://docs.python.org/3/tutorial/controlflow.html) (sections on `if` and `for`, ~5 minutes).
- Reflect on how explicit conditionals (e.g., `hours > 40`) make the payroll script clearer than implicit checks.

---

#### Notes
- The first test is this Saturday (covering Days 1–5: history, setup, variables, data types, operators, control flow). Expect coding problems and multiple-choice questions.
- If you encounter errors (e.g., indentation issues), check VS Code’s linting or ask for help.
- Ensure your virtual environment is active.

Let me know if you want to revisit Day 3, need help with the exercise, or have questions about control flow!


### Day 6: Functions in Python

#### Objective
Learn how to define, use, and organize **functions** in Python to create modular, reusable, and maintainable code. Building on Day 4’s operators and Day 5’s control flow, functions allow you to encapsulate logic, making your programs more structured and aligned with professional programming practices.

---

#### Lecture (10 minutes)
**Functions** are reusable blocks of code that perform a specific task, defined using the `def` keyword. They improve code organization, reduce redundancy, and enhance readability, aligning with Python’s “explicit is better than implicit” philosophy.

**Key Concepts**:
- **Syntax**: `def function_name(parameters) -> return_type:`
  - Parameters: Inputs to the function (optional).
  - Return type: Use type hints to indicate output type.
  - Docstring: Describe the function’s purpose (explicit documentation).
- **Return Statements**: Use `return` to output a value; defaults to `None` if omitted.
- **Default Parameters**: Allow optional arguments with default values.
- **Scope**: Variables defined inside a function are local; global variables are accessible but should be used cautiously.
- **Best Practices**:
  - Use descriptive names (e.g., `calculate_total` instead of `calc`).
  - Keep functions short and focused (single responsibility).
  - Use type hints and docstrings for clarity.

**Why This Matters**:
Functions are fundamental for structuring code in professional projects, from small scripts to large applications like web servers or data pipelines. They prepare you for modular programming and frameworks like Flask or Django.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code.

1. **Basic Function Definition**:
   ```python
   def greet(name: str) -> str:
       """Return a greeting for the given name."""
       return f"Hello, {name}!"
   
   result: str = greet("Alice")
   print(result)  # Output: Hello, Alice!
   ```

2. **Functions with Multiple Parameters**:
   ```python
   def calculate_area(length: float, width: float) -> float:
       """Calculate the area of a rectangle."""
       return length * width
   
   area: float = calculate_area(5.0, 3.0)
   print(f"Area: {area}")  # Output: Area: 15.0
   ```

3. **Default Parameters**:
   ```python
   def apply_discount(price: float, discount: float = 0.1) -> float:
       """Apply a discount to a price (default 10%)."""
       return price * (1 - discount)
   
   print(apply_discount(100.0))  # Output: 90.0 (10% discount)
   print(apply_discount(100.0, 0.2))  # Output: 80.0 (20% discount)
   ```

4. **Returning Multiple Values**:
   ```python
   def divide_and_remainder(a: int, b: int) -> tuple[int, int]:
       """Return quotient and remainder of division."""
       quotient = a // b
       remainder = a % b
       return quotient, remainder
   
   q, r = divide_and_remainder(17, 5)
   print(f"Quotient: {q}, Remainder: {r}")  # Output: Quotient: 3, Remainder: 2
   ```

5. **Scope and Error Handling**:
   ```python
   def safe_divide(a: float, b: float) -> float:
       """Divide a by b, handling division by zero."""
       try:
           result = a / b
           return result
       except ZeroDivisionError:
           return float('inf')  # Return infinity for division by zero
   
   print(safe_divide(10.0, 2.0))  # Output: 5.0
   print(safe_divide(10.0, 0.0))  # Output: inf
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `functions.py` in your `day2_project` folder that:
1. Defines a function `calculate_bmi` that:
   - Takes `weight` (kg, float) and `height` (meters, float) as parameters.
   - Calculates BMI: `weight / (height ** 2)`.
   - Returns the BMI and a category (e.g., “Underweight” for BMI < 18.5, “Normal” for 18.5–24.9, “Overweight” for 25–29.9, “Obese” for ≥30).
2. Prompts the user for weight and height, calls the function, and prints the results.
3. Includes type hints, a docstring, and error handling for invalid inputs.
4. Uses a default parameter for a unit system (e.g., metric by default, but convertible to imperial).

**Example Solution**:
```python
def calculate_bmi(weight: float, height: float, is_metric: bool = True) -> tuple[float, str]:
    """Calculate BMI and category. If is_metric=False, convert from lbs and feet."""
    try:
        if not is_metric:
            weight = weight * 0.453592  # Convert lbs to kg
            height = height * 0.3048  # Convert feet to meters
        
        bmi: float = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        return bmi, category
    except ZeroDivisionError:
        return 0.0, "Error: Height cannot be zero"

def main() -> None:
    """Collect user input and display BMI results."""
    try:
        weight: float = float(input("Enter weight (kg or lbs): "))
        height: float = float(input("Enter height (meters or feet): "))
        unit: str = input("Unit system (metric/imperial): ").lower()
        is_metric: bool = unit != "imperial"
        
        bmi, category = calculate_bmi(weight, height, is_metric)
        print(f"BMI: {bmi:.2f}, Category: {category}")
    except ValueError:
        print("Error: Please enter valid numeric values for weight and height.")

main()
```

**Task**:
- Run the script with inputs (e.g., weight=70, height=1.75, unit=metric).
- Test with imperial units (e.g., weight=154, height=5.74, unit=imperial) and invalid inputs (e.g., height=0).
- Add a feature to loop and ask for another calculation until the user enters “no”.

**Expected Output** (for weight=70, height=1.75, unit=metric):
```
Enter weight (kg or lbs): 70
Enter height (meters or feet): 1.75
Unit system (metric/imperial): metric
BMI: 22.86, Category: Normal
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to define and use functions to modularize code, incorporating parameters, return values, and error handling. You applied these in a BMI calculator, reinforcing explicit practices with type hints and docstrings. Tomorrow, we’ll explore **lists and tuples**, diving into Python’s core data structures for storing collections of data.

#### Homework
- Modify `functions.py` to:
  - Add a parameter to `calculate_bmi` for a target BMI, and print whether the user’s BMI is above, below, or equal to it.
  - Validate that weight and height are positive numbers.
- Experiment with functions:
  - Write a function that takes a list of numbers and returns the minimum and maximum as a tuple.
  - Test it with `[4, 2, 9, 1]` and print the results.
- Read the [Python documentation on functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) (~5 minutes).
- Reflect on how functions in today’s exercise made the code more reusable compared to Day 5’s payroll script.

---

#### Notes
- The first test is tomorrow (Saturday, covering Days 1–6: history, setup, variables, data types, operators, control flow, functions). Expect 3 hours with coding problems (e.g., write a function to process user input) and multiple-choice questions (e.g., function syntax).
- If you hit issues (e.g., scope errors or invalid inputs), check VS Code’s debugging tools or ask for help.
- Ensure your virtual environment is active.

Let me know if you need help with the exercise, want a review for the test, or have questions about functions!


### Day 7: Lists and Tuples in Python

#### Objective
Learn how to use **lists** and **tuples**, Python’s core data structures for storing collections of data. Building on Day 6’s functions and previous topics, these structures allow you to manage multiple values efficiently, a critical skill for data processing and professional programming.

---

#### Lecture (10 minutes)
**Lists** and **tuples** are sequence types in Python that store ordered collections of items. They are versatile and widely used in applications like data analysis, web development, and automation.

- **Lists**:
  - **Mutable**: Can be modified after creation (add, remove, or change items).
  - Syntax: `my_list = [1, 2, 3]` or `my_list: list[int] = [1, 2, 3]` (with type hints).
  - Common operations: Indexing, slicing, appending, extending, removing.
  - Use cases: Storing dynamic data (e.g., user inputs, datasets).
- **Tuples**:
  - **Immutable**: Cannot be changed after creation.
  - Syntax: `my_tuple = (1, 2, 3)` or `my_tuple: tuple[int, ...] = (1, 2, 3)`.
  - Use cases: Fixed data, return multiple values from functions, dictionary keys.
- **Key Concepts**:
  - Indexing: Access items with `list[0]` (starts at 0).
  - Slicing: Extract sublists with `list[start:end]`.
  - List methods: `append()`, `remove()`, `pop()`, `sort()`, etc.
  - Explicitness: Use type hints and descriptive names for clarity.
- **Why This Matters**:
  Lists and tuples are foundational for handling collections in Python, used in everything from simple scripts to complex data pipelines. Understanding their differences (mutability vs. immutability) is key for efficient and safe coding.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code.

1. **Creating and Accessing Lists**:
   ```python
   # Define a list with type hints
   numbers: list[int] = [10, 20, 30, 40]
   print(f"First item: {numbers[0]}")  # Output: 10
   print(f"Last item: {numbers[-1]}")  # Output: 40
   print(f"Sublist: {numbers[1:3]}")  # Output: [20, 30]
   ```

2. **Modifying Lists**:
   ```python
   fruits: list[str] = ["apple", "banana"]
   fruits.append("orange")  # Add item
   fruits[1] = "mango"  # Replace item
   fruits.remove("apple")  # Remove item
   print(f"Modified list: {fruits}")  # Output: ['mango', 'orange']
   ```

3. **Creating and Using Tuples**:
   ```python
   point: tuple[float, float] = (3.0, 4.0)
   print(f"X coordinate: {point[0]}")  # Output: 3.0
   # point[0] = 5.0  # Error: Tuples are immutable
   ```

4. **List Operations in a Function**:
   ```python
   def filter_above_threshold(numbers: list[float], threshold: float) -> list[float]:
       """Return numbers above the given threshold."""
       return [num for num in numbers if num > threshold]  # List comprehension
       
   scores: list[float] = [85.5, 90.0, 75.0, 95.0]
   high_scores: list[float] = filter_above_threshold(scores, 80.0)
   print(f"High scores: {high_scores}")  # Output: [85.5, 90.0, 95.0]
   ```

5. **Tuple as Return Value**:
   ```python
   def min_max(numbers: list[int]) -> tuple[int, int]:
       """Return the minimum and maximum of a list."""
       return min(numbers), max(numbers)
   
   values: list[int] = [4, 2, 9, 1]
   min_val, max_val = min_max(values)
   print(f"Min: {min_val}, Max: {max_val}")  # Output: Min: 1, Max: 9
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `lists_tuples.py` in your `day2_project` folder that:
1. Defines a function `process_grades` that:
   - Takes a list of grades (float) and a passing threshold (float).
   - Returns a tuple containing:
     - A list of passing grades (above threshold).
     - The average of all grades.
     - The count of failing grades (below threshold).
2. Prompts the user to input grades (comma-separated, e.g., “85, 90, 70”).
3. Calls the function with a default threshold of 75.0 and prints the results.
4. Includes type hints, a docstring, and error handling.

**Example Solution**:
```python
def process_grades(grades: list[float], threshold: float = 75.0) -> tuple[list[float], float, int]:
    """Process grades and return passing grades, average, and failing count."""
    try:
        passing: list[float] = [grade for grade in grades if grade >= threshold]
        average: float = sum(grades) / len(grades) if grades else 0.0
        failing_count: int = sum(1 for grade in grades if grade < threshold)
        return passing, average, failing_count
    except ZeroDivisionError:
        return [], 0.0, 0

def main() -> None:
    """Collect grades and display processed results."""
    try:
        input_str: str = input("Enter grades (comma-separated): ")
        grades: list[float] = [float(g.strip()) for g in input_str.split(",")]
        
        passing_grades, avg_grade, failing_count = process_grades(grades)
        print(f"Passing grades: {passing_grades}")
        print(f"Average grade: {avg_grade:.2f}")
        print(f"Failing grades count: {failing_count}")
    except ValueError:
        print("Error: Please enter valid numeric grades.")

main()
```

**Task**:
- Run the script with inputs (e.g., “85, 90, 70, 60”).
- Test with invalid inputs (e.g., “85, abc, 90”) to verify error handling.
- Add a feature to loop and process another set of grades until the user enters “done”.

**Expected Output** (for “85, 90, 70, 60”):
```
Enter grades (comma-separated): 85, 90, 70, 60
Passing grades: [85.0, 90.0]
Average grade: 76.25
Failing grades count: 2
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to use lists and tuples to store and manipulate collections, integrating them with functions for modular code. You reinforced explicit practices with type hints and docstrings. Tomorrow, we’ll cover **dictionaries and sets**, exploring more advanced data structures for key-value pairs and unique collections.

#### Homework
- Modify `lists_tuples.py` to:
  - Validate that grades are between 0 and 100.
  - Add a feature to return the highest and lowest grades in the results tuple.
- Experiment with lists and tuples:
  - Create a list of 5 numbers and sort it in descending order using `sort()`.
  - Create a tuple of 3 strings and try modifying it to confirm immutability.
- Read the [Python documentation on lists and tuples](https://docs.python.org/3/tutorial/datastructures.html) (sections on lists and tuples, ~5 minutes).
- Reflect on how lists vs. tuples in today’s exercise impact code design (e.g., mutability for grades vs. immutability for results).

---

#### Notes
- Today’s test (Saturday, covering Days 1–6: history, setup, variables, data types, operators, control flow, functions) is scheduled. Since it’s 1:24 AM EAT on Friday, July 25, 2025, I can provide a sample test now if you’re ready, or we can proceed tomorrow. Let me know your preference!
- The test will include:
  - Coding problems (e.g., write a function with control flow).
  - Multiple-choice questions (e.g., syntax, operator precedence).
  - Short exercises (e.g., debug a script).
- Ensure your virtual environment is active.

Let me know if you want the test now, need help with the exercise, or have questions about lists and tuples!


### Day 8: Dictionaries and Sets in Python

#### Objective
Learn how to use **dictionaries** and **sets**, Python’s powerful data structures for storing key-value pairs and unique collections, respectively. Building on Day 7’s lists and tuples, these structures enable efficient data organization and manipulation, critical for professional applications like data processing, web development, and database operations.

---

#### Lecture (10 minutes)
**Dictionaries** and **sets** are advanced data structures that complement lists and tuples:
- **Dictionaries**:
  - Store **key-value pairs**, where keys are unique and immutable (e.g., strings, numbers, tuples).
  - Syntax: `my_dict = {"key": "value"}` or `my_dict: dict[str, int] = {"age": 25}`.
  - Common operations: Add/delete items, access values, iterate over keys/values.
  - Use cases: Storing structured data (e.g., user profiles, JSON-like data).
- **Sets**:
  - Store **unique, unordered** items; mutable but no duplicates.
  - Syntax: `my_set = {1, 2, 3}` or `my_set: set[int] = {1, 2, 3}`.
  - Common operations: Union, intersection, difference, add/remove items.
  - Use cases: Removing duplicates, testing membership, set operations.
- **Key Concepts**:
  - Dictionaries use keys for fast lookups (hash tables).
  - Sets ensure uniqueness, ideal for deduplication.
  - Explicitness: Use type hints and clear key names for readability.
  - Mutability: Dictionaries and sets are mutable; use `frozenset` for immutable sets.
- **Why This Matters**:
  Dictionaries and sets are widely used in professional Python projects, such as parsing APIs, managing unique IDs, or analyzing data. They prepare you for working with databases and frameworks like Django.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code.

1. **Creating and Accessing Dictionaries**:
   ```python
   # Define a dictionary with type hints
   student: dict[str, any] = {"name": "Alice", "age": 20, "grade": 85.5}
   print(f"Student name: {student['name']}")  # Output: Alice
   print(f"Keys: {list(student.keys())}")  # Output: ['name', 'age', 'grade']
   print(f"Values: {list(student.values())}")  # Output: ['Alice', 20, 85.5]
   ```

2. **Modifying Dictionaries**:
   ```python
   # Add and update items
   student["major"] = "Computer Science"
   student["age"] = 21  # Update existing key
   del student["grade"]  # Remove key
   print(f"Updated student: {student}")  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
   ```

3. **Creating and Using Sets**:
   ```python
   # Define a set
   unique_numbers: set[int] = {1, 2, 2, 3}  # Duplicates removed
   print(f"Set: {unique_numbers}")  # Output: {1, 2, 3}
   unique_numbers.add(4)  # Add item
   unique_numbers.remove(1)  # Remove item
   print(f"Updated set: {unique_numbers}")  # Output: {2, 3, 4}
   ```

4. **Set Operations**:
   ```python
   set1: set[int] = {1, 2, 3}
   set2: set[int] = {2, 3, 4}
   print(f"Union: {set1 | set2}")  # Output: {1, 2, 3, 4}
   print(f"Intersection: {set1 & set2}")  # Output: {2, 3}
   print(f"Difference: {set1 - set2}")  # Output: {1}
   ```

5. **Dictionary and Set in a Function**:
   ```python
   def analyze_grades(grades: dict[str, float]) -> tuple[set[str], float]:
       """Return unique students with passing grades and average score."""
       passing_students: set[str] = {name for name, score in grades.items() if score >= 75.0}
       average: float = sum(grades.values()) / len(grades) if grades else 0.0
       return passing_students, average

   grades: dict[str, float] = {"Alice": 85.0, "Bob": 70.0, "Charlie": 90.0}
   passers, avg = analyze_grades(grades)
   print(f"Passing students: {passers}, Average: {avg:.2f}")  # Output: Passing students: {'Alice', 'Charlie'}, Average: 81.67
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `dicts_sets.py` in your `day2_project` folder that:
1. Defines a function `process_inventory` that:
   - Takes a dictionary of item names (str) and quantities (int).
   - Returns a tuple containing:
     - A set of items with low stock (quantity < 5).
     - The total quantity of all items.
     - A dictionary of items with sufficient stock (quantity >= 5).
2. Prompts the user to input items and quantities (e.g., “apple:10,banana:3”).
3. Calls the function and prints the results.
4. Includes type hints, a docstring, and error handling.

**Example Solution**:
```python
def process_inventory(inventory: dict[str, int]) -> tuple[set[str], int, dict[str, int]]:
    """Process inventory and return low stock items, total quantity, and sufficient stock."""
    low_stock: set[str] = {item for item, qty in inventory.items() if qty < 5}
    total_qty: int = sum(inventory.values())
    sufficient_stock: dict[str, int] = {item: qty for item, qty in inventory.items() if qty >= 5}
    return low_stock, total_qty, sufficient_stock

def main() -> None:
    """Collect inventory input and display results."""
    try:
        input_str: str = input("Enter items and quantities (e.g., apple:10,banana:3): ")
        inventory: dict[str, int] = {
            item.split(":")[0].strip(): int(item.split(":")[1].strip())
            for item in input_str.split(",")
        }
        
        low_stock, total_qty, sufficient_stock = process_inventory(inventory)
        print(f"Low stock items: {low_stock}")
        print(f"Total quantity: {total_qty}")
        print(f"Sufficient stock: {sufficient_stock}")
    except (ValueError, IndexError):
        print("Error: Please enter valid item:quantity pairs (e.g., apple:10,banana:3).")

main()
```

**Task**:
- Run the script with inputs (e.g., “apple:10,banana:3,orange:2”).
- Test with invalid inputs (e.g., “apple:abc”) to verify error handling.
- Add a loop to process another inventory until the user enters “done”.

**Expected Output** (for “apple:10,banana:3,orange:2”):
```
Enter items and quantities (e.g., apple:10,banana:3): apple:10,banana:3,orange:2
Low stock items: {'banana', 'orange'}
Total quantity: 15
Sufficient stock: {'apple': 10}
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to use dictionaries for key-value storage and sets for unique collections, integrating them with functions for practical tasks. You reinforced explicit practices with type hints and docstrings. Tomorrow, we’ll cover **file input/output (I/O)**, learning how to read from and write to files for persistent data storage.

#### Homework
- Modify `dicts_sets.py` to:
  - Validate that quantities are non-negative.
  - Add a feature to return the item with the highest quantity in the results tuple.
- Experiment with dictionaries and sets:
  - Create a dictionary of 3 students and their grades, then update one grade and add a new student.
  - Create two sets of numbers and print their union and intersection.
- Read the [Python documentation on dictionaries and sets](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) (sections on dictionaries and sets, ~5 minutes).
- Reflect on how dictionaries vs. lists in today’s exercise affect data organization (e.g., key-based access vs. ordered indices).

---

#### Notes
- Yesterday’s test (Saturday, covering Days 1–6) was mentioned. Since it’s now 1:25 AM EAT on Friday, July 25, 2025, I assume you meant to continue with the next lesson. If you want the test for Days 1–6 or a review, let me know, and I can provide it!
- The next test (Week 4, Saturday) will cover Days 1–10, including today’s dictionaries and sets.
- Ensure your virtual environment is active.

Let me know if you need the Week 2 test, help with the exercise, or have questions about dictionaries and sets!



### Day 9: File Input/Output (I/O) in Python

#### Objective
Learn how to read from and write to files in Python, enabling persistent data storage and retrieval. Building on Day 8’s dictionaries and sets, file I/O is essential for handling data in real-world applications like logging, configuration files, and data processing, preparing you for professional workflows.

---

#### Lecture (10 minutes)
**File I/O** allows Python programs to interact with files on disk, reading data for processing or writing results for storage. Python provides built-in functions to handle text and binary files, with a focus on simplicity and explicitness.

- **Key Concepts**:
  - **Opening Files**: Use `open(filename, mode)` with modes like `'r'` (read), `'w'` (write), `'a'` (append), `'rb'`/`'wb'` (binary read/write).
  - **Reading**: Methods like `read()`, `readline()`, `readlines()` or iterating over a file object.
  - **Writing**: Methods like `write()`, `writelines()`.
  - **Closing Files**: Use `close()` or a `with` statement (context manager) for automatic closure.
  - **Best Practices**:
    - Use `with` statements to ensure files are closed properly.
    - Handle exceptions (e.g., `FileNotFoundError`) for robustness.
    - Use type hints and clear file paths for explicitness.
- **Why This Matters**:
  File I/O is critical for tasks like saving user data, processing CSV files, or logging in professional applications (e.g., web servers, data pipelines). It prepares you for working with databases and APIs.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code. Create a `files` folder in `day2_project` for today’s work.

1. **Writing to a Text File**:
   ```python
   def write_student_data(filename: str, student: dict[str, any]) -> None:
       """Write student data to a text file."""
       with open(filename, 'w') as file:
           for key, value in student.items():
               file.write(f"{key}: {value}\n")
   
   student: dict[str, any] = {"name": "Alice", "age": 20, "grade": 85.5}
   write_student_data("files/student.txt", student)
   ```

2. **Reading from a Text File**:
   ```python
   def read_student_data(filename: str) -> dict[str, any]:
       """Read student data from a text file."""
       student: dict[str, any] = {}
       try:
           with open(filename, 'r') as file:
               for line in file:
                   key, value = line.strip().split(": ", 1)
                   student[key] = value if key != "age" else int(value)
               return student
       except FileNotFoundError:
           print(f"Error: {filename} not found.")
           return {}
   
   data = read_student_data("files/student.txt")
   print(f"Read data: {data}")  # Output: {'name': 'Alice', 'age': 20, 'grade': '85.5'}
   ```

3. **Appending to a File**:
   ```python
   def append_log(filename: str, message: str) -> None:
       """Append a message to a log file."""
       with open(filename, 'a') as file:
           file.write(f"{message}\n")
   
   append_log("files/log.txt", "User logged in at 2025-07-25")
   append_log("files/log.txt", "User updated profile")
   ```

4. **Reading All Lines**:
   ```python
   def read_log(filename: str) -> list[str]:
       """Read all lines from a log file."""
       try:
           with open(filename, 'r') as file:
               return [line.strip() for line in file]
       except FileNotFoundError:
           print(f"Error: {filename} not found.")
           return []
   
   logs = read_log("files/log.txt")
   print(f"Log entries: {logs}")  # Output: ['User logged in at 2025-07-25', 'User updated profile']
   ```

5. **Working with CSV Files** (using `csv` module):
   ```python
   import csv

   def write_csv(filename: str, data: list[dict[str, any]]) -> None:
       """Write a list of dictionaries to a CSV file."""
       headers = data[0].keys() if data else []
       with open(filename, 'w', newline='') as file:
           writer = csv.DictWriter(file, fieldnames=headers)
           writer.writeheader()
           writer.writerows(data)
   
   students = [
       {"name": "Alice", "grade": 85.5},
       {"name": "Bob", "grade": 90.0}
   ]
   write_csv("files/students.csv", students)
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `file_io.py` in your `day2_project` folder that:
1. Defines a function `manage_tasks` that:
   - Takes a list of tasks (dictionaries with keys “task” and “priority”).
   - Writes tasks to a text file (`files/tasks.txt`) in the format “task: priority”.
   - Reads the file and returns a set of high-priority tasks (priority > 5).
2. Prompts the user to input tasks and priorities (e.g., “Write report:7,Email:3”).
3. Calls the function and prints the high-priority tasks.
4. Includes type hints, a docstring, and error handling.

**Example Solution**:
```python
def manage_tasks(tasks: list[dict[str, any]], filename: str) -> set[str]:
    """Write tasks to a file and return high-priority tasks."""
    try:
        # Write tasks to file
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"{task['task']}: {task['priority']}\n")
        
        # Read and filter high-priority tasks
        high_priority: set[str] = set()
        with open(filename, 'r') as file:
            for line in file:
                task, priority = line.strip().split(": ")
                if int(priority) > 5:
                    high_priority.add(task)
        return high_priority
    except (FileNotFoundError, ValueError):
        print(f"Error processing {filename} or invalid data.")
        return set()

def main() -> None:
    """Collect task input and display high-priority tasks."""
    try:
        input_str: str = input("Enter tasks and priorities (e.g., Write report:7,Email:3): ")
        tasks: list[dict[str, any]] = [
            {"task": item.split(":")[0].strip(), "priority": int(item.split(":")[1].strip())}
            for item in input_str.split(",")
        ]
        
        high_priority = manage_tasks(tasks, "files/tasks.txt")
        print(f"High-priority tasks: {high_priority}")
    except (ValueError, IndexError):
        print("Error: Please enter valid task:priority pairs.")

main()
```

**Task**:
- Create the `files` folder if it doesn’t exist.
- Run the script with inputs (e.g., “Write report:7,Email:3,Meeting:8”).
- Test with invalid inputs (e.g., “Write report:abc”) to verify error handling.
- Add a loop to process another set of tasks until the user enters “done”.

**Expected Output** (for “Write report:7,Email:3,Meeting:8”):
```
Enter tasks and priorities (e.g., Write report:7,Email:3): Write report:7,Email:3,Meeting:8
High-priority tasks: {'Write report', 'Meeting'}
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to read from and write to files, using text and CSV formats for persistent data storage. You integrated file I/O with dictionaries and sets, reinforcing explicit practices with type hints and error handling. Tomorrow, we’ll explore **string manipulation and formatting**, diving deeper into text processing for robust data handling.

#### Homework
- Modify `file_io.py` to:
  - Validate that priorities are between 1 and 10.
  - Append new tasks to the file instead of overwriting it.
- Experiment with file I/O:
  - Write a script to save a list of 3 numbers to a file and read them back as a list.
  - Try reading a non-existent file and handle the `FileNotFoundError`.
- Read the [Python documentation on file I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) (~5 minutes).
- Reflect on how file I/O in today’s exercise could be used in a professional project (e.g., logging user actions).

---

#### Notes
- The Week 2 test (covering Days 1–6) was scheduled for yesterday (Saturday). Since it’s now 1:26 AM EAT on Friday, July 25, 2025, I assume you’re continuing with lessons. If you want to take or review the test, let me know!
- The next test (Week 4, Saturday) will cover Days 1–10, including today’s file I/O.
- Ensure your virtual environment is active and the `files` folder is created.

Let me know if you need the Week 2 test, help with the exercise, or have questions about file I/O!


### Day 10: String Manipulation and Formatting in Python

#### Objective
Learn how to manipulate and format strings in Python, a critical skill for processing text data in applications like web development, data analysis, and automation. Building on Day 9’s file I/O and previous topics, you’ll explore string operations, formatting techniques, and regular expressions to handle text effectively.

---

#### Lecture (10 minutes)
**Strings** are immutable sequences of characters in Python, used for text data. String manipulation and formatting are essential for tasks like parsing user input, generating reports, or formatting data for files.

- **Key Concepts**:
  - **String Operations**:
    - Concatenation (`+`), repetition (`*`), slicing (`str[start:end]`).
    - Methods: `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`, `find()`.
  - **String Formatting**:
    - f-strings: `f"Name: {name}"` (Python 3.6+, preferred for readability).
    - `.format()`: `"Name: {}".format(name)` (older but still used).
    - `%` operator: `"Name: %s" % name` (legacy, avoid in new code).
  - **Regular Expressions** (intro):
    - Use the `re` module for pattern matching (e.g., validating emails).
  - **Best Practices**:
    - Use f-strings for explicit, readable formatting.
    - Handle edge cases (e.g., empty strings) with error checking.
    - Use type hints (e.g., `str`) for clarity.
- **Why This Matters**:
  Strings are ubiquitous in programming, from user interfaces to data parsing. Mastering string manipulation prepares you for tasks like processing CSV files, generating logs, or building web APIs.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code. Use the `files` folder from Day 9 for file-related examples.

1. **Basic String Operations**:
   ```python
   def process_text(text: str) -> dict[str, str]:
       """Process a string and return modified versions."""
       return {
           "uppercase": text.upper(),
           "stripped": text.strip(),
           "words": text.split()
       }
   
   input_text: str = "  Hello, World!  "
   result = process_text(input_text)
   print(f"Uppercase: {result['uppercase']}")  # Output: HELLO, WORLD!
   print(f"Stripped: {result['stripped']}")  # Output: Hello, World!
   print(f"Words: {result['words']}")  # Output: ['Hello,', 'World!']
   ```

2. **String Formatting with f-strings**:
   ```python
   def format_student(student: dict[str, any]) -> str:
       """Format student data into a string."""
       return f"Student: {student['name']}, Age: {student['age']}, Grade: {student['grade']:.2f}"
   
   student: dict[str, any] = {"name": "Alice", "age": 20, "grade": 85.5}
   print(format_student(student))  # Output: Student: Alice, Age: 20, Grade: 85.50
   ```

3. **Joining and Replacing**:
   ```python
   words: list[str] = ["Python", "is", "awesome"]
   sentence: str = " ".join(words)
   print(f"Joined: {sentence}")  # Output: Python is awesome
   modified: str = sentence.replace("awesome", "great")
   print(f"Modified: {modified}")  # Output: Python is great
   ```

4. **Regular Expressions with `re`**:
   ```python
   import re

   def is_valid_email(email: str) -> bool:
       """Check if a string is a valid email address."""
       pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
       return bool(re.match(pattern, email))
   
   email: str = "user@example.com"
   print(f"Valid email: {is_valid_email(email)}")  # Output: True
   print(f"Valid email: {is_valid_email('invalid@.com')}")  # Output: False
   ```

5. **File I/O with Strings**:
   ```python
   def save_formatted_data(filename: str, items: list[dict[str, any]]) -> None:
       """Save formatted item data to a file."""
       with open(filename, 'w') as file:
           for item in items:
               line = f"{item['name']}: ${item['price']:.2f}\n"
               file.write(line)
   
   items = [{"name": "Apple", "price": 0.5}, {"name": "Banana", "price": 0.3}]
   save_formatted_data("files/items.txt", items)
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `strings.py` in your `day2_project` folder that:
1. Defines a function `process_log` that:
   - Takes a list of log entries (strings, e.g., “2025-07-25 10:00: User logged in”).
   - Returns a tuple containing:
     - A set of unique user actions (e.g., “logged in”, “logged out”).
     - A formatted string summarizing the number of entries and earliest date.
   - Writes the log entries to a file (`files/log_summary.txt`) in a formatted way.
2. Prompts the user to input log entries (comma-separated, e.g., “2025-07-25 10:00: User logged in,2025-07-25 11:00: User logged out”).
3. Calls the function and prints the results.
4. Includes type hints, a docstring, and error handling.

**Example Solution**:
```python
import re
from typing import Tuple, Set

def process_log(entries: list[str], filename: str) -> Tuple[Set[str], str]:
    """Process log entries, save to file, and return unique actions and summary."""
    try:
        # Extract actions using regex
        actions: Set[str] = set()
        dates: list[str] = []
        for entry in entries:
            match = re.match(r"(\d{4}-\d{2}-\d{2}).*?User (.*?)$", entry)
            if match:
                dates.append(match.group(1))
                actions.add(match.group(2))
        
        # Write formatted entries to file
        with open(filename, 'w') as file:
            for entry in entries:
                file.write(f"Log: {entry}\n")
        
        # Create summary
        summary: str = f"Total entries: {len(entries)}, Earliest date: {min(dates) if dates else 'N/A'}"
        return actions, summary
    except (FileNotFoundError, ValueError):
        print(f"Error processing {filename} or invalid log format.")
        return set(), "Error: Invalid data"

def main() -> None:
    """Collect log entries and display results."""
    try:
        input_str: str = input("Enter log entries (e.g., 2025-07-25 10:00: User logged in,...): ")
        entries: list[str] = [entry.strip() for entry in input_str.split(",")]
        
        actions, summary = process_log(entries, "files/log_summary.txt")
        print(f"Unique actions: {actions}")
        print(summary)
    except ValueError:
        print("Error: Please enter valid log entries.")

main()
```

**Task**:
- Run the script with inputs (e.g., “2025-07-25 10:00: User logged in,2025-07-25 11:00: User logged out,2025-07-24 09:00: User logged in”).
- Test with invalid inputs (e.g., “invalid”) to verify error handling.
- Add a loop to process another set of logs until the user enters “done”.

**Expected Output** (for above input):
```
Enter log entries (e.g., 2025-07-25 10:00: User logged in,...): 2025-07-25 10:00: User logged in,2025-07-25 11:00: User logged out,2025-07-24 09:00: User logged in
Unique actions: {'logged in', 'logged out'}
Total entries: 3, Earliest date: 2025-07-24
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to manipulate and format strings, using operations, f-strings, and regular expressions, and integrated them with file I/O. You reinforced explicit practices with type hints and error handling. Tomorrow, we’ll start **Phase 2: Intermediate Concepts** with **modules and packages**, learning how to organize and reuse code across files.

#### Homework
- Modify `strings.py` to:
  - Validate log entries have a valid date format (YYYY-MM-DD) using regex.
  - Add a feature to count occurrences of each action (e.g., “logged in: 2”).
- Experiment with strings:
  - Write a script to split a sentence into words, reverse each word, and join them back.
  - Test a regex to find all numbers in a string (e.g., “Price: $10.50, Tax: $2.00”).
- Read the [Python documentation on strings](https://docs.python.org/3/library/stdtypes.html#string-methods) and [re module](https://docs.python.org/3/library/re.html) (string methods and basic regex, ~5 minutes).
- Reflect on how f-strings in today’s exercise improved readability compared to concatenation.

---

#### Notes
- The Week 2 test (Days 1–6) was scheduled for yesterday (Saturday). Since it’s 1:27 AM EAT on Friday, July 25, 2025, I assume you’re continuing lessons. If you want the test or a review, let me know!
- The next test (Week 4, Saturday, August 2, 2025) covers Days 1–10, including today’s strings.
- Ensure your virtual environment is active and the `files` folder exists.

Let me know if you need the Week 2 test, help with the exercise, or have questions about strings!

### Day 11: Modules and Packages in Python

#### Objective
Learn how to create, use, and organize **modules** and **packages** in Python to modularize code for reusability and maintainability. Building on Day 10’s string manipulation and previous topics, this marks the start of **Phase 2: Intermediate Concepts**, preparing you for structured, professional-grade Python projects.

---

#### Lecture (10 minutes)
**Modules** are single Python files (`.py`) containing reusable code (e.g., functions, variables, classes). **Packages** are directories containing multiple modules and an `__init__.py` file, enabling organized code distribution. These concepts allow you to break large programs into manageable, reusable components.

- **Key Concepts**:
  - **Creating a Module**: Any `.py` file is a module (e.g., `utils.py`).
  - **Importing**: Use `import module`, `from module import name`, or `import module as alias`.
  - **Standard Library Modules**: Python includes modules like `math`, `datetime`, `os`.
  - **Packages**: A directory with `__init__.py` (can be empty) to group modules.
  - **Best Practices**:
    - Use explicit imports (e.g., `from math import pi` instead of `from math import *`).
    - Organize related functionality into modules or packages.
    - Use type hints and docstrings for clarity.
  - **Why This Matters**:
    Modules and packages are the backbone of large-scale Python projects, used in frameworks like Django, libraries like pandas, and collaborative development. They promote code reuse and maintainability, critical for professional work.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code. Create a `utils` folder in `day2_project` for today’s work.

1. **Creating a Module**:
   - Create a file `utils/string_utils.py`:
     ```python
     # utils/string_utils.py
     def reverse_string(text: str) -> str:
         """Reverse a string."""
         return text[::-1]
     
     def count_words(text: str) -> int:
         """Count words in a string."""
         return len(text.split())
     ```
   - Use the module in a script:
     ```python
     # main.py
     from utils.string_utils import reverse_string, count_words
     
     text: str = "Hello, Python!"
     print(f"Reversed: {reverse_string(text)}")  # Output: Reversed: !nohtyP ,olleH
     print(f"Word count: {count_words(text)}")  # Output: Word count: 2
     ```

2. **Using Standard Library Modules**:
   ```python
   import math
   import datetime
   
   def calculate_circle_area(radius: float) -> float:
       """Calculate area of a circle."""
       return math.pi * radius ** 2
   
   def get_current_date() -> str:
       """Return current date as a string."""
       return str(datetime.date.today())
   
   print(f"Circle area (r=5): {calculate_circle_area(5):.2f}")  # Output: Circle area (r=5): 78.54
   print(f"Today: {get_current_date()}")  # Output: Today: 2025-07-25
   ```

3. **Creating a Package**:
   - Create a package structure in `day2_project`:
     ```
     day2_project/
     ├── utils/
     │   ├── __init__.py  # Empty file to mark as package
     │   ├── string_utils.py
     │   ├── math_utils.py
     ├── files/
     ├── main.py
     ```
   - Create `utils/math_utils.py`:
     ```python
     # utils/math_utils.py
     def factorial(n: int) -> int:
         """Calculate factorial of a number."""
         if n == 0:
             return 1
         return n * factorial(n - 1)
     ```
   - Use the package in `main.py`:
     ```python
     # main.py
     from utils.string_utils import reverse_string
     from utils.math_utils import factorial
     
     print(reverse_string("Python"))  # Output: nohtyP
     print(f"Factorial of 5: {factorial(5)}")  # Output: Factorial of 5: 120
     ```

4. **Installing External Packages**:
   ```python
   # Install requests package (run in terminal: pip install requests)
   import requests
   
   def fetch_webpage(url: str) -> str:
       """Fetch the title of a webpage."""
       try:
           response = requests.get(url)
           return response.text[:100]  # First 100 characters
       except requests.RequestException:
           return "Error fetching webpage"
   
   print(fetch_webpage("https://example.com"))  # Output: First 100 chars of webpage
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `modules.py` in your `day2_project` folder and a new module `utils/data_utils.py` that:
1. Defines a function `process_user_data` in `data_utils.py` that:
   - Takes a list of dictionaries (user data with “name” and “score” keys).
   - Returns a tuple of (average score, set of names with scores above 75).
2. In `modules.py`:
   - Prompts the user to input user data (e.g., “Alice:85,Bob:70”).
   - Calls `process_user_data` and prints the results.
   - Saves results to `files/user_results.txt`.
3. Includes type hints, docstrings, and error handling.

**Example Solution**:
- `utils/data_utils.py`:
  ```python
  from typing import List, Dict, Tuple, Set
  
  def process_user_data(users: List[Dict[str, any]]) -> Tuple[float, Set[str]]:
      """Process user data and return average score and high scorers."""
      try:
          scores = [user["score"] for user in users]
          avg_score = sum(scores) / len(scores) if scores else 0.0
          high_scorers = {user["name"] for user in users if user["score"] > 75}
          return avg_score, high_scorers
      except (KeyError, ZeroDivisionError):
          return 0.0, set()
  ```

- `modules.py`:
  ```python
  from typing import List, Dict
  from utils.data_utils import process_user_data
  
  def main() -> None:
      """Collect user data, process it, and save results."""
      try:
          input_str: str = input("Enter user data (e.g., Alice:85,Bob:70): ")
          users: List[Dict[str, any]] = [
              {"name": item.split(":")[0].strip(), "score": float(item.split(":")[1].strip())}
              for item in input_str.split(",")
          ]
          
          avg_score, high_scorers = process_user_data(users)
          result = f"Average score: {avg_score:.2f}\nHigh scorers: {high_scorers}"
          print(result)
          
          with open("files/user_results.txt", "w") as file:
              file.write(result)
      except (ValueError, IndexError):
          print("Error: Please enter valid name:score pairs.")
  
  main()
  ```

**Task**:
- Create the `utils` package with `__init__.py` if not already done.
- Run the script with inputs (e.g., “Alice:85,Bob:70,Charlie:90”).
- Test with invalid inputs (e.g., “Alice:abc”) to verify error handling.
- Add a loop in `modules.py` to process another set of users until “done”.

**Expected Output** (for “Alice:85,Bob:70,Charlie:90”):
```
Enter user data (e.g., Alice:85,Bob:70): Alice:85,Bob:70,Charlie:90
Average score: 81.67
High scorers: {'Alice', 'Charlie'}
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to create and use modules and packages, organizing code for reusability and integrating with file I/O. You reinforced explicit practices with type hints and docstrings. Tomorrow, we’ll cover **exception handling**, diving deeper into robust error management for reliable programs.

#### Homework
- Modify `modules.py` to:
  - Validate scores are between 0 and 100.
  - Append results to `files/user_results.txt` instead of overwriting.
- Experiment with modules:
  - Create a new module `utils/text_utils.py` with a function to capitalize words in a string.
  - Use it in `modules.py` to capitalize user names before processing.
- Read the [Python documentation on modules](https://docs.python.org/3/tutorial/modules.html) (~5 minutes).
- Reflect on how modules in today’s exercise improved code organization compared to Day 9’s single-file approach.

---

#### Notes
- The Week 2 test (Days 1–6) was scheduled for last Saturday. Since it’s 1:28 AM EAT on Friday, July 25, 2025, I assume you’re continuing lessons. If you want the test or a review, let me know!
- The Week 4 test (Days 1–10) is scheduled for Saturday, August 2, 2025, covering today’s modules and packages.
- Ensure your virtual environment is active and the `utils` package is set up.

Let me know if you need the Week 2 test, help with the exercise, or have questions about modules and packages!


### Day 12: Exception Handling in Python

#### Objective
Learn how to handle errors in Python using **exception handling** to create robust and reliable programs. Building on Day 11’s modules and packages, exception handling ensures your code gracefully manages errors, a critical skill for professional applications like data processing, web development, and automation.

---

#### Lecture (10 minutes)
**Exceptions** are errors that occur during program execution (e.g., dividing by zero, accessing a non-existent file). Python’s exception handling allows you to catch and manage these errors, preventing crashes and improving user experience.

- **Key Concepts**:
  - **Try-Except**: Use `try` to wrap code that might fail and `except` to handle specific exceptions.
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    ```
  - **Multiple Exceptions**: Handle different errors with multiple `except` blocks or a tuple of exceptions.
  - **Else and Finally**:
    - `else`: Runs if no exception occurs.
    - `finally`: Runs regardless of exceptions (e.g., for cleanup).
  - **Raising Exceptions**: Use `raise` to trigger custom errors.
  - **Custom Exceptions**: Define your own exception classes for specific cases.
  - **Best Practices**:
    - Catch specific exceptions, not general ones (e.g., `except ValueError` over `except`).
    - Use explicit error messages and logging.
    - Combine with type hints and docstrings for clarity.
- **Why This Matters**:
  Exception handling is essential for robust software, ensuring programs handle edge cases (e.g., invalid user input, missing files) gracefully. It’s critical in professional settings like APIs, data pipelines, and user-facing applications.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code. Use the `utils` package and `files` folder from previous days.

1. **Basic Try-Except**:
   ```python
   def safe_divide(a: float, b: float) -> float:
       """Divide a by b, handling division errors."""
       try:
           return a / b
       except ZeroDivisionError:
           return float('inf')
   
   print(safe_divide(10.0, 2.0))  # Output: 5.0
   print(safe_divide(10.0, 0.0))  # Output: inf
   ```

2. **Multiple Exceptions**:
   ```python
   def parse_number(text: str) -> float:
       """Convert text to float, handling errors."""
       try:
           return float(text)
       except (ValueError, TypeError):
           return 0.0
   
   print(parse_number("123.45"))  # Output: 123.45
   print(parse_number("abc"))  # Output: 0.0
   ```

3. **Else and Finally**:
   ```python
   def read_file_content(filename: str) -> str:
       """Read file content, handling file errors."""
       try:
           with open(filename, 'r') as file:
               content = file.read()
       except FileNotFoundError:
           return "Error: File not found"
       else:
           return f"Content: {content[:50]}"  # First 50 chars
       finally:
           print("File operation completed")
   
   print(read_file_content("files/student.txt"))  # Output: Content: ... (if file exists)
   print(read_file_content("files/nonexistent.txt"))  # Output: Error: File not found
   ```

4. **Raising Exceptions**:
   ```python
   def restrict_age(age: int) -> None:
       """Restrict access based on age."""
       if age < 18:
           raise ValueError("Age must be 18 or older")
       print("Access granted")
   
   try:
       restrict_age(16)
   except ValueError as e:
       print(f"Error: {e}")  # Output: Error: Age must be 18 or older
   ```

5. **Custom Exceptions**:
   ```python
   class InvalidScoreError(Exception):
       """Custom exception for invalid scores."""
       pass
   
   def validate_score(score: float) -> None:
       """Validate a score is between 0 and 100."""
       if not 0 <= score <= 100:
           raise InvalidScoreError(f"Score {score} must be between 0 and 100")
       print("Valid score")
   
   try:
       validate_score(150)
   except InvalidScoreError as e:
       print(f"Error: {e}")  # Output: Error: Score 150 must be between 0 and 100
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `exceptions.py` in your `day2_project` folder and a module `utils/validation_utils.py` that:
1. Defines a function `process_sales` in `validation_utils.py` that:
   - Takes a list of sales (dictionaries with “item” and “amount” keys).
   - Validates that amounts are positive, raising a custom `InvalidSaleError` if not.
   - Returns a tuple of (total sales, set of items with sales above $100).
   - Saves valid sales to `files/sales.txt`.
2. In `exceptions.py`:
   - Prompts the user to input sales data (e.g., “apple:50,banana:-10”).
   - Calls `process_sales` and handles exceptions.
3. Includes type hints, docstrings, and error handling.

**Example Solution**:
- `utils/validation_utils.py`:
  ```python
  from typing import List, Dict, Tuple, Set
  
  class InvalidSaleError(Exception):
      """Custom exception for invalid sale amounts."""
      pass
  
  def process_sales(sales: List[Dict[str, float]], filename: str) -> Tuple[float, Set[str]]:
      """Process sales, validate amounts, and save to file."""
      try:
          for sale in sales:
              if sale["amount"] <= 0:
                  raise InvalidSaleError(f"Invalid amount {sale['amount']} for {sale['item']}")
          
          total_sales = sum(sale["amount"] for sale in sales)
          high_sales = {sale["item"] for sale in sales if sale["amount"] > 100}
          
          with open(filename, 'w') as file:
              for sale in sales:
                  file.write(f"{sale['item']}: ${sale['amount']:.2f}\n")
          
          return total_sales, high_sales
      except (InvalidSaleError, FileNotFoundError) as e:
          return 0.0, set()
  ```

- `exceptions.py`:
  ```python
  from typing import List, Dict
  from utils.validation_utils import process_sales, InvalidSaleError
  
  def main() -> None:
      """Collect sales data and process results."""
      try:
          input_str: str = input("Enter sales (e.g., apple:50,banana:150): ")
          sales: List[Dict[str, float]] = [
              {"item": item.split(":")[0].strip(), "amount": float(item.split(":")[1].strip())}
              for item in input_str.split(",")
          ]
          
          total, high_sales = process_sales(sales, "files/sales.txt")
          print(f"Total sales: ${total:.2f}")
          print(f"High-value items: {high_sales}")
      except (ValueError, IndexError):
          print("Error: Please enter valid item:amount pairs.")
      except InvalidSaleError as e:
          print(f"Error: {e}")
  
  main()
  ```

**Task**:
- Run the script with inputs (e.g., “apple:50,banana:150,orange:-10”).
- Test with invalid inputs (e.g., “apple:abc”) to verify error handling.
- Add a loop in `exceptions.py` to process another set of sales until “done”.

**Expected Output** (for “apple:50,banana:150”):
```
Enter sales (e.g., apple:50,banana:150): apple:50,banana:150
Total sales: $200.00
High-value items: {'banana'}
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to handle exceptions with `try`, `except`, `else`, `finally`, and custom exceptions, integrating them with modules and file I/O. You reinforced explicit practices with type hints and error messages. Tomorrow, we’ll explore **advanced data structures** (e.g., stacks, queues), building on lists and other collections for algorithmic problem-solving.

#### Homework
- Modify `exceptions.py` to:
  - Validate that item names are non-empty.
  - Log errors to `files/errors.txt` instead of printing them.
- Experiment with exceptions:
  - Write a script that attempts to read a non-existent file and handles `FileNotFoundError`.
  - Raise a custom exception for invalid user input (e.g., negative numbers).
- Read the [Python documentation on exceptions](https://docs.python.org/3/tutorial/errors.html) (~5 minutes).
- Reflect on how exception handling in today’s exercise improved robustness compared to Day 10’s string processing.

---

#### Notes
- The Week 2 test (Days 1–6) was scheduled for last Saturday. Since it’s 1:29 AM EAT on Friday, July 25, 2025, I assume you’re continuing lessons. If you want the test or a review, let me know!
- The Week 4 test (Days 1–10) is tomorrow, Saturday, August 2, 2025. I can provide a sample test after this lesson if you’re ready.
- Ensure your virtual environment is active and the `files` and `utils` folders are set up.

Let me know if you need the Week 2 or Week 4 test, help with the exercise, or have questions about exception handling!


**Note**: It seems there’s a discrepancy in the date provided (Friday, July 25, 2025, vs. the expected timeline where Day 12 aligns with August 1, 2025, and the Week 4 test is scheduled for tomorrow, August 2, 2025). I’ll proceed with **Day 13: Advanced Data Structures** as the next logical topic in the curriculum, assuming we’re continuing the daily progression. If you meant to address the Week 4 test or revisit a specific topic, please clarify!

---

### Day 13: Advanced Data Structures in Python

#### Objective
Learn how to implement and use **advanced data structures** like stacks, queues, and linked lists in Python. Building on Day 12’s exception handling and Day 7’s lists/tuples, these structures are crucial for algorithmic problem-solving and professional applications like task scheduling, graph traversal, and system design.

---

#### Lecture (10 minutes)
**Advanced data structures** extend Python’s built-in types (lists, dictionaries, etc.) to handle specific use cases efficiently:
- **Stacks**: Last-In, First-Out (LIFO) structure.
  - Use cases: Undo operations, backtracking algorithms.
  - Implementation: Use a list with `append()` (push) and `pop()` (pop).
- **Queues**: First-In, First-Out (FIFO) structure.
  - Use cases: Task scheduling, breadth-first search.
  - Implementation: Use `collections.deque` for efficient appends/pops from both ends.
- **Linked Lists**: Nodes with data and pointers to the next node.
  - Use cases: Dynamic memory allocation, implementing other structures.
  - Implementation: Custom classes for nodes and lists.
- **Key Concepts**:
  - **Efficiency**: Choose the right structure for performance (e.g., `deque` for queues vs. lists).
  - **Explicitness**: Use clear method names and type hints.
  - **Error Handling**: Validate inputs and handle edge cases (e.g., empty structures).
- **Why This Matters**:
  These structures are foundational for algorithms in software engineering, data science, and system design. They prepare you for technical interviews and building efficient programs.

---

#### Code Examples & Guided Practice (30 minutes)
Ensure your virtual environment (from Day 2) is activated in VS Code. Add to the `utils` package from Day 11.

1. **Stack Implementation (Using List)**:
   ```python
   # utils/stack.py
   from typing import List, TypeVar, Generic
   
   T = TypeVar('T')
   
   class Stack(Generic[T]):
       """A simple stack implementation using a list."""
       def __init__(self) -> None:
           self.items: List[T] = []
       
       def push(self, item: T) -> None:
           """Add an item to the top of the stack."""
           self.items.append(item)
       
       def pop(self) -> T:
           """Remove and return the top item."""
           if self.is_empty():
               raise ValueError("Stack is empty")
           return self.items.pop()
       
       def is_empty(self) -> bool:
           """Check if the stack is empty."""
           return len(self.items) == 0
   ```

   Test it:
   ```python
   # main.py
   from utils.stack import Stack
   
   stack: Stack[int] = Stack()
   stack.push(1)
   stack.push(2)
   print(stack.pop())  # Output: 2
   print(stack.pop())  # Output: 1
   print(stack.is_empty())  # Output: True
   ```

2. **Queue Implementation (Using `deque`)**:
   ```python
   # utils/queue.py
   from collections import deque
   from typing import TypeVar, Generic
   
   T = TypeVar('T')
   
   class Queue(Generic[T]):
       """A queue implementation using deque."""
       def __init__(self) -> None:
           self.items: deque[T] = deque()
       
       def enqueue(self, item: T) -> None:
           """Add an item to the rear of the queue."""
           self.items.append(item)
       
       def dequeue(self) -> T:
           """Remove and return the front item."""
           if self.is_empty():
               raise ValueError("Queue is empty")
           return self.items.popleft()
       
       def is_empty(self) -> bool:
           """Check if the queue is empty."""
           return len(self.items) == 0
   ```

   Test it:
   ```python
   # main.py
   from utils.queue import Queue
   
   queue: Queue[str] = Queue()
   queue.enqueue("task1")
   queue.enqueue("task2")
   print(queue.dequeue())  # Output: task1
   print(queue.dequeue())  # Output: task2
   print(queue.is_empty())  # Output: True
   ```

3. **Linked List Implementation**:
   ```python
   # utils/linked_list.py
   from typing import Optional, TypeVar
   
   T = TypeVar('T')
   
   class Node(Generic[T]):
       """A node in a singly linked list."""
       def __init__(self, data: T) -> None:
           self.data: T = data
           self.next: Optional[Node[T]] = None
   
   class LinkedList(Generic[T]):
       """A singly linked list implementation."""
       def __init__(self) -> None:
           self.head: Optional[Node[T]] = None
       
       def append(self, data: T) -> None:
           """Append a node to the end of the list."""
           new_node = Node(data)
           if not self.head:
               self.head = new_node
               return
           current = self.head
           while current.next:
               current = current.next
           current.next = new_node
       
       def display(self) -> list[T]:
           """Return list of node data."""
           result: list[T] = []
           current = self.head
           while current:
               result.append(current.data)
               current = current.next
           return result
   ```

   Test it:
   ```python
   # main.py
   from utils.linked_list import LinkedList
   
   ll: LinkedList[int] = LinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   print(ll.display())  # Output: [1, 2, 3]
   ```

---

#### Hands-On Exercise (15 minutes)
Create a script `data_structures.py` in your `day2_project` folder that:
1. Uses the `Stack` and `Queue` classes from `utils/stack.py` and `utils/queue.py`.
2. Defines a function `process_tasks` that:
   - Takes a list of tasks (strings) and processes them using a stack and a queue.
   - Returns a tuple of (stack-processed tasks in reverse order, queue-processed tasks in original order).
   - Saves both results to `files/task_results.txt`.
3. Prompts the user to input tasks (comma-separated, e.g., “task1,task2,task3”).
4. Includes type hints, docstrings, and error handling.

**Example Solution**:
- Ensure `utils/stack.py` and `utils/queue.py` exist as shown above.
- `data_structures.py`:
  ```python
  from typing import List, Tuple
  from utils.stack import Stack
  from utils.queue import Queue
  
  def process_tasks(tasks: List[str], filename: str) -> Tuple[List[str], List[str]]:
      """Process tasks using stack and queue, save to file."""
      try:
          # Process with stack (LIFO)
          stack: Stack[str] = Stack()
          for task in tasks:
              stack.push(task)
          stack_result: List[str] = []
          while not stack.is_empty():
              stack_result.append(stack.pop())
          
          # Process with queue (FIFO)
          queue: Queue[str] = Queue()
          for task in tasks:
              queue.enqueue(task)
          queue_result: List[str] = []
          while not queue.is_empty():
              queue_result.append(queue.dequeue())
          
          # Save to file
          with open(filename, 'w') as file:
              file.write(f"Stack (LIFO): {stack_result}\n")
              file.write(f"Queue (FIFO): {queue_result}\n")
          
          return stack_result, queue_result
      except (ValueError, FileNotFoundError) as e:
          print(f"Error: {e}")
          return [], []
  
  def main() -> None:
      """Collect tasks and display results."""
      try:
          input_str: str = input("Enter tasks (e.g., task1,task2,task3): ")
          tasks: List[str] = [task.strip() for task in input_str.split(",")]
          
          stack_tasks, queue_tasks = process_tasks(tasks, "files/task_results.txt")
          print(f"Stack processed (LIFO): {stack_tasks}")
          print(f"Queue processed (FIFO): {queue_tasks}")
      except ValueError:
          print("Error: Please enter valid tasks.")
  
  main()
  ```

**Task**:
- Ensure the `utils` package has `stack.py` and `queue.py`.
- Run the script with inputs (e.g., “task1,task2,task3”).
- Test with empty input to verify error handling.
- Add a loop in `main()` to process another set of tasks until “done”.

**Expected Output** (for “task1,task2,task3”):
```
Enter tasks (e.g., task1,task2,task3): task1,task2,task3
Stack processed (LIFO): ['task3', 'task2', 'task1']
Queue processed (FIFO): ['task1', 'task2', 'task3']
```

---

#### Summary & Preview (5 minutes)
Today, you learned how to implement and use stacks, queues, and linked lists, integrating them with file I/O and modules. You reinforced explicit practices with type hints and error handling. Tomorrow, we’ll cover **regular expressions** in depth, building on Day 10’s introduction for advanced text processing.

#### Homework
- Modify `data_structures.py` to:
  - Validate that tasks are non-empty strings.
  - Add a feature to count the number of tasks processed by each structure.
- Experiment with data structures:
  - Create a linked list with 5 numbers and print it in reverse order (by modifying `LinkedList`).
  - Use a stack to reverse a string input by the user.
- Read the [Python documentation on `collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque) (~5 minutes).
- Reflect on how stacks vs. queues in today’s exercise suit different use cases (e.g., undo vs. task scheduling).

---

#### Notes
- The Week 4 test (Days 1–10: history, setup, variables, data types, operators, control flow, functions, lists/tuples, dictionaries/sets, file I/O, strings, modules) is scheduled for tomorrow, Saturday, August 2, 2025. I can provide a sample test after this lesson if you’re ready.
- If you missed the Week 2 test (Days 1–6), let me know to provide it.
- Ensure your virtual environment is active and the `utils` and `files` folders are set up.

Let me know if you want the Week 4 test now, need help with the exercise, or have questions about advanced data structures!


