import random

for elem in [23, 21, 42, 21, "hehe", 23]:  # tablice moga miec orzne typy
    print(elem, '\n')

print('koniec')
for i in range(10, 30, 2):
    print(i, end='\t')
example_float = float(input('\npodaj  liczbe') or 23.2147141)
# example_float =  23.2147141

print("\nda sie skrocic: {:.3f}".format(example_float))  # TO nie ucina tylko ZAOKRAGLA (w gore lub w dol)!

random_range = random.randrange(1, 15)
i = 0

while i < random_range:
    print('{} < {}'.format(i, random_range))
    i += 1

height = int(input("podaj wysokosc drzewka") or 4) + 1

# for lvl in range(1, height):
#     i, j = 0, 0
#     while i < height - lvl:
#         print(' ',end='')
#         i+=1
#     while j < 1 + (lvl-1)*2:
#         print('#',end='')
#         j+=1
#     print('') #z automatu daje new line
# i = 0
# while(i < height - 1):
#     print(' ',end='')
#     i+=1
# print('#')

#  wersja z for ladniejsza

for lvl in range(1, height):
    for i in range(height - lvl):
        print(' ',end='')
    for j in range(1 + (lvl - 1) * 2):
        print('#',end='')
    print() #z automatu daje new line
for i in range(height - 1):
    print(' ',end='')
print('#')
