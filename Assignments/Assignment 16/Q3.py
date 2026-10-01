# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
#    size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.
class Shirt:
    size_level = {"small": 0, "medium": 1, "large": 2, "xlarge": 3}
    increase_percent = 10

    def __init__(self, sid=0, sname="Unknown", type="Unknown", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Destructor called: shirt '{self.sname}' removed")

    @staticmethod
    def calculate_price(total_amount, size):
        level = Shirt.size_level.get(size.lower(), 0)
        return total_amount + (total_amount * Shirt.increase_percent / 100) * level

    def show_shirt(self):
        print("--- Shirt Details ---")
        print(f"ID          : {self.sid}")
        print(f"Name        : {self.sname}")
        print(f"Type        : {self.type}")
        print(f"Size        : {self.size}")
        print(f"Base price  : {self.price}")
        print(f"Final price : {Shirt.calculate_price(self.price, self.size)}")


s1 = Shirt()
s2 = Shirt(1, "Raymond", "Formal", 1000, "small")
s3 = Shirt(2, "Levis", "Casual", 1000, "medium")
s4 = Shirt(3, "Allen Solly", "Formal", 1000, "large")
s5 = Shirt(4, "Peter England", "Formal", 1000, "xlarge")

for s in (s2, s3, s4, s5):
    s.show_shirt()

del s1
print("End of program")
