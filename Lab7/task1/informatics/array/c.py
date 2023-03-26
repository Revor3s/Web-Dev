n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(0,n-1):
    if arr[i]>=0:
        cnt+=1
print(cnt)