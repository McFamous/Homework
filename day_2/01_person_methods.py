class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        print(f"{self.first_name} {self.last_name}, {self.age}")

    def say_as(self, message):
        return f"<{self.first_name}> {message}"

user = Person("John", "Doe", 30)
user1 = Person("Artur", "Doe", 25)
user.info()
user1.info()

print(user.say_as("Hello"))