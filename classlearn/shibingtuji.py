class Gun:
    def __init__(self,model,count,maxcount):
        self.name = model
        self.bullet_count = count
        self.max_conut = maxcount
    def shoot(self,number):
        print(f"{self.name}_fire!")
        self.bullet_count -= number
        print( f"bullet_count shengxia {self.bullet_count}")
    def add_bullet(self,count):
        if (self.bullet_count + count) <= self.max_conut:
            self.bullet_count += count
            print( f"bullet_count shengxia {self.bullet_count}")
            return
        print( "cont add")
class Soldier:
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun
    def fire(self,count):
        if (self.gun.bullet_count - count) < 0:
            print("no bullet")
            return
        else:   
            print(f"{self.gun.name} fire {count}")
            self.gun.shoot(count)
    def add_bullet1(self,count):
        self.gun.add_bullet(count)
def test():
    ak47 = Gun("ak47",10,30)
    xusanduo = Soldier("xusanduo",ak47)
    xusanduo.fire(10)
    xusanduo.add_bullet1(50)
    xusanduo.fire(10)

if __name__ == "__main__":
    test()