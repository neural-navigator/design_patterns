"""
Pattern Name: SingleTon (Mono state pattern)
Pattern type: Creational Design pattern
"""


class Borg:
    dd = {}

    def __init__(self):
        self.__dict__ = self.dd


class SingleTon(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg


o1 = SingleTon("Hardik")
print(o1.__dict__)
print(o1.dd)
print("o1 ==> ", o1)
print(f"o1.val is {o1.val}")

o2 = SingleTon("Patel")
print(f"o2 ==> ", o2)
print(f"o2.val is ==> ", o2.val)

o2.val = "Satya"

print(f"o1.val = {o1.val} and o2.val = {o2.val}")
