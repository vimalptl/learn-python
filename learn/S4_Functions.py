#DRY - Don't Repeat Yourself
#Functions:  Write onetime, reuse many times.
def say_hi_without_parameters():
    print("Hello, World - no parameters")
#function takes parameters
def say_hi(name="World"):
    print("Hello, " + name)

say_hi_without_parameters()
say_hi()
say_hi("Vimal")

#function with return
def add(a, b):
    """ Add two numbers. """
    return a + b
help(add)
print('Add 3 + 4 using an add function:', add(3, 4))