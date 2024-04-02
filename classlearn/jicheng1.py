class Animal:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am %s.' % self.name)
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')
class Dog(Animal):
    def bark(self):
        print('wangwang')
class Cat(Animal):
    def catch(self):
        print('catch mouse')
        
def test():
    dog = Dog('dog')
    dog.greet()
    dog.eat()
    dog.sleep()
    dog.bark()
   
if __name__ == "__main__":
    test()