#Added a comment 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def info(self):
        return f"I am an animal and my name is {self.name}."

