#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    Rose = Plant()
    Rose.name = "Rose"
    Rose.height = 25
    Rose.age = 30
    Sunflower = Plant()
    Sunflower.name = "Sunflower"
    Sunflower.height = 80
    Sunflower.age = 45
    Cactus = Plant()
    Cactus.name = "Cactus"
    Cactus.height = 15
    Cactus.age = 120
    print("=== Garden Plant Registry ===")
    Rose.show()
    Sunflower.show()
    Cactus.show()
