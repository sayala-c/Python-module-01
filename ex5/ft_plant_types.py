#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def grow(self) -> None:
        self._height = self._height + self._growth

    def age_update(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color
        self._is_blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully")

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self._is_blooming = True
        self.show()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade "
              f"of {round(self._height, 1)}cm "
              f"long and {round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 harves_season: str) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harves_season
        self.nutrition = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutrition}")

    def update_nutri(self) -> None:
        self.nutrition += 1


def manage_flower() -> None:
    rose = Flower("Rose", 15.0, 10, 0, "red")

    print("=== Flower")
    rose.show()
    rose.bloom()


def manage_tree() -> None:
    oak = Tree("Oak", 200.0, 365, 0, 5.0)

    print("=== Tree")
    oak.show()
    oak.produce_shade()


def manage_veggie() -> None:
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    print(f"[make {tomato._name} grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_update()
        tomato.update_nutri()
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    manage_flower()
    print()
    manage_tree()
    print()
    manage_veggie()
