class parent:
    def m1(self):
        print("inside parent")
class child:
    def m2(self):
        print("inside child")
class subchild(child):
    def m3(self):
        print("inside subchild")
sc=subchild()
sc.m3()
sc.m2()
