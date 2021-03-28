def f(x,y):
    if x==y: return x
    elif x>y: return f(y,x)
    else: return f(x, y-x)
    
f(66,770)