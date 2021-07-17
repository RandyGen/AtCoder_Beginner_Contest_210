n, a, x, y = input().split()

if int(n) > int(a):
    ans = int(a) * int(x) + (int(n) - int(a)) * int(y)
else:
    ans = int(n) * int(x)
    

print(ans)