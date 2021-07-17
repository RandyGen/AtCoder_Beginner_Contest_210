# AC  * 14
# WA  *  3
# TLE *  7

import sys

c = 0
s = set()
ans = 0

for row in sys.stdin:
  if c == 0:
    k = row.split()
    k = int(k[-1])
    c = 1
  else:
    l = row.split()
    for i in range(len(l)-k+1):
      for j in range(k):
        s.add(l[i+j])
        if (len(s)+k-j) < k:
          break
      if ans < len(s):
        ans = len(s)
      if ans == k:
        break
      s = set()
    print(ans)