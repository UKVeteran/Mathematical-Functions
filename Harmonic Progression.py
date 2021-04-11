def w(i):
    if not isinstance(i, int) or i <=0: return False
    elif i == 1: return 1
    else: return(i-sum([j*w(j) for j in range (1, i)]))/i
    
S, x = 0, 0
    
while S <= 3:
    x+=1 
    S+=w(x)
        
    print (x)