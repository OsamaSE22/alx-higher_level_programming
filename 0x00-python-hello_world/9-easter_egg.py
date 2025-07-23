#!/usr/bin/python3
print("The Zen of Python, by Tim Peters")
with open("a.txt", "r") as file:
    content = file.read()
print(content, end="")
