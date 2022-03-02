class a:
    def get1(self):
        print("i am a class")
class b:
    def get2(self):
        print("i am class")
class c(a,b):
    def put(self):
        print("yes i am inherit a and b")
        obj=c()
        obj.get1()
        obj.get2()
        obj.get3()
        obj.put()
