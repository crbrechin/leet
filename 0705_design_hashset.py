class MyHashSet:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        self.list.append(key)

    def remove(self, key: int) -> None:
        self.list = list(x for x in self.list if x != key)

    def contains(self, key: int) -> bool:
        return key in self.list


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
