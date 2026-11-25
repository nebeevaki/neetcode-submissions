class StockSpanner:

    def __init__(self):
        self.stack = [(100_001, 0)]

    def next(self, price: int) -> int:
        index = len(self.stack) - 1
        prev_price, prev_days = self.stack[index]
        while prev_price <= price:
            if prev_price <= price:
                index -= prev_days
            prev_price, prev_days = self.stack[index]
        self.stack.append((price, len(self.stack) - index))
        return len(self.stack) - index - 1


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)