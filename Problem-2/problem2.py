def chatBot(a,b):
    f=lambda x:len({*x}&{*b})
    m=max([],*a,key=f)
    while f(m):
        _,*m=m
    return b+m