class Singleton():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return ('Singleton instance')

    def __repr__(self):
        return (type(self) + '()')


first = Singleton()
second = Singleton()
print (first == second)
print (first.__dict__)
