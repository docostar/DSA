def fibonci(n):
    assert n>=0 and int(n)==n,"Number must be int and greater than zero"
    if n in [0,1]:
        return n
    else:
        return fibonci(n-1)+ fibonci(n-2)
    
print(fibonci(7))