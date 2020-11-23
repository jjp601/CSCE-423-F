def minimalBasketPrice(maxPrice, vendorsDelivery, vendorsProducts):
    m, v, a, *z = eval(dir()[0])
    n = numpy
    v = n.argsort(v)
    a = n.r_[a]
    a[a<0] = 99 
    for j in v:
        z += j,
        t = a[z]
        if sum(t.min( 0)) <= m:
            return [*{*v[t.argmin( 0)]}]