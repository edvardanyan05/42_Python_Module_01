#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age_days: int = 0

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, value: float) -> None:
        self.height += value

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    print("=== Garden Plant Growth ===")
    rose.show()
    h = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - h, 1)}cm")
