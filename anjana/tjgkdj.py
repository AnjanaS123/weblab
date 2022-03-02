n=int(input("enter the integer number"));
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n/10
print("the reverse of a number is:",rev);
