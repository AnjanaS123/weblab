file1=open("demo.txt","r")
content=file1.read()
print(content)
file1.close()
file1=open("demo.txt","a")
file1.write("i am 20 years old")
file1.close()


