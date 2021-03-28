def tiles(n):
    if n==1: return 1
    elif n==2: return 2 
    else: return tiles(n-1)+tiles(n-2)

tiles(7)