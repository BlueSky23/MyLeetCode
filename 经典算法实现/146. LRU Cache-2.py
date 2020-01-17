# 使用ordereddict类，其顺序可以通过dict.keys获取的key顺序获取

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        self.cache_dict.move_to_end(key)
        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_dict[key] = value
            self.cache_dict.move_to_end(key)
            return
        # 最不常用的元素在0位置
        if len(self.cache_dict) >= self.capacity:
            self.cache_dict.popitem(last=False)
        # 放入一个新的元素,在字典的最后面
        self.cache_dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
