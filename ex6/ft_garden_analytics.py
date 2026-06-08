class Plant:
    class Stats:
        def __init__(self, grow_calls: int, age_calls: int, show_calls: int) -> None:
            self._grow_calls = grow_calls
            self._age_calls = age_calls
            self._show_calls = show_calls

        def display_stats(self, plant_name: str) -> None:
            print(f"[statistics for {plant_name}]")
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")           

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

    @staticmethod
    def older_than_year(age_compare: int) -> bool:
        return age_compare > 365

    @classmethod
    def anonymous(cls) -> None:
        cls(name="Anonymous", height=0.0, age=0, growth=0.0)


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
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._has_bloomed = True
        print(f"[asking the {self._name} to grow and bloom]")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, growth: float, color: str, seeds: int) -> None:
        super().__init__(name, height, age, growth, color)
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        if not self._has_bloomed:
            print(f" {self._name} has not bloomed yet")
            print(f" Seeds: {self.seeds}")
        else:
            print(f"{self._name}  is blooming beautifully!")

    def bloom(self) -> None:
        self._has_bloomed = True
        print(f"[make {self._name} grow, age and bloom]")
        print(f" Seeds: {self.seeds}")

0
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

def manage_flower() -> None:
    rose = Flower(Plant)
    
    rose.show()


