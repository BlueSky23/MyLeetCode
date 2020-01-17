# 用字典存内容，用列表存顺序
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 保存顺序
        self.cache_list = []
        # 保存内容
        self.cache_dict = {}

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        # 更新最近最少使用的元素情况
        self.cache_list.remove(key)
        self.cache_list.append(key)
        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.cache_dict[key] = value
            self.cache_list.remove(key)
            self.cache_list.append(key)
            return
        # 最不常用的元素在0位置
        if len(self.cache_list) >= self.capacity:
            self.cache_dict.pop(self.cache_list[0])
            self.cache_list.pop(0)
        # 放入一个新的元素
        self.cache_dict[key] = value
        self.cache_list.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
