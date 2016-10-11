from decimal import Decimal as Dec

lista = list(range(3,10))
print(lista)
print(4 in lista)
print(2 in lista)

letters = "zs"
number = "23"
space = " "

print("letter alpha {}".format(letters.isalpha()))
print("letter alnum {}".format(letters.isalnum()))
print("letter numeric  {}".format(letters.isnumeric()))
print("number alpha {}".format(number.isalpha()))
print("number alnum {}".format(number.isalnum()))
print("number numeric {}".format(number.isnumeric()))
print("space alpha {}".format(space.isalpha()))
print("space alnum {}".format(space.isalnum()))
print("space numeric {}".format(space.isnumeric()))

cezar = "test cezara hehehe zxc"


def cezar_code(input: str):
    output = ''
    for c in input:
        code = ord(c)
        if code == 32:
            code = code
        elif (code < 95):
            code = code + 3 if code < 88 else code - 23
        else:
            code = code + 3 if code < 120 else code - 23
        output += chr(code)
    return output


print(cezar_code(cezar))


def save_to_decimal(value: str):
    print("{} {}".format(value, value.isdecimal()))
    return Dec(value) if value.isdecimal() else Dec("0")


print(save_to_decimal("232.13"))
print(save_to_decimal("xc"))

string = input("wprowadz zdanie")
result = ''
print()

# znacznie latwiej uzyc string.split()
while (string.find(' ') > -1):
    split = string.split(' ', maxsplit=1)
    result += split[0].capitalize().strip()[0]
    string = split[1]

result += string.capitalize().strip()[0]

print(result)
