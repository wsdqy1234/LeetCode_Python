a = [5, 9, 1, 2, 10, 4, 3]
num = len(a)
# 插入排序法
for i in range(0, num-1):
    current = a[i+1] # 拿i+1的元素出来，与0:i的元素挨个比较
    preIdx = i # 从i开始比较
    while(preIdx >= 0 and current < a[preIdx]): # 一直移动序列的元素，直到current找到应该插入的位置
        a[preIdx+1] = a[preIdx]
        preIdx = preIdx - 1
    a[preIdx+1] = current # 插入元素
print(a)