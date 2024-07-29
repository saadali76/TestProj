from base_class import Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def info(self):
        base_info = super().info()
        return f"{base_info} I am a {self.breed}."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

    def info(self):
        base_info = super().info()
        return f"{base_info} I am a {self.color} cat."
