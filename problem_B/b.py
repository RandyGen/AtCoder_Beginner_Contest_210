import sys

c = 0

for row in sys.stdin:
  if c == 0:
    c = 1
  else:
    l = list(row)
    for i in range(len(l)):
      if l[i] == '1' and (i+1)%2 == 1:
        print('Takahashi')
        break
      elif l[i] == '1' and (i+1)%2 == 0:
        print('Aoki')
        break
