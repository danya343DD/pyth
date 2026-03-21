from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Кипятим воду...")

    def pour_in_cup(self):
        print("Наливаем в чашку...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True

class Espresso(Beverage):
    def brew(self):
        print("Завариваем эспрессо под давлением...")

    def add_condiments(self):
        print("Добавляем сахар...")

class Cappuccino(Beverage):
    def brew(self):
        print("Завариваем эспрессо...")

    def add_condiments(self):
        print("Добавляем взбитое молоко и пенку...")

class HotChocolate(Beverage):
    def brew(self):
        print("Растворяем какао-порошок...")

    def add_condiments(self):
        print("Добавляем зефирки и сливки...")

class Americano(Beverage):
    def brew(self):
        print("Завариваем эспрессо и добавляем воду...")

    def add_condiments(self):
        print("Добавляем сахар...")

class LatteMacchiato(Beverage):
    def brew(self):
        print("Наливаем молоко, затем вливаем эспрессо...")

    def add_condiments(self):
        print("Добавляем молочную пенку...")

class DoubleShotEspresso(Espresso):
    def brew(self):
        print("Завариваем первую порцию...")
        print("Завариваем вторую порцию...")

class HealthyCappuccino(Cappuccino):
    def customer_wants_condiments(self):
        return False

if __name__ == "__main__":
    drink = Cappuccino()
    drink.prepare_recipe()

    drink = HotChocolate()
    drink.prepare_recipe()

    drink = HealthyCappuccino()
    drink.prepare_recipe()

    drink = LatteMacchiato()
    drink.prepare_recipe()

    drink = DoubleShotEspresso()
    drink.prepare_recipe()