for n in range(2,50):
    for x in range(2,n):
        if n % x == 0:
            print(n,'=',x,'*',n//x)
            for y in range(x+1,n):
                if n % y ==0:
                     if y > n//y:
                         break
                     print(n, '=', y, '*', n // y)
            break
    else:
        print(n,'is prime')