class MyHashSet:

    def __init__(self):
        self.my_set = dict()
        self.n = 10**9 + 7

    def add(self, key: int) -> None:
        self.my_set[key % self.n] = self.my_set.get(key % self.n, [])
        if key not in self.my_set[key % self.n]:
            self.my_set[key % self.n].append(key)

    def remove(self, key: int) -> None:
        if key % self.n in self.my_set and self.my_set[key % self.n] and key in self.my_set[key % self.n]:
            self.my_set[key % self.n].remove(key)

    def contains(self, key: int) -> bool:
        if key % self.n in self.my_set and key in self.my_set[key % self.n]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)