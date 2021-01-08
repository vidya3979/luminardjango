class books:
    def __init__(self,pages):
        self.pages=pages
 #   def __str__(self):
  #      return str(self.pages)
    def __add__(self, other):
        return self.pages + other.pages
obj=books(100)
obj1=books(200)
print(obj+obj1)
