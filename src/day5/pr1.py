
def    greet() :
    print("Hello, World!")
greet()

#parameter 

def add_number(a,b):
    return a+b

result  = add_number(5, 10)
print(f"The sum is: {result}")      


#scope
x=10
def show_value():
    x=5
    print(x)
print("local variable:")
show_value()
print("global variable:")
print(x)


#ice creame
icecreame="vanilla"
def food():
    fruit="apple"
    vegitable="carrot"
    print(f"Inside function: {fruit}, {vegitable}, {icecreame}")
   
food()
print(f"Outside function: {icecreame}")


#import  random
import  math
import random
print("random  float  between 0 and 1:", random.uniform(1,10))
