class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)} cm, {self.age} days old")

    def grow(self) -> None:
        self.height = self.height + self.growth

    def age_update(self) -> None:
        self.age += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age_update()
        rose.grow()
        rose.show()
    print("f")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
