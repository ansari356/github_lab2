class Stack:
    def __init__(self) -> None:
        self.data_list = []

    def push(self, data):
        self.data_list.append(data)

    def pop(self):
        if self.is_Empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.data_list.pop()

    def peek(self):
        if self.is_Empty():
            raise IndexError("Cannot peek an empty stack")
        return self.data_list[-1]

    def is_Empty(self):
        return len(self.data_list) == 0

    def size(self):
        return len(self.data_list)

    def print(self):
        print_data = ""
        for item in reversed(self.data_list):
            print_data += str(item) + "->"
        print(print_data)

s = Stack()
for i in range(1, 10):
    s.push(i)

s.print()
print(s.pop())
# print(f"peek = {s.peek()}")
# print(f"pop = {s.pop()}")
# print(f"isEmpty = {s.is_Empty()}")
# print(f"size = {s.size()}")
s.print()


