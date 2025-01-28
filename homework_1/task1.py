class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def makesound(self):
        print(f"{self.name} издает звук: {self.sound}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "мяу")
        self.color = color
    
    def makesound(self):
        print(f"{self.name} ({self.color}) говорит: {self.sound}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "гав")
        self.color = color
    
    def makesound(self):
        print(f"{self.name} ({self.color}) говорит: {self.sound}")


# Примеры использования
cat = Cat("Муся", "серый")
dog = Dog("Палкан", "белый")

cat.makesound()  # Муся (серый) говорит: мяу
dog.makesound()  # Палкан (белый) говорит: гав
