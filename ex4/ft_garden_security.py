class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float) -> None:
        self._name = name
        self._heightheight = height
        self._age = age
        self._growth = growth

    def grow(self) -> None:
        self._height = self.height + self.growth

    def age_update(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)} cm, {self._age} days old")

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height} cm")


