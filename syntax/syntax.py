### Syntax file for Python learnings

### Variables

x: int = 4
z: bool = True
y: str = "Hello"
w: float = 43.4

### Output

print(x)

### Function

def the_function():
    print(x*3)

def another_one(x:str):
    print('another one', x)

the_function()
another_one('hello')

### Classes

class TheClass:
    def __init__(self):
        print("I'm here")

class NewClass:
    def __init__(self, x: str):
        print('new class', x)
    def __init__(self, i: int):
        print('new class', i)

instance: TheClass = TheClass()
the_instance: NewClass = NewClass('hello')
the_instance: NewClass = NewClass(4)

### Data Structures

