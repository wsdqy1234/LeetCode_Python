a = [5, 9, 1, 2, 10, 4, 3]
num = len(a)
# 选择排序法
for i in range(num):
    tmp_min = i #先确定第i个为最小
    for j in range(i+1, num):
        if a[j]<a[tmp_min]: # 找i以后的有没有更小的，把最小的找出来
            tmp_min = j
    # 最小的换到i位置
    tmp = a[i]
    a[i] = a[tmp_min]
    a[tmp_min] = tmp
print(a)