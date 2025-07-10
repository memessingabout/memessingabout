# **Comprehensive Python Guide (Based on "Automate the Boring Stuff with Python")**  

## **Introduction to Python**  
Python is a versatile, high-level programming language known for its readability and wide range of applications—from web development to data science and automation.  

### **Why Python?**  
- **Easy to Learn**: Simple syntax, resembling plain English.  
- **Cross-Platform**: Runs on Windows, macOS, and Linux.  
- **Large Ecosystem**: Rich standard library and third-party modules.  
- **Automation Power**: Perfect for scripting repetitive tasks.  

### **Key Concepts**  
- **Programming**: Writing instructions for a computer to execute.  
- **Source Code**: The actual text of a program.  
- **Python Interpreter**: Software that reads and executes Python code.  
- **Debugging**: Finding and fixing errors in code.  

### **Asking Smart Programming Questions**  
When stuck:  
1. Explain **what you're trying to achieve**, not just what you did.  
2. Specify **where the error occurs** (startup or after a specific action?).  
3. Share **the full error message** and relevant code (use [Pastebin](http://pastebin.com/) or [GitHub Gist](http://gist.github.com/)).  
4. Mention **what you’ve already tried**.  
5. State your **Python version and OS**.  

---

## **Chapter 1: Python Basics**  
### **Expressions & Operators**  
- **Expressions**: Combinations of values and operators (e.g., `2 + 3`).  
- **Operator Precedence**: Determines evaluation order:  
  | Operator | Operation          |  
  |----------|--------------------|  
  | `**`     | Exponentiation     |  
  | `%`      | Modulus (remainder)|  
  | `//`     | Floor division     |  
  | `/`      | Division           |  
  | `*`      | Multiplication     |  
  | `-`      | Subtraction        |  
  | `+`      | Addition           |  

### **Data Types**  
| Type      | Example       | Description                     |  
|-----------|--------------|---------------------------------|  
| `int`     | `42`         | Whole numbers                   |  
| `float`   | `3.14`       | Decimal numbers                 |  
| `str`     | `"Hello"`    | Text (single or double quotes)  |  
| `bool`    | `True/False` | Boolean (logical) values        |  

### **Variables & Naming Rules**  
- Store values for reuse (e.g., `x = 10`).  
- **Rules**:  
  1. One word (no spaces).  
  2. Only letters, numbers, and underscores (`_`).  
  3. Cannot start with a number.  
- **Case-sensitive**: `var` ≠ `Var`.  

### **Basic Functions**  
| Function    | Description                          | Example                   |  
|-------------|-------------------------------------|---------------------------|  
| `print()`   | Displays output                     | `print("Hello")`          |  
| `input()`   | Takes user input (returns a string) | `name = input("Name? ")`  |  
| `len()`     | Returns length of a string/list     | `len("Python")` → `6`     |  
| `str()`     | Converts to string                  | `str(100)` → `"100"`      |  
| `int()`     | Converts to integer                 | `int("50")` → `50`        |  
| `float()`   | Converts to float                   | `float("3.14")` → `3.14`  |  

---

## **Chapter 2: Flow Control**  
### **Boolean Logic**  
- **Comparison Operators**:  
  | Operator | Meaning          | Example (`x = 5`) |  
  |----------|------------------|-------------------|  
  | `==`     | Equal to         | `x == 5` → `True` |  
  | `!=`     | Not equal        | `x != 3` → `True` |  
  | `<`      | Less than        | `x < 10` → `True` |  
  | `>`      | Greater than     | `x > 2` → `True`  |  
  | `<=`     | Less or equal    | `x <= 5` → `True` |  
  | `>=`     | Greater or equal | `x >= 5` → `True` |  

- **Boolean Operators**:  
  - `and`: Both conditions must be `True`.  
  - `or`: At least one condition must be `True`.  
  - `not`: Inverts the Boolean value.  

### **Conditional Statements**  
- **`if` Statement**:  
  ```python
  if condition:
      # Code block executes if True
  ```  
- **`elif` (Else If)**:  
  ```python
  if x > 10:
      print("Big")
  elif x > 5:
      print("Medium")
  else:
      print("Small")
  ```  
- **`else`**: Runs if all other conditions are `False`.  

### **Loops**  
- **`while` Loop**:  
  ```python
  while condition:
      # Runs until condition is False
  ```  
- **`for` Loop with `range()`**:  
  ```python
  for i in range(5):  # 0, 1, 2, 3, 4
      print(i)
  ```  
  - `range(start, stop, step)` (e.g., `range(1, 10, 2)` → `1, 3, 5, 7, 9`).  
- **`break`**: Exits loop immediately.  
- **`continue`**: Skips to next iteration.  

### **Importing Modules**  
- **Standard Library**: Pre-installed modules (e.g., `math`, `random`).  
- **Syntax**:  
  ```python
  import math
  print(math.sqrt(16))  # 4.0
  ```  
  Or:  
  ```python
  from math import sqrt
  print(sqrt(16))  # 4.0
  ```  

---
