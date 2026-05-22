class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth = growth

    def grow(self) -> None:
        self._height = self.height + self.growth

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

    def get_name(self) -> None:
        return self._name

def ft_garden_security() -> None:
    rose = Plant("Rose", 15.0, 10, 0)

    print(f"Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(-5)
    rose.set_age(4)
    print()
    print(f"Current state: {rose.get_name()}: {round(rose.get_height(), 1)}cm, {rose.get_age()} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security()
  
   
    