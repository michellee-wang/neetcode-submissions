class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # append to actual stack
        self.stack.append(val)
        
        #if self.min is empty, append
        if not self.min_stack:
            self.min_stack.append(val)
        # if value smaller than the last element, append
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)
        # append current smallest element agian
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]