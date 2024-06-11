# Decorators
def functionCall(fx):
    def mfx(*arge, **kwargs):
        print("Good Morning")
        fx(*arge, **kwargs)
        print("Thanks for using this Functions")
    return mfx
@functionCall
def world():
    print("Samiul Sakib")

@functionCall
def add(a, b):
    print(a+b)
world()
add(3, 8)