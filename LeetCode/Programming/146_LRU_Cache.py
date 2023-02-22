from collections import OrderedDict

class LRUCache:
    data = OrderedDict()
    count = 0
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()
        self.count = len(self.data.keys())

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        temp = self.data[key]
        del(self.data[key])
        self.data[key] = temp
        return temp

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            del(self.data[key])
            self.data[key] = value
        else:
            if self.count == self.capacity:
                self.data.popitem(last=False)
                self.count -= 1
            self.count+=1
            self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)