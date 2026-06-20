#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth
        self._stats = self.Stats()

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height = self._height + self._growth

    def age_update(self) -> None:
        self._stats._age_calls += 1
        self._age += 1

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def get_name(self) -> str:
        return self._name

    @staticmethod
    def older_than_year(age_compare: int) -> bool:
        return age_compare > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0, growth=0.0)

    def display_stats(plant: "Plant") -> None:
        print(f"[statistics for {plant.get_name()}]")
        print(f"Stats: {plant._stats._grow_calls} grow, "
              f"{plant._stats._age_calls} age, "
              f"{plant._stats._show_calls} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self._has_bloomed:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._has_bloomed = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, growth, color)
        self.seeds = seeds

    def show(self) -> None:
        Plant.show(self)
        print(f" Color: {self.color}")
        if not self._has_bloomed:
            print(f" {self._name} has not bloomed yet")
            print(" Seeds: 0")
        else:
            print(f"{self._name} is blooming beautifully!")
            print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {round(self.trunk_diameter, 1)}cm wide.")

    def display_stats(self) -> None:
        super().display_stats()
        print(f" {self._shade_calls} shade")


def check_years() -> None:
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")


def manage_stats(plant: Plant) -> None:
    plant.display_stats()


def manage_flower() -> None:
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    manage_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    manage_stats(rose)


def manage_tree() -> None:
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.0, 5.0)
    oak.show()
    manage_stats(oak)
    oak.produce_shade()
    manage_stats(oak)


def manage_seed() -> None:
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 42)
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_update()
    sunflower.bloom()
    sunflower.show()
    manage_stats(sunflower)


def manage_anonim() -> None:
    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    manage_stats(anon)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    check_years()
    print()
    manage_flower()
    print()
    manage_tree()
    print()
    manage_seed()
    print()
    manage_anonim()
