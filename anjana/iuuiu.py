def squaresum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum
    n=int(input("please enter an integer:\n"))
    print(squaresum(n))
