from turtle import*
pensize(3)
clr=["blue","green"]
for n in range(4):
    rt(90)
    begin_fill()
    for i in range(40,101,20):
        circle(i)
        end_fill()
     
