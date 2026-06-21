class bankaccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance #private
    def get_balance(self):#getter
        return self.__balance
    def set_balance(self, newBalance):
        self.__balance = newBalance

acc1 = bankaccount("Rahul", 90000)
acc1.set_balance(200000)
print(acc1.name, acc1.get_balance())
