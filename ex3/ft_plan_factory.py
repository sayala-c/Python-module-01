class Plant:
    def __init__(self, name: str, height: float, age: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def grow(self) -> None:
        self.height = self.height + self.growth

    def age_update(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)} cm, {self.age} days old")


def ft_plant_factory() -> None:
    my_garden: list[Plant] = [
        Plant("Rose", 25, 30, 0),
        Plant("Oak", 200, 365, 0),
        Plant("Cactus", 5, 90, 0),
        Plant("Sunflower", 80, 45, 0),
        Plant("Fern", 15, 120, 0)
        ]

    for planta in my_garden:
        print("Created: ", end="")
        planta.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
