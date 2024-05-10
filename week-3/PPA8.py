n  = int(input())
ans = ''

for i in range(1,n+1):
    # print(i +',')
    # print(type(i))
    ans += str(i)
    if i < n:
        ans += ','
print(ans)
