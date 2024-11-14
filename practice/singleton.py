class Singleton:
    _singleton = None
    
    def __new__(cls):
        if not cls._singleton:
            cls._singleton = super(Singleton, cls).__new__(cls)
        return cls._singleton


    def print_val(self):
        print (self)


print (Singleton().print_val())
print (Singleton().print_val())
print (Singleton().print_val())
s1 = Singleton()
s2 = Singleton()
print (s1 == s2)
