class product:
    count =0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        product.count+=1
    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")
    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price*discount/100)
        print(f"final price = {final_price}")
p1 =product("phone", 10000)
p2 =product("laptop", 60000)
p3 =product("pen", 10)
query = input("Enter your query: ")
if (query == "phone"):
    p1.get_info()
elif (query == "laptop"):
    p2.get_info()
elif (query == "pen"):
    p3.get_info()
elif (query == "discount in phone"):
    p1.calc_discount(p1.price, 10)
elif (query == "discount in laptop"):
    p1.calc_discount(p2.price, 50)
elif (query == "discount in pen"):
    p1.calc_discount(p3.price, 10)