class C:
    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b

    def __iter__(self):
        return iter(self.__dict__.items())


c = C(10, 'John')
for k, v  in c:
   print(k, v)
