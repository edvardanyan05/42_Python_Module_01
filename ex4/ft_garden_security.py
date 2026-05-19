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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    rose.set_height(-5)
    print("Height update rejected")
    rose.set_age(-10)
    print("Age update rejected")
    print("Current state: ", end="")
    rose.show()
