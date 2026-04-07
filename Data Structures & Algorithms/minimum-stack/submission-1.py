class MinStack:

    def __init__(self):
        self.arr=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.arr.append(val)

        if not self.minstack or val<=self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        rm=self.arr.pop()

        if self.minstack[-1]==rm:
            self.minstack.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minstack[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()