"""
Pattern Name: SingleTon
Pattern type: Creational design pattern
uses:
"""

# Solution 1


class SingleTon:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


o1 = SingleTon()
print("Object 1 ==> ", o1)
o1.data = 10
print(f"o1.data ==> ", {o1.data})

o2 = SingleTon()
print("o2 ==> ", o2)
o2.data = 5

print(f"o1.data = {o1.data} , o2.data = {o2.data}")
