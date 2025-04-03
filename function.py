#1.What is the difference between a function and a method in Python?

#ans.>> function :- block of code that perform task , for defining using def keyword , functions are work independently.
#       method :- functios that was assoicated with an object , and define with in class , called on an object
#example >> functions
def name(x): #  x is functions 
    print(" hello welcome" , x)
name("tarun")

#example>> method
class Person:
    def greet(self):  # Method inside a class
        print("Hello from the Person!")

p = Person()
p.greet() 

#2. Explain the concept of function arguments and parameters in Python.

#ans.>> parameters :- variable , varibales and variable lists in funtions are parameter
#       arguments :- arguments are those values which are passed against the parameters 
#example :-
def addition(a,b,c): # a,b,c are the parameters
    return (a+b+c)
print(addition(2,5,3)) # values i.e. 2,5,3 are the arguments

#3. What are the different ways to define and call a function in Python?

#ans>> there are the many ways to define and call the functions in python :-
#     1. regular function 
#     2. lambda function 
#     3. function with keywords
#     4. function with arguments
# eample:- regular function>>
def greet(name):
    print("from regular function : hello welcome ",name)
greet("Tarun")
#example:- lambda function>>
greet01 = lambda name : f"hello welcome,{name}"
print("from lambda function :", greet01("Tarun"))

#4. What is the purpose of the `return` statement in a Python function?

#ans.>> return statement in python used for execute function with argument and return back to the caller and used when we want to use such result of return ststement later also 
# but it exits the function and storing in memory 
#example:-
def num(a,b):
    return a+b
print(num(7,3))

#5. What are iterators in Python and how do they differ from iterables?

#ans.>> 1. iterables:- the object which contain element and we want to iterate over such elements 
#       2. iterators :- iterators means object with methods of iteration that iterate each element but one at time 
#example:-
num=[1,2,3,4,5,6,7,8,9]
even_num=[]
for i in num:
    if i%2==0:
        even_num.append(i)
print("even numbers :",even_num)

#6. Explain the concept of generators in Python and how they are defined.

#ans.>> generators :- here we use yield insted of return for producing sequence of values one by one without storing it in memory . 
#example:-
def num(x):
    for i in range(x) :
        yield(x**2)
num(5)

#7. What are the advantages of using generators over regular functions?

#ans.>> these are the some advantages of using generator over regular function:-
#      1. generator functions saves the memory because it doesn't uses the memory but regular function uses the memory
#      2.generators are useful when there is large data sets 
#      3. generate values one by one when we call such values not print all values at once
#example:- regular functions >>
def square(n):
    sq_no = []  
    for i in range(n):  
        sq_no.append(i**2)  
    return sq_no  
print("squares of numbers :",square(5))

#8. What is a lambda function in Python and when is it typically used?

#ans.>> lambda is a function which is used when we have multipule arguments but having only single expression
#       lambda is used for short and simple operations 
#example:-
square = lambda x : x**2
square(10)

#9. Explain the purpose and usage of the `map()` function in Python.

#ans.>> map function is a function which is applies such function to the all elements in an iterable
#example:-
l = [1,2,3,4,5,6,7,8,9]
square = list(map(lambda a : a**2,l))
print(square)

#10. What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

#ans.>> 1. map():- map function is a function which is applies such function to the all elements in an iterable
#example:-
from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
square_num = list(map(lambda x : x**2 ,l))
print("map result :" ,square_num)

#2. reduce():- reduce performe cumulative computation of an elements which is itreable
#example:-
sum_all_num = reduce(lambda a,b : a+b , l)
print("reduce result :" ,sum_all_num)

#3. filter():- filter function is used when we need to filter the elements of iterable
#example:-
even_num = list(filter(lambda e : e%2==0,l))
print("filter result :" , even_num)

#11. Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given list:[47,11,42,13]; 

#ans.>> sum operation using reduce function
from PIL import Image
import requests
from io import BytesIO
from IPython.display import display

# Corrected raw image URL (Replace with your actual raw URL)


# Fetch and open the image
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Resize the image (Width x Height) - Adjust as needed
img_resized = img.resize((300, 300))  # Resizing to 300x300 pixels

