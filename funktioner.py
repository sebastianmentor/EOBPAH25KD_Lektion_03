"""
Funktioner i Python!

def <funktionsnamn>(<arg1, arg2,...>):
    <kodblock>

"""
# ------------------------------------------------------------
# DEKLARERING AV FUNKTIONER
# ------------------------------------------------------------

def greet():
    print("Hello world!")


# ------------------------------------------------------------
# ANROP AV FUNKTIONER
# ------------------------------------------------------------

greet()
# reference = greet
# reference()

# ------------------------------------------------------------
# PARAMETRAR OCH ARGUMENT
# ------------------------------------------------------------
def greet2(name):
    print(f"Hello {name}")


greet2("Sebastian")

# ------------------------------------------------------------
# FLERA PARAMETRAR
# ------------------------------------------------------------

def greet_two(name1, name2, name3):
    print(f"Hello {name1} and hello {name2} and also hello {name3}")

print(greet_two("Nisse", name3="Sebastian", name2="Kalle"))

# ------------------------------------------------------------
# RETURN-VÄRDEN
# ------------------------------------------------------------

def add(a,b):
    return a+b

print(add(4,5))
print(f"{type(add(4,5))=}")

def swapp(a,b):
    return b,a

x,y = 3,8
ret = swapp(x,y)
print(type(ret))
x,y = ret
print(f"{x=}, {y=}")

# ------------------------------------------------------------
# DEFAULTVÄRDEN
# ------------------------------------------------------------

def greet_master(name, master=None):
    if master:
        print(f"The master of us all {master}") 
    else:
        print(f"New master is {name}")


greet_master("Sebastian")
greet_master("Sebastina", "Nisse")

def greet_default(name="Sebastian"):
    print(f"Hej {name}")

greet_default()
greet_default("Kalle Anka")

# VARNING med mutable objects as default!!!

def bad_func(values, default_list = []):
    default_list.append(values)
    return default_list

print(bad_func(9))
print(bad_func(23))

def better_func(values, default_list = None):
    if not default_list:
        default_list = []
    default_list.append(values)
    return default_list

print(better_func(9))
print(better_func(23))

# ------------------------------------------------------------
# NYCKELORDSARGUMENT (KEYWORD ARGUMENTS)
# ------------------------------------------------------------

def keyword_func(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

keyword_func(b=3, a=2, c=1, d=23)

# ------------------------------------------------------------
# GODTYCKLIGT ANTAL ARGUMENT (*args)
# ------------------------------------------------------------

def print_args(*args):
    print(type(args))
    for arg in args: print(arg)

print_args("Hejsan", 4, True, 5.5)

# ------------------------------------------------------------
# GODTYCKLIGA NAMNGIVNA ARGUMENT (**kwargs)
# ------------------------------------------------------------

def print_kwargs(**kwargs):
    print_args(type(kwargs))
    for key, value in kwargs.items():
        print(key, "->", value)


print_kwargs(hejsan=78, bananer="frukt", setup={"start":98}, T5=38)
 
# ------------------------------------------------------------
# DOCSTRINGS
# ------------------------------------------------------------

def some_function(a,b,c=None):
    """This is the best function evere!!"""
    print(a,b,c)
    return a

some_function(3,5)


# ------------------------------------------------------------
# LAMBDA-FUNKTIONER
# ------------------------------------------------------------

square = lambda x: x**2

print(square(8))

lista_med_dict = [{"age":23}, {"age":88}, {"age":44}]
lista_med_dict.sort(key=lambda x: x["age"])
print(lista_med_dict)

# ------------------------------------------------------------
# GLOBALA OCH LOKALA VARIABLER
# ------------------------------------------------------------

my_value = 10

def print_value():
    my_value = 2
    print(my_value)

print_value()

glob_list = []

def mutable_func(value):
    glob_list.append(value)

print(glob_list)
mutable_func(5)
print(glob_list)

# ------------------------------------------------------------
# GLOBAL-NYCKELORDET
# ------------------------------------------------------------

new_value = 0
def modify_global(value):
    global new_value
    new_value = value

print(new_value)
modify_global(4)
print(new_value)
modify_global(9)
print(new_value)

print("-----------------------")
def non_local_scope(value):
    new_value = 24
    def print_value():
        global new_value
        print(new_value)

    return print_value

f = non_local_scope("hejsan två")
f()
new_value = 10
f()