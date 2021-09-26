for i in range(1,input()): 
    print(*list(int(range(1,i+1))) + list(int(reversed(range(1,i)))), sep='', end='\n')