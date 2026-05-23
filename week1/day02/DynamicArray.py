# 模拟c语言中使用malloc函数构建的动态数组
class DynamicArray:

    def __init__(self, initial_capacity=4):
        """初始化：模拟 malloc(initial_capacity)"""
        self.capacity = initial_capacity
        self.size = 0
        self._data = [None] * self.capacity  # 预分配，避免频繁扩容
    
    def append(self, value):
        """追加元素：满了就扩容"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # 容量翻倍，模拟 realloc
        self._data[self.size] = value
        self.size += 1
    
    def _resize(self, new_capacity):
        """内部方法：模拟 realloc + memcpy"""
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[i]  # 逐个拷贝，模拟 memcpy
        self._data = new_data
        self.capacity = new_capacity
        print(f"扩容: {self.capacity // 2} -> {self.capacity}")  # 观察扩容时机
    
    def __getitem__(self, index):
        """支持 arr[i] 访问"""
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")
        return self._data[index]
    
    def __len__(self):
        """支持 len(arr)"""
        return self.size
    
    def __str__(self):
        """打印时只看有效元素"""
        return str(self._data[:self.size])


# ========== 测试代码 ==========
if __name__ == "__main__":
    arr = DynamicArray(initial_capacity=2)  # 小容量方便观察扩容
    
    for i in range(10):
        arr.append(i * 10)
        print(f"追加 {i*10}, size={len(arr)}, capacity={arr.capacity}")
    
    print("\n最终数组:", arr)
    print("访问 arr[3]:", arr[3])