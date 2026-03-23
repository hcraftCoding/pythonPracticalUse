"""
Practice 2: finally as a cleanup tool
Program: "finallyForCleanUpPractice.py"
Author: Hunter Craft
3/22/2026

def read_file(filename):
    # write a try/except/finally block that:
    # - tries to open and print the contents of the file
    # - catches FileNotFoundError with a clean message
    # - always prints "file operation complete" in finally
    pass
"""
import json

def read_file(filename):
    try:
        with open(filename, "r") as f:
            file_contents = json.load(f)
            print(file_contents)
    except FileNotFoundError:
        print("File Not Found")
    finally:
        print("file operation complete")
    # - tries to open and print the contents of the file
    # - catches FileNotFoundError with a clean message
    # - always prints "file operation complete" in finally
    

read_file("response.json")    # this one exists
read_file("fake_file.json")   # this one doesn't