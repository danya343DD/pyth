
class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price



class SmallHouse(House):
    def __init__(self, price):

        super().__init__(40, price)



class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age, money=0):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = None

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house}")

    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned {amount}. Total money: {self.__money}")

    def buy_house(self, house, discount=0):
        final_price = house.price * (1 - discount)

        if self.__money >= final_price:
            self.__money -= final_price
            self.__house = house
            print(f"House bought! Remaining money: {self.__money}")
        else:
            print("Warning: Not enough money to buy this house!")



print("=== Part 4: Execution ===\n")


print("1. Default info:")
Human.default_info()
print()


person = Human("Alice", 25, 5000)


print("2. Human object info:")
person.info()
print()


small_house = SmallHouse(50000)
print(f"3. SmallHouse created - Area: {small_house.area}m², Price: {small_house.price}")
print()


print("4. Trying to buy house with insufficient funds:")
person.buy_house(small_house)
print()


print("5. Earning money:")
person.earn_money(50000)
print()


print("6. Trying to buy house again:")
person.buy_house(small_house)
print()


print("7. Final human object state:")
person.info()