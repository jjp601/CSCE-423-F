def treeDiameter(n, tree):
    n, t = eval(dir()[0])
    import scipy.sparse as s 
    g = s.lil_matrix((n,n))
    d = s.csgraph.dijkstra
    for i,j in t: g[i,j] = 1 
    return max(d(g,0,d(g,0,0).argmax()))