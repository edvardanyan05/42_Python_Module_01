#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age_days: int = 0
        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old"
        )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_days += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return
        self._height = height

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return
        self._age_days = age_days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.color: str = color
        self._has_bloomed: bool = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long ",
            end=""
        )
        print(f"and {round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
