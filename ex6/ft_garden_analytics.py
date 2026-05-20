#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age_days: int = 0
        self._stats = Plant.Stats()
        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        self._stats.add_show()
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old"
        )

    def grow(self) -> None:
        self._stats.add_grow()
        self._height += 0.8

    def age(self) -> None:
        self._stats.add_age()
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

    @staticmethod
    def is_year_old(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self) -> None:
        self._stats.display()


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
        self._shade_calls: int = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long ",
            end=""
        )
        print(f"and {round(self.trunk_diameter, 1)}cm wide.")

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shade_calls} shade")


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
        print(f"Nutritional value: {int(self.nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_year_old(30)}"
    )

    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_year_old(400)}"
    )

    print("=== Flower")

    rose = Flower("Rose", 15.0, 10, "red")

    rose.show()

    display_statistics(rose)

    print("[asking the rose to grow and bloom]")

    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()
    rose.grow()

    rose.bloom()

    rose.show()

    display_statistics(rose)

    print("=== Tree")

    oak = Tree("Oak", 200.0, 365, 5.0)

    oak.show()

    display_statistics(oak)

    print("[asking the oak to produce shade]")

    oak.produce_shade()

    display_statistics(oak)

    print("=== Seed")

    sunflower = Seed(
        "Sunflower",
        80.0,
        45,
        "yellow"
    )

    sunflower.show()

    print("[make sunflower grow, age and bloom]")

    for _ in range(20):
        sunflower.grow()
        sunflower.age()

    sunflower.bloom()

    sunflower.show()

    display_statistics(sunflower)

    print("=== Anonymous")

    unknown = Plant.create_anonymous()

    unknown.show()

    display_statistics(unknown)
