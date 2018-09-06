class Dog(object):
    def __init__(self):
        print("---------__init__--------方法")
    def __del__(self):
        print("---------__del__--------方法")
    def __str__(self):
        print("---------__str__--------方法")
    def __new__(cls):
        print(id(cls))
        print("---------__new__--------方法")
        return object.__new__(cls)

print(id(Dog))

xtq = Dog()


