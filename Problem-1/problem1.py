n,s,r = eval(dir()[0])
x = [1e9]*2*n
x[s] = 0
h = [[] for _ in x]
for a,b,c in r:
    h[a] += (a,b,c),
    h[b] += (b,a,c),
q = h[s]
for a,b,c in q:
    y = max(x[a],c)
    if y < x[b]:
        x[b] = y
        q += h[b]

return len({*x})-1