# Display the resized image
display(img_resized)

#1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.
l = [1,2,3,4,5,6,7,8,9]
sum_even = list(filter(lambda x :  x%2==0 ,l))
print(sum(sum_even))

#2. Create a Python function that accepts a string and returns the reverse of that string.
string = input("enter a string :")
print("reversed string :" ,string[::-1])

#3. Implement a Python function that takes a list of integers and returns a new list containing the squares of each number.
l = [1,2,3,4,5,6,7,8,9]
square = list(map(lambda x : x**2 ,l))
print("output with map function:",square)

#with general function
l2 = [1,2,3,4,5,6,7,8,9]
def sq_num(l2):
    l3=[]
    for i in l2:
        l3.append(i**2)
    return l3
        
print("output with general function:",sq_num(l2))

#4. Write a Python function that checks if a given number is prime or not from 1 to 200
primes =[]
for n in range(1,201):
    if n<2:
        continue
    prime_num = True
    for i in range(2,n):
        if n%i==0:
            prime_num=False
            break
    if prime_num:
        primes.append(n)

print(primes)

#5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms.

#ans.>>
class Fibonacci:
    def __init__(self, n):
        self.a, self.b, self.n = 0, 1, n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        self.a, self.b = self.b, self.a + self.b
        return self.b - self.a

# Create and use the iterator in the simplest way
fib_obj = Fibonacci(10)
print(*fib_obj)

#6. Write a generator function in Python that yields the powers of 2 up to a given exponent.
def power_of_2(n):
    for i in range(n+1):
        yield 2**i
print(list(power_of_2(5)))

#7. Implement a generator function that reads a file line by line and yields each line as a string.

#ans.>>
def read_file(file_path):
    with open(file_path, "r") as file:
        yield from file

#8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
t=[(1,2),(4,8),(5,3),(6,5)]
print(sorted(t,key=lambda x : x[1]))        

#9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.
celsius = [ 0 , 50,60,78,95,110]
fahrenhiet = list(map(lambda c : ((c*9/5)+32) , celsius))
print(fahrenhiet)

#10. Create a Python program that uses `filter()` to remove all the vowels from a given string
v = input("enter a string")
remove_vowels = filter(lambda r : r.lower() not in "aieou",v)
print("".join(remove_vowels))

#11) Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:
''' Order No.  Book Title and Author                 Quantity   Price per item
     34587      Learning Python, Mark Lutz              4            40.95
     98762      Programming Python, Mark Lutz           5            56.80
     77226      Head First Python, Paul Barry           3            32.95
     88112      Einführung in Python3, Bernd Klein      3            24.99  '''
#Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the
#product of the price per item and the quantity. The product should be increased by 10,- € if the value of the
#order is smaller than 100.00 €.

#Write a Python program using lambda and map


#ans.>>

order_list= [
    (34587, "Learning Python, Mark Lutz", 4, 40.95),
    (98762, "Programming Python, Mark Lutz", 5, 56.80),
    (77226, "Head First Python, Paul Barry", 3, 32.95),
    (88112, "Einführung in Python3, Bernd Klein", 3, 24.99)
]

result= list(map(lambda x:(x[0], x[2]*x[3]+(10 if x[2]*x[3]<100 else 0)),order_list))
print("(oder no , final total price) :",result)

#map function applies a lambda function to each order.
#lambda function calculates the total price (quantity * price per item).
#If the total is less than 100, it adds 10 to the value.
#The result is a list of tuples with (order number, final total price).

11. Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given list:[47,11,42,13]; 

#ans.>> sum operation using reduce function
from PIL import Image
import requests
from io import BytesIO
from IPython.display import display

# Corrected raw image URL (Replace with your actual raw URL)
img_url""" https://acrobat.adobe.com/id/urn:aaid:sc:AP:1749c39a-ad04-438d-88f6-e6aa17c7d294"""

# Fetch and open the image
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Resize the image (Width x Height) - Adjust as needed
img_resized = img.resize((300, 300))  # Resizing to 300x300 pixels

# Display the resized image
display(img_resized)