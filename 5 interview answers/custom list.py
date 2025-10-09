lst = UndoableList()
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)  # [10, 20, 30]

lst.remove(20)
print(lst)  # [10, 30]

lst.undo()
print(lst)  # [10, 20, 30]

lst.redo()
print(lst)  # [10, 30]

lst.reverse()
print(lst)  # [30, 10]

lst.undo()
print(lst)  # [10, 30]
