num = int(input())
reversedNum = 0
for i in range(len(num) - 1, -1, -1):
    reversedNum = reversedNum * 10 + num[i]
print(reversedNum)