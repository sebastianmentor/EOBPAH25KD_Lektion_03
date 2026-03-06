# from my_module2 import func2
import my_module2
print("Second line")

point = tuple[int|float,int|float]

def calculate_distance(p1:point, p2:point) -> float:
    """
    p1 and p2 is a tuple of numrical values 
    example p1=(3,1)...
    """
    x = p2[1] - p1[1]
    y = p2[0] - p1[0]

    return (x**2 + y**2)**0.5

def another_function_in_my_module() -> None:
    print("I was created in my_module.py!")

def test():
    return 8

print("In file my_module.py and __name__ is", __name__)

if __name__ == "__main__":
    # print(variable_dont_exist)
    print(f"{type(test())=}")
    # input()