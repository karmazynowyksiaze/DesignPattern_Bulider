"""
Imie i naziwsko: Pawel Pawlowski
Grupa C7
Numer indeksu: 14073
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def pizzaDough(self) -> None:
        pass

    @abstractmethod
    def pizzaSauce(self) -> None:
        pass

    @abstractmethod
    def pizzaTopping(self) -> None:
        pass

class ConcreteBuilderH(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = HawaiianPizza()

    @property
    def product(self) -> HawaiianPizza:
        product = self._product
        self.reset()
        return product

    def pizzaDough(self) -> None:
        self._product.add("thick")

    def pizzaSauce(self) -> None:
        self._product.add("mild")

    def pizzaTopping(self) -> None:
        self._product.add("ham + pineapple")

class ConcreteBuilderS(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = HawaiianPizza()

    @property
    def product(self) -> SpicyPizza:
        product = self._product
        self.reset()
        return product

    def pizzaDough(self) -> None:
        self._product.add("thin")

    def pizzaSauce(self) -> None:
        self._product.add("hot")

    def pizzaTopping(self) -> None:
        self._product.add("salami + pepperoni")

class HawaiianPizza():
    def __init__(self) -> None:
        self.elements = []

    def add(self, part: Any) -> None:
        self.elements.append(part)

    def list_elements(self) -> None:
        print(f"Pizza elements: {', '.join(self.elements)}", end="")

class SpicyPizza():
    def __init__(self) -> None:
        self.elements = []

    def add(self, part: Any) -> None:
        self.elements.append(part)

    def list_elements(self) -> None:
        print(f"Pizza elements: {', '.join(self.elements)}", end="")

class Waiter():
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_pizza(self) -> None:
        self.builder.pizzaDough()

    def build_full_pizza(self) -> None:
        self.builder.pizzaDough()
        self.builder.pizzaSauce()
        self.builder.pizzaTopping()

if __name__ == "__main__":
    print("\t\tDesignPattern_Builder\n")

    pizzaType =input("{h}HawaiianPizza {s}SpicyPizza  ")
    if pizzaType == "h":
        waiter = Waiter()
        builder = ConcreteBuilderH()
        waiter.builder = builder

        print("\nHawaiian Pizza ")
        waiter.build_full_pizza()
        builder.product.list_elements()
        print("\n")

        print("Custom Hawaiian Pizza elements")
        builder.pizzaDough()
        builder.pizzaSauce()
        builder.product.list_elements()

    if pizzaType == "s":
        waiter = Waiter()
        builder = ConcreteBuilderS()
        waiter.builder = builder

        print("\nSpicy Pizza ")
        waiter.build_full_pizza()
        builder.product.list_elements()

        print("\n")

        print("Custom Spicy Pizza elements")
        builder.pizzaDough()
        builder.pizzaSauce()
        builder.product.list_elements()
