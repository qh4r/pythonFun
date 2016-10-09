while True:
    try:
        number = int(input('numer wez podaj'))
        break
    except ValueError:
        print('to nie numer')
    except:
        print('cos sie popsulo')

print('dzieki')

print('razy dwa: {}'.format(number*2))

# takie do while
print('fibonacci')
tab = [1,1]
while True:
    x = tab[0] + tab[1]
    tab[0] = tab[1]
    tab[1] = x
    print(tab)
    if x > 1000: break

import math # mozna se importowac  w takich gupich miejsach no ale wlasnie - to gupie
print('ceil ',math.ceil(4.1312))
print('floor ',math.floor(4.1312))
print('abs ',math.fabs(-4.1312))
print('factorial', math.factorial(5)) #silnia
print('truncate', math.trunc(5.4)) # ucina reszte i zostawia inta

print('to degrees', math.degrees(1.57))
print('to radinas', math.radians(45))