def sebastian_greets():
    print("Hello from Sebastian!")


def run_function(fun):
    fun()

sg = sebastian_greets

sg()

run_function(sebastian_greets)
# run_function("String!")
# "Test"()

def func_with_arguments(var1, var2, var3=5):
    print(var1, var2, var3)


func_with_arguments(1,2,3)
func_with_arguments(1,3,2)
func_with_arguments(1,2)
func_with_arguments(var2=1, var1=2)
func_with_arguments(2, var2=1)


def bad_function(value, a_list = []):
    a_list.append(value)
    return a_list 


my_list = bad_function(42)
print(my_list)
print(f"{id(my_list)=}")
my_list.append(999)
my_second_list = bad_function(666)
print(my_second_list)
print(f"{id(my_second_list)=}")

def better_function(value, a_list = None):
    if not a_list: a_list = []

    a_list.append(value)
    return a_list

my_list = better_function(42)
print(my_list)
print(f"{id(my_list)=}")
my_list.append(999)
my_second_list = better_function(666)
print(my_second_list)
print(f"{id(my_second_list)=}")

def fun(*arg):
    print(f"{type(arg)=}")


fun("Hejsan!")
fun(88)
fun(1,2)

def function_retun_same(value):
    return value

print(type(function_retun_same("string")))
print(type(function_retun_same(8)))

def swapp(value1, value2):
    return value2, value1

print(type(swapp(5, 8)))
print(type(swapp("hej", "då")))

def five_copies(val):
    return val,val,val,val,val


values = five_copies(5)
print(values)
first, *rest = five_copies(8)
print(first, rest)
print(type(first), type(rest))

def args_function(*args):
    for arg in args:
        print(arg)


args_function(1,2,3,4,5,6)

def kwargs_function(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} --> {v}")

kwargs_function(val1=77, val2="hej", val3=None)


def master_function(first_value, *args, **kwargs):
    """
    Use with care, programmer is stupid!

    first_value is a must! 

    The rest are free to do whatever!s
    """
    print(first_value)
    print(args)
    print(kwargs)

master_function(1,2,3, v=88, m="hejh")

greet = lambda _ : print("Hello there!")

greet(None)

square = lambda x: x*x

print(square(8))

persons = [    
    {
    "name":"Harry",
    "age":77
    },
    {
    "name":"Mary",
    "age":12
    },
    {
    "name":"Barry",
    "age":34
    },
    {
    "name":"Sally",
    "age":52
    }          
]

persons.sort(key=lambda p:p["age"])
print(persons)
persons.sort(key=lambda p:p["name"], reverse=True)
print(persons)



global_variable = 42

def print_global():
    # global global_variable
    global_variable = 10
    print(global_variable)

print_global()
print(global_variable)


global_list = [888]

def mutate_list(value):
    print(global_list)
    global_list.append(value)
    print(global_list)

mutate_list(12)
global_list.append(10)
mutate_list(4)