from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Pizza:
    def init(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def setDough(self, dough):
        self.dough = dough

    def setSauce(self, sauce):
        self.sauce = sauce

    def setTopping(self, topping):
        self.topping = topping

class PizzaBuilder:
    def getPizza(self):
        return self.pizza

    def createNewPizzaProduct(self):
        self.pizza = Pizza()

    def buildDough(self):
        pass

    def buildSauce(self):
        pass

    def buildTopping(self):
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def buildDough(self):
        self.pizza.setDough("thick")

    def buildSauce(self):
        self.pizza.setSauce("mild")

    def buildTopping(self):
        self.pizza.setTopping("ham + pineapple")

class SpicyPizzaBuilder(PizzaBuilder):
    def buildDough(self):
        self.pizza.setDough("thin")

        def buildSauce(self):
            self.pizza.setSauce("hot")

        def buildTopping(self):
            self.pizza.setTopping("pepperoni + salami")

        def list_parts(self):
            print(f"Product parts: {', '.join(self.pizza)}", end="")

class Waiter:
    def setPizzaBuilder(self, pizzaBuilder):
        self.pizzaBuilder = pizzaBuilder

    def getPizza(self):
        return self.pizzaBuilder.getPizza()

    def constructPizza(self):
        self.pizzaBuilder.createNewPizzaProduct()
        self.pizzaBuilder.buildDough()
        self.pizzaBuilder.buildSauce()
        self.pizzaBuilder.buildTopping()

    def constructPizzaWithoutSauce(self):
        self.pizzaBuilder.createNewPizzaProduct()
        self.pizzaBuilder.buildDough()
        self.pizzaBuilder.buildTopping()


if __name__ == "__main__":
    waiter = Waiter()
    print ("What kind of pizza to prepare")
    pizzaType = input("[h]HawaiianPizza [s]SpicyPizza: ")
    if pizzaType == "h":
        hawaiianPizzaBuilder = HawaiianPizzaBuilder()
        waiter.setPizzaBuilder(hawaiianPizzaBuilder)
        waiter.constructPizza()
    if pizzaType == "s":
        spicyPizzaBuilder = SpicyPizzaBuilder()
        waiter.setPizzaBuilder(spicyPizzaBuilder)
        waiter.constructPizza()
