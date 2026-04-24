class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        a = []
        a.append(x)
        a.extend(self.queue)
        self.queue = a

    def pop(self) -> int:
        try:
            return self.queue.pop(0)
        except:
            return []

    def top(self) -> int:
        try:
            return int(self.queue[0])
        except:
            return None

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
