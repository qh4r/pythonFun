#inny sposob na improt
from decimal import Decimal as Dec
from math import ceil as ceil

#dzieki temu mozna latwo wywolywac metody w taki skrocony sposobs
print(ceil(2.32323))

sum = Dec(0)
sum += Dec(0.232)
sum += Dec('232.21331')
# sum += Dec('21,323') # format z przecinkiem jest zly
print(sum);

print(type(sum))
print(type(23))

st = "cos tam cos tam i jeszcze troche";
print('dl. stringa: ',len(st))
# print(len(sum)) # -- nie zadziala obiekt musi miec dlugosc
print(st.__len__()) # -- mozna tak sie dostac do pola z dlugoscia
print(st[4:9],'\n', st[-10: -5]) # zakresy od do - drugi od kocna liczac
print(str(4) + "asd")

# tez mozna iterowac pos tringach
for c in "dupa":
    print(c, end=' - ')

# A - Z  -> 65 - 90
# a - z -> 97 - 122

# ord  - daje z litery jej wartosc unicode - odwrotenie dzala chr
for c in range(ord('A')-1, ord('Z')+1): # troche glupi hack ale range wyswietla top - bottom elementow
    print('{} => {}'.format(chr(c), c))


string = input('slowo uppercase!')

hash = ''
for c in string.lower():
    hash += (str(ord(c) + 50))

print('zakodowane: {}'.format(hash))

clean = ''
for i in range(0, len(hash)-1, 3):
    clean += chr(int((hash[i] + hash[i+1] + hash[i+2])) - 50 -32) # + 32 to taki to lower -32 to to to upper

    # z malymi literami trudniej bo moga miec 3 miejsca
    # przesuniecie o 50 rozwiazuje ten problem - operujemy tylko na liczbach 3 cyfrowych
    # przesuniecie o 50 w dol bylo by jeszcze latwiejsze i pozwalalo by operowac na liczbach 2 cyfrowych
print('i odkodowane to lower: {}'.format(clean))