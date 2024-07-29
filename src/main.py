from derived_class import Dog, Cat

def main():
    dog = Dog(name="Buddy", breed="Golden Retriever")
    cat = Cat(name="Whiskers", color="Black")

    print(dog.info())
    print(dog.speak())

    print(cat.info())
    print(cat.speak())

if __name__ == "__main__":
    main()
