

class Cat:
    def __init__(self):
        print("init")
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

class Car:
    def __init__(self, color, manufacturer, model):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model


class person:
    def __init__(self, name, age,weight):
        self.name = name
        self.age = age
        self.wight = weight
    def __str__(self) -> str:
        pass
    def run(self):
        print("run")
        self.wight -= 1
        print(self.wight)
    def eat(self):
        print("eat")
        self.wight += 1
        print(self.wight)
        
# xiaoming = person("xiaoming", 18,60)
# xiaoming.eat()
# xiaomei = person("xiaomei", 18,50)
# xiaomei.run()
class HouseItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self) -> str:
        return f"{self.name} takes up {self.area} area"
    
class House():
    def __init__(self, area, address):
        self.area = area
        self.address = address
        self.free_area = area
        self.item_list = []
    def __str__(self) -> str:
        return f"House area is {self.area}, address is {self.address}, free area is {self.free_area}, item list is {self.item_list}"
    def add_item(self, item):
        if item.area <= self.free_area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print("no enough space")
def OOPlearn():
    my_House = House(100, "beijing")
    bed = HouseItem("bed", 4)
    my_House.add_item(bed)
    print(my_House)
    sofa = HouseItem("sofa", 30)
    my_House.add_item(sofa)
    print(my_House)
if __name__ == "__main__":

    OOPlearn()