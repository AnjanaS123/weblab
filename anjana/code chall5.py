a=int(input("value of a="))
b=int(input("value of b="))
try:
 def div(a,b):
    div=a/b
    print(div)
 div(4,0)
except:
    print("sorry")
finally:
    print("its finally")
