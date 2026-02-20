class Dog:
    def speak(self):
        print("Bark")

class Human:
    def speak(self):
        print("Hello")

for obj in [Dog(), Human()]:
    obj.speak()