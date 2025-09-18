class IntList:
    def __init__(self):
        self.data = []

    def _check_int(self, value):
        if not isinstance(value, int):
            raise TypeError("Only integers are allowed")

    def append(self, value: int):
        self._check_int(value)
        self.data.append(value)

    def remove(self, value: int):
        self._check_int(value)
        self.data.remove(value)  # raises ValueError if not found

    def pop(self, index: int = -1) -> int:
        return self.data.pop(index)

    def slice(self, start: int, end: int) -> list:
        return self.data[start:end]

    def __repr__(self):
        return str(self.data)

# Example
arr = IntList()
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)          # [10, 20, 30]
arr.remove(20)
print(arr)          # [10, 30]
print(arr.pop())    # 30
print(arr)          # [10]
print(arr.slice(0, 1))  # [10]
