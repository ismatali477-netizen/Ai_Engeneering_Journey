class MinStack:
    def __init__(self):
        self.stack = []
        # self.minimum= 0
    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def get_min(self):
        return self.stack[-1][1]
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(7)
print(stack.get_min())   # 2
stack.pop()
print(stack.get_min())   # 2
stack.pop()
print(stack.get_min())   # 5