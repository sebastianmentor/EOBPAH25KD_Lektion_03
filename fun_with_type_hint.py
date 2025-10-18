"""
Type hint, the nice way to hint stuff!

"""

age: int = 25


def greet(namn: str) -> str:
    return f"Hej på dig {namn}"


def add(a:int, b:int) -> int:
    return a + b

print(add(5, 8))
print(add("Hejsan", " Hoppsan!")) 

print(add.__annotations__)

def add(x,y):
    return x + y

print(add.__annotations__)


def total(prices:list[float]) -> float:
    return sum(prices)

print(total([3.0,4.0,5.0,5.0]))

User = dict[str, int]

def create_user(name:str, age:int) -> User:
    return {name:age}

all_users:list[User] = []

def add_user(user: User) -> None:
    all_users.append(user)

u1 = create_user("Sebastian", 88)
u2 = create_user("Nise", 66)

add_user(u1)
add_user(u2)

def get_all_ages(users:list[User]) -> list[int]:
    all_ages = []
    for user in users:
        all_ages.append(user.values())

from typing import Optional, Union

def return_maybe(val:int) -> int|None:
    if val < 100:
        return None
    return val//2