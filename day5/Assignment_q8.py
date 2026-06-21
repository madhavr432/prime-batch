class player:
    count=0
    def __init__(self, name, level):
        player.count+=1
        self.name = name
        self.level = level
    def get_info(self):
        print(f"the name of player is {self.name} and level of player is {self.level}\n")
    def get_count(self):
        print(player.count)
p1 = player("madhav", 3)
p2 = player("rahul", 4)
p1.get_count()
p1.get_info()
p2.get_info()
        