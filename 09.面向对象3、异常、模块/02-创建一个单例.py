class Dog(object):
    __instance = None
    def __new__(cls):
        if cls.__instance==None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
a = Dog()
print(id(a))
b = Dog()
print(id(b))


#单例的实现   就是重写new方法    只允许对象创建一次

