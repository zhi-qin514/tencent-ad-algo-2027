class SimpleArray:
    def __init__(self, capacity=4):
        # 填空 1：创建一个固定长度的列表，预填充 None
        self._data = [None] *capacity  # 提示：[None] * capacity
        self.size = 0              # 实际用了多少个位置
        self.capacity = capacity   # 总容量
    
    def append(self, value):
        if self.size == self.capacity:
            # 填空 2：打印"扩容"，并把 capacity 翻倍
            print(f"Expansion: {self.capacity} -> {self.capacity * 2}")
            self.capacity = self.capacity * 2  # 翻倍
            # 填空 3：创建新列表，把旧数据拷贝过去
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self._data[i]  # self._data[i]
            self._data = new_data
        
        self._data[self.size] = value
        self.size += 1
    
    def show(self):
        # 只打印有效部分
        print(self._data[:self.size])


# 测试
arr = SimpleArray(capacity=2)
for i in range(6):
    arr.append(i * 10)
    arr.show()