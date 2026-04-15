class StockSpanner:

    def __init__(self):
        self.s=[]


    def next(self, price: int) -> int:
        self.s.append(price)
        temp=self.s.copy()
        count=0
        while temp and temp[-1]<=price:
            # print("temp",temp)
            count+=1
            temp.pop()
        # print(count)
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)