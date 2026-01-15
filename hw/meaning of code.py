#meaning of the code if __name__=="__main__":
#Meanin
# If the file is run directly (e.g. python myfile.py), then __name__ is set to "__main__".
#If the file is imported as a module in another file, then __name__ is set to the module’s name (e.g. "myfile").
#So the code inside if __name__ == "__main__": will only run when the file is executed directly, not when import

def greet():
    print("Hello from greet()!")

if __name__ == "__main__":
    print("This file is run directly!")
    greet()
