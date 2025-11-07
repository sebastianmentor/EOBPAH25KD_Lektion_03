import exempel1_modul as e1m
# from exempel1_modul import my_function
# from exempel1_modul import * 

# e1m.my_function("Hallå")

# my_function("Hejsan")

def my_function(arg1):
    print("My function first declaration")
    print(arg1)

my_function("Hejsan")


def my_function(arg2):
    print("My function second declaration")
    print(arg2)
    print(arg2)

my_function("Hejsan")
# e1m.my_function("Hallå")
# e1m.VARIABELNAMN

skriv_ut = print

skriv_ut("Jag skriver ut den här texten via en annan variabel!")

# BAD SIDE-effects with mutable default values!!!!
def create_user(name:str, age:int, user_dict={}) -> dict:
    if user_dict: # user_dict = {} --> False
        print(f"Inside create_user, here is the dictinary before modification {user_dict}\n")
    user_dict["name"] = name
    user_dict["age"] = age
    return user_dict

user_list = []

u1 = create_user("Sebastian", 45)
user_list.append(u1)
print(f"{u1=}")
print(f"{user_list=}\n")

u2 = create_user("Kalle", 88)
user_list.append(u2)
u2["new_key"] = "has a new value"
print(f"{u1=}")
print(f"{user_list=}\n")

u3 = {"name":"Kalle", "age":87}
print(f"{user_list[0] is user_list[1]=}\n")

print(f"{u1 is u2=}")
print(f"{id(u1)=} and {id(u2)=}")
print(f"{u1 == u2=}\n")

print(f"{u1 is u3=}")
print(f"{id(u1)=} and {id(u3)=}")
print(f"{u1 == u3=}\n")



def create_user2(name:str, age:int, user_list=[]) -> list:
    user_list.append(name)
    user_list.append(age)
    return user_list

print(create_user2("Sebastian", 45))
print(create_user("Kalle", 88))