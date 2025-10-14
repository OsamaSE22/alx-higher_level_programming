# 🐍 Python Inheritance — Practice & Notes

This repository contains exercises and notes to practice **Inheritance** in Python.

---

## 📘 What Is Inheritance?

**Inheritance** allows one class (called the *child* or *subclass*) to inherit the attributes and methods of another class (the *parent* or *base class*).

This helps with:
- **Code reuse** — write once, use many times.
- **Extensibility** — extend existing code without modifying it.
- **Organization** — build clear class hierarchies.

---

## 🧩 Basic Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Bobby")
print(dog.name)    # inherited from Animal
print(dog.speak()) # overridden in Dog

Output:
Bobby
Woof!
