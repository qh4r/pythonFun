# fun fun
'''
mulitline
komentarz
'''

# name = input("napisz cos")
name = ''

print("siemasz " + (name or 'nico'))
print('asd ', name or 'nico', ' bsa ', '\n a')

# a , b = input('dwie liczby')  # -- w taki sposob pojedyncze znaki do kolejnych zmiennych przypisuje
a = input('jenda lczba')
b  = input('druga liczba')
# print("suma: ", a, '+', b, int(a) + int(b))
print("suma: {} + {} = {}".format(a,b,int(a)+int(b)))
print("iloraz: {} / {} = {}".format(a,b,int(a)/int(b))) # -- sam przemienia na floaty


num1, sign, num2 = input('wpisz obliczenie na 2 liczbach').split() # domyslnie split po whitespacie

i_num1 = int(num1)
i_num2 = int(num2)

if sign == '+':
    print('{} + {} = {}'.format(num1, num2, i_num1+i_num2))
elif sign == '-':
    print('{} - {} = {}'.format(num1, num2, i_num1-i_num2))
elif sign == '*':
    print('{} * {} = {}'.format(num1, num2, i_num1*i_num2))
elif sign == '/':
    print('{} / {} = {}'.format(num1, num2, i_num1/i_num2))
else:
    print('dupa')

