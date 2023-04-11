a = [5, 9, 1, 2, 10, 4, 3]
num = len(a)
# 冒泡排序法
for i in range(num):
    for j in range(0, num-1-i): #每次把最大的冒到最右边，因此只需要考虑[0, num-1-i]
        # 大的放到右边
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
print(a)