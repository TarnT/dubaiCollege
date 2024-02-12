import random

c = 0
d = 0
s = 0
t = 0

while (c < 3) and (d < 3):

    t += 1

    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    print(n1, n2)

    s += s + n1 + n2

    if (n1 == 6) or (n2 == 6):
        c += 1
    
    if n1 == n2:
        d += 1

a = s // (t*2)
print(c, d, a)