
class bank_details:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def get_balance(self):
        return self.balance
    def set_balance(self, newbalance):
        self.balance= newbalance
acc1 = bank_details("manan",200 )
query = input("Enter the query\n")
if(query=="deposite"):
    amt = int(input("Enter the deposite amount: "))
    newbalance = acc1.get_balance() + amt
    acc1.set_balance(newbalance)
    print(f"Your new balance is {acc1.get_balance()}")
elif(query == "withdraw"):
    amt = int(input("Enter the withdrawn amount: "))
    newbalance = acc1.get_balance() - amt
    acc1.set_balance(newbalance)
    print(f"Your new balance is {acc1.get_balance()}")
elif(query == "check balance"):
    print(f"Your balance is {acc1.get_balance()}")
    
        