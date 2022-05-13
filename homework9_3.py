# Декоратор
"""
1) def decor(function):
    def inner(arg):
        print("Start Decorator")
        function(arg)
        print("Finish")
    return inner
def name(arg):
    print("Hello", arg)
name = decor(name)
print(name("Dima"))
2) def decor(function):
    def inner(arg,arg2):
        print("Start Decorator")
        function(arg,arg2)
        print("Finish")
    return inner
@decor
def man(name: object, surname: object):
    print("Hello ", name, surname)
print(man("Dima", "Vladik"))
3) def header(function):
    def inner(*args,**kwargs):
        print("<h1>")
        function(*args,**kwargs)
        print("</h1>")
    return inner
@header
def man(name, surname, age):
    print(f"Hello {name}, your age {age} , your surname is {surname} ")
print(man("Dima", "Vladik", "30"))



Декоратор -  это функция, которая принимает другую функцию в качестве аргумента.
Декоратор модифицирует или улучшает принятую функцию и выдает измененную.


"""