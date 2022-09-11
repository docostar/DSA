def sumdigit(n):
    assert n>0 and int(n)==n,"Numbe rmust be integer and positive"
    if n<10:
        return n
    else:
        return (n%10) + sumdigit(int(n/10))
    
    
print(sumdigit(355))