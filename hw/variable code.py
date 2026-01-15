#
#Python with 4 functions — where the 4th function should always run — and whether execution depends on:
#the order of functions inside the class, or
#the number of parameters.
#🔹 Important Python rules
#Order of function definitions inside a class doesn’t matter → functions don’t “auto-run” just because they’re defined first or last.
#Functions (methods) only run when you call them.
#If you want a particular function (say the 4th one) to always execute, you must call it explicitly (e.g., in __init__ or after other functions).

#✅ Explanation
#It does not depend on the position of the function in the class.
#It does not depend on the number of parameters.
#A function only runs when called.
#If you want the 4th function to always run, you explicitly call it inside the other functions (or inside __init__).

class MyClass:
    def func1(self, a, b):
        print("Function 1: Add =", a + b)
        self.func4()   # calling func4

    def func2(self, a):
        print("Function 2: Square =", a * a)
        self.func4()   # calling func4

    def func3(self):
        print("Function 3: Just a message")
        self.func4()   # calling func4

    def func4(self):
        print("Function 4: This always executes!")

#Usage
obj = MyClass()
obj.func1(2, 3)   # calls func1, then func4
obj.func2(5)      # calls func2, then func4
obj.func3()       # calls func3, then func4
obj.func4()       # directly calling func4
