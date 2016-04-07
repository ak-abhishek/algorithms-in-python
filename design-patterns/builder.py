#!/usr/bin/env python


class Item(object):

    def name(self):
        raise NotImplementedError

    def packing(self):
        raise NotImplementedError

    def price(self):
        raise NotImplementedError


class Packing(object):

    def pack(self):
        raise NotImplementedError


class Wrapper(Packing):

    def pack(self):
        return "Wrapper"


class Bottle(Packing):

    def pack(self):
        return "Bottle"


class Burger(Item):

    def packing(self):
        return Wrapper()

    def price(self):
        raise NotImplementedError


class Drink(Item):

    def packing(self):
        return Bottle()

    def price(self):
        raise NotImplementedError


class VegBurger(Burger):

    def name(self):
        return "Veg-Burger"

    def price(self):
        return 20.5


class ChickenBurger(Burger):

    def name(self):
        return "Chicken-Burger"

    def price(self):
        return 50.2


class Coke(Drink):

    def name(self):
        return "Coke"

    def price(self):
        return 10


class Pepsi(Drink):

    def name(self):
        return "Pepsi"

    def price(self):
        return 9.5


class Meal(object):

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        self.total_cost = 0.0
        for item in self.items:
            self.total_cost += item.price()

        return self.total_cost

    def show_items(self):
        for item in self.items:
            print "Item Name:", item.name(), " Packing:", item.packing().pack(), " Price:", item.price()


class MealBuilder(object):

    def veg_meal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal

    def chiecken_meal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal


if __name__ == '__main__':
    meal_builder = MealBuilder()

    veg_meal = meal_builder.veg_meal()
    veg_meal.show_items()
    print "Total Cost: ", veg_meal.get_cost()

    chicken_meal = meal_builder.chiecken_meal()
    chicken_meal.show_items()
    print "Total Cost: ", chicken_meal.get_cost()
