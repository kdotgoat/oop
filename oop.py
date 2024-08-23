class Person:
    def me(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")

# Create an instance of the Person class and initialize it
person1 = Person()
person1.me("Orado Wise", 30, "male")

# Call the greet method
person1.greet()