class myInt(int):
    def __call__(self, c):
        return myInt(self + c)

def add(x):
    return myInt(x)
