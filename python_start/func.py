x = "test"
y = "test2"


def fun(val):
    x = val  # nie ma dostepu do zmiennych z poza funkcji!!
    global y  # to sprawia ze zaczyna uzywac zmiennej globalnej
    y = val
    y  # nie ma automatycznego zwracania osatniej wartosci potrzeba return


print(fun("zmiana"))

print("x: {}, y: {}".format(x, y))


def multi_return(a: str, b: str, c: str):
    return a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a
    # return [a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a] # to nie to samo!

print(multi_return('a', 'e', 'i'))

first, second, _, *third = multi_return('a','e','i') # elment z gwiazdka zbiera wszystko co zostalo
#popularne jest omijanie  elementow przy uzyciu _
print(first, second, third)


#generator
def multiply_list(*list): #przyjmuje wiele argumentow
    for i in list:
        yield i + 2

for x in multiply_list(2,3,5,1,35):
    print(x)