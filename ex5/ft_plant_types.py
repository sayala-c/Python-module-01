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

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print(f" {self._name} has not bloomed yet\n"
              "[asking the rose to bloom]")
        self.show()
        print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age:  int, growth: float,
                 harves_season: str, nutritional_value: int,
                 harvest_time: int) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harves_season
        self.nutrition = nutritional_value
        self.harvest_time = harvest_time

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
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0, 20)
    tomato.show()
    print(f"[make {tomato._name} grow and age for {tomato.harvest_time} days]")
    for _ in range(tomato.harvest_time):
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
