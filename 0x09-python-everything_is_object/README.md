# 0x09. Python - Everything is object

## Description
This project dives deep into one of the core ideas of Python: **everything in Python is an object**.  
You will explore how Python handles variables, objects, references, assignments, and how mutability affects behavior.  
The tasks focus on answering theoretical questions about Python’s object model and require you to think carefully before testing in the interpreter.

---

## Learning Objectives
By the end of this project, you should be able to explain, without using external resources:

- Why Python programming is awesome.
- What is an object.
- The difference between a **class** and an **object/instance**.
- The difference between **immutable** and **mutable** objects.
- What a **reference** is in Python.
- What **assignment** means in Python.
- What an **alias** is and how it affects variables.
- How to check if two variables are identical.
- How to check if two variables are linked to the same object.
- How to display the variable identifier (memory address in CPython).
- Which Python types are **mutable** and which are **immutable**.
- How Python passes variables to functions.

---

## Resources
Read or watch:
- [Objects and values (9.10)](https://docs.python.org/3/tutorial/datastructures.html#)
- [Aliasing (9.11)](https://docs.python.org/3/tutorial/datastructures.html#)
- [Immutable vs mutable types](https://docs.python.org/3/reference/datamodel.html)
- **Mutation** (this chapter only)
- [Cloning lists (9.12)](https://docs.python.org/3/tutorial/datastructures.html#)
- [Python tuples: immutable but potentially changing](https://docs.python.org/3/tutorial/datastructures.html#)

---

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`.
- All files interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
- All files must end with a newline.
- First line of all scripts: `#!/usr/bin/python3`.
- Code must follow **pycodestyle (2.8.\*)**.
- All files must be executable.
- File length will be tested with `wc`.

### Answer Files
- Only one line.
- No shebang.
- Must end with a newline.

---

## Usage
The project is mainly **Q&A based**.  
Each answer must be placed in its corresponding `.txt` file with exactly one line.  
For Python scripts, make sure they are executable and respect the required format.

---

## Example
```python
>>> a = [1, 2, 3]
>>> b = a
>>> a[0] = 'x'
>>> b
['x', 2, 3]

