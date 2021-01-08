class bank:


    def create_acc(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount
        print("your account no.",self.acc_no,"has been credited with amt",amount,"\n","your avail balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient amt in ur acc")
        else:
            self.balance-=amount
            print("your account no.",self.acc_no,"has been debited with amt",amount,"\n","your avail balance",self.balance)

    def balance_enq(self):
        print("yur acc bal =",self.balance)


obj=bank()
obj.create_acc(100,"reji",3000)

obj.deposit(5000)
obj.withdraw(1000)

obj.balance_enq()