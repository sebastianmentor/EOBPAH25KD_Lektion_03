"""
anonyma funktioner i Python

lambda: <argument>: <uttryck>

+
map
filert
reduce

"""

identity = lambda x: x


print(identity("Hejsan"))

numbers = [1,2,3,4,5,6,7,8,9]

double = list(map(lambda x:x**2, numbers))
print(type(double))
print(double)


even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

from functools import reduce

summera = reduce(lambda x,y: x+y, numbers)
print(summera)

# print([n**2 for n in numbers])
# print([n for n in numbers if n%2==0])
# print(sum(numbers))


lista_med_namn = ["Kalle", "Erik", "Nisse", "Kurt"]
# lista_med_namn[0].startswith

start_with_K = list(filter(lambda x: x.startswith("K"), lista_med_namn))
print(start_with_K)

start_with_K_2 = [x for x in lista_med_namn if x.startswith("K")]

print(start_with_K_2)