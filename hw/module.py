#How will you know function, class variable of a particular module?
#Just replace math with any module (like os, sys, random) and it will list functions, classes, and variables separately.

import inspect
import math   # you can replace with any module

# Functions
print("Functions:")
for name, obj in inspect.getmembers(math, inspect.isfunction):
    print("  ", name)

# Classes
print("\nClasses:")
for name, obj in inspect.getmembers(math, inspect.isclass):
    print("  ", name)

# Variables / constants
print("\nVariables:")
for name, obj in inspect.getmembers(math):
    if not inspect.isfunction(obj) and not inspect.isclass(obj):
        print("  ", name)
