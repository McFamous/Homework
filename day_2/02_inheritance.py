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


class User(Person):
    password: str

    def check_password(self, user_password):
        return self.password == user_password


user = User("test", "test", 20)
user.password = 123123

print(user.check_password(123123))