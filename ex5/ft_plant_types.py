class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def grow(self) -> None:
        self._height = self._height + self._growth

    def age_update(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")

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
    def __init__(self, name: str, height: float, age: int, growth: float, color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color

    def bloom(self) -> None:
        print(
            "Rose has not bloomed yet"
            "[Asking the rose to bloom]"
        )
        self.show()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        pass


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age:  int, growth: float, harves_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harves_season
        self.nutrition = nutritional_value

    def update_nutri(self) -> None:
        pass
