def bmiwh(height,weight):
    bmi=height/weight
    return bmi
height=float(input("height="))
weight=float(input("weight="))      
bmi=bmiwh(height,weight)
print("BMI is",bmi)
if bmi<=18:
    print("you are underweighted")
elif bmi<=29:
    print("you are heathy")
else:
    print("you are overweight")
    
