#oops theory question.

#1. What is Object-Oriented Programming (OOP)?

#ans.>> OOPS is the programe in which cerated a object first , in which they contain data/attributs and functions/methods 
#       in the concept of OOPS it allows reusability ,abstractions,modulity 

#2. What is a class in OOP?

#ans.>> class is the main the object under which we cerate sub-class objects . and it define the behaviour and structure of such sub-class from which class it related

#3. What is an object in OOP?

#ans.>> An object is an instance of a class. It has its own data and can use the methods defined in the class.
#       object in class the like sub-class of such class we can recall it  .

#4. Difference between Abstraction and Encapsulation?

#ans.>> Abstraction : it this it hide the complex implementations(unneed details) like backend details and exposing the required details like seeing only inerface
#      Encapsulation : bundling of data and method of class , use of access modifier - pubic , private ,  in Python?

#5. What are dunder methods in Python?

#ans.>> dunder method are the methods define by built-in classes in python ,class define these type of method for cerating custom objects and data for every object

# 6. Explain the concept of Inheritance in OOP

#ans.>> it refers to process of child reciving the proerty of parent class 

#7. What is Polymorphism in OOP?

#ans.>> refers to an object taking servel from depending on the method/data , 
#       function taking different form with respect to different data passed 

#8. How is encapsulation achieved in Python?

#ans.>> public : means access data and method from inside or outside the class
#       private : means access data and method from only within the class(__)
#       protected : within the class and its sub-class protected member can be accessed(_)


#9. What is a constructor in Python?

#ans.>>A constructor is the __init__ method, automatically called when an object is created.

#10. What are class and static methods in Python?

#ans.>> class method : in class method we can access/modify methods and attributes accosiated to class,bound to class(not to a prticular instance of class
#       static method : it doesn't modify/access class or instance state , it doesn't depend upon class or instance

#11. What is method overloading in Python?

#ans.>> when any method is an alternative of  the any other method so it is called overloading of methods ,
#       Python doesn't support traditional overloading, but you can simulate it using default arguments.

#12. What is method overriding in OOP?

#ans.>> method in parent class and child class with same signature , the child class method will be execuded.

#13. What is a property decorator in Python?

#ans.>> it allows the method to be accessed as attribute/property/data
#       Used to create read-only or controlled-access attributes.

#14. Why is polymorphism important in OOP?

#ans.>> it provide flexibility and resablity that we can call same method on different object.

# 15. What is an abstract class in Python?

#ans.>> abstraction can be achived by using abstract class for which we need to import abc module.

#16. What are the advantages of OOP?

#ans.>> these are the advantages of oops:-
#    1.Maintainability
#    2.Reusability
#    3.Modularity
#    4.Scalability

#17. What is multiple inheritance in Python?

#ans.>> when child class is having more then one parent class inheritance

#18. Class variable vs Instance variable

#ans.>>Class variable: Shared across all instances
#     Instance variable: Unique to each object.

#19. Purpose of __str__ and __repr__

#ans.>> __str__ are User-friendly representation.
#      __repr__ are Developer-friendly, unambiguous.

# 20. Significance of super()

#ans.>> super() is used to call parent class method in child class

#21. Purpose of __del__ method

#ans.>> we Call __del__ method when an object is deleted. Rarely used , used for cleanup.

#22. Difference between @staticmethod and @classmethod

#ans.>> staticmethod : No access to class or instance (self, cls)
#       classmethod : Access to the class (cls)

#23. How does polymorphism work in Python with inheritance?

#ans.>> there are two methods by which polymorphism works :-
#    1. overloading : overloading doesn't support in python
#    2 overriding : method in parent class and child class with same signature , the child class method will be execuded

#24. What is method chaining in Python OOP?

#ans.>> chaining is the the mothod when we call multipule methods in one line.

#25. Purpose of __call__ method

#ans.>> __call__ is used when we want to make a object like a function which is callable

#practical question.

#1. Create a parent class Animal with a method speak() that prints a generic message. Create a child class Dog that overrides the speak() method to print "Bark!".

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Bark!")

d = Dog()
d.speak()

#2. Write a program to create an abstract class Shape with a method area(). Derive classes Circle and Rectangle from it and implement the area() method in both.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)
print("Circle Area:", c.area())
print("Rectangle Area:", r.area())

#3. Implement a multi-level inheritance scenario where a class Vehicle has an attribute type. Derive a class Car and further derive a class ElectricCar that adds a battery attribute.

class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, type, brand, battery):
        self.type = type
        self.brand = brand
        self.battery = battery

ev_car = ElectricCar("car","tata motors","225kwh")
print(ev_car.type)
print(ev_car.brand)

#4. Demonstrate polymorphism by creating a base class Bird with a method fly(). Create two derived classes Sparrow and Penguin that override the fly() method. 


class bird:
    def fly(self):
        print("bird is flying")

class sparrow(bird):
    def fly(self):
        print("sparrow fly's high")

class penguin(bird):
    def fly(self):
        print("pengiun can't fly")

b = bird()
s = sparrow()
p = penguin()

b.fly()
s.fly()
p.fly()

#5. Write a program to demonstrate encapsulation by creating a class BankAccount with private attributes balance and methods to deposit, withdraw, and check balance.

class bank_account:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit(self,amount):
        if amount>0:
            self.__balance = self.__balance+amount
        else:
            print(" enter a valid amount")

    def withdraw(self,amount):
         if amount<= self.__balance:
             self.__balance = self.__balance-amount
         else:
             print(" balance is not sufficient to withdraw this amount")

    def get_balance(self):
          return self.__balance

account1 = bank_account(3000)
account1.deposit(10000)
account1.withdraw(5000)
account1.get_balance()

#6. Demonstrate runtime polymorphism using a method play() in a base class Instrument. Derive classes Guitar and Piano that implement their own version of play()

class instrument:
    def play(self):
        print("now all instruments is playing music")

class guitar(instrument):
    def play(self):
        print("guitar is playing C-Sharp")

class piano(instrument):
    def play(self):
        print("piano is playing G-Minor")

i = instrument()
g =guitar()
p = piano()

i.play()
g.play()
p.play()

#7. Create a class MathOperations with a class method add_numbers() to add two numbers and a static method subtract_numbers() to subtract two numbers.

class MathOperations:
    @classmethod
    def add_num(cls,a,b):
        return a+b
    @staticmethod
    def subtract_num(a,b):
        return a-b

print("addition :",MathOperations.add_num(10,12))
print("subtraction :" ,MathOperations.subtract_num(20,13))

#8. Implement a class Person with a class method to count the total number of persons created.

class person:
    no_of_person = 0
    
    def __init__(self,name):
        self.name = name
        person.no_of_person=person.no_of_person+1
        
    @classmethod
    def total_persons(cls):
        return cls.no_of_person

p1 = person("amit")
p2 = person("ajit")
p3 = person("sandhya")
p4 = person("khushi")

print("total no. of persons :", person.total_persons())

#9. Write a class Fraction with attributes numerator and denominator. Override the str method to display the fraction as "numerator/denominator".

class fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    
    def __str__(self):
        return (f"{self.numerator}/{self.denominator}")


f1 = fraction(10,15)
print("fraction is :",f1)

#10. Demonstrate operator overloading by creating a class Vector and overriding the add method to add two vectors.

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return vector(self.x+other.x , self.y+other.y)
        
    def __str__(self):
        return (f"{self.x} , {self.y} ")

v1 = vector(10,20)
v2 = vector(23,12)
v3 = (v1+v2)
print("vector addition is :",v3)

#11. Create a class Person with attributes name and age. Add a method greet() that prints "Hello, my name is {name} and I am {age} years old."


class person:
    def __init__(self,name , age):
        self.name=name
        self.age=age
    def greet(self):
        return (F" hello my name is {self.name} and i am {self.age} years old")

p1 = person("amit",25)
p2 = person("ajit",26)
print(p1.greet())
print(p2.greet())

#12. Implement a class Student with attributes name and grades. Create a method average_grade() to compute the average of the grades.

class student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
        
    def avg_grades(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0

s1 = student("amit",[55,67,78])
s2 = student("ajit",[78,89,91])

print(f"my name is {s1.name} my avg. grades is {s1.avg_grades()} ")
print(f"my name is {s2.name} my avg. grades is {s2.avg_grades()} ")

#13. Create a class Rectangle with methods set_dimensions() to set the dimensions and area() to calculate the area.

class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area_rectangle(self):
        return self.l*self.b
#14. Create a class Employee with a method calculate_salary() that computes the salary based on hours worked and hourly rate. Create a derived class Manager that adds a bonus to the salary.
r1 = rectangle(12,14)
r2 = rectangle(9,13)
print("area of r1 rectangle :",r1.area_rectangle())
print("area of r2 rectangle :",r2.area_rectangle)()
class employee:
    def __init__(self,name,rate,hours):
        self.name=name
        self.rate=rate
        self.hours=hours
    def cal_salary(self):
        return self.rate*self.hours

class manager(employee):
    def __init__(self,name,rate,hours,bouns):
        self.name=name
        self.rate=rate
        self.hours=hours
        self.bouns=bouns
    def cal_salary(self):
        return ((self.rate*self.hours)+self.bouns)

e = employee("amit",250,400)
m = manager("ajit",400,350,10000)
print("employee's salary :" ,e.cal_salary())
print("manager's salary :",m.cal_salary())

#15. Create a class Product with attributes name, price, and quantity. Implement a method total_price() that calculates the total price of the product.

class product:
    def __init__(self,pro_name,price,quantity):
        self.pro_name=pro_name
        self.price=price
        self.quantity=quantity
    def cal_total_price(self):
        return self.quantity*self.price

p1 = product("clay bottle",399,25)
p2 =product("ceramic plates",189,75)
p3 = product("ceramic mugs",235,80)

print(f"total price for {p1.pro_name} : {p1.cal_total_price()} ")
print(f"total price for {p2.pro_name} : {p2.cal_total_price()} ")
print(f"total price for {p3.pro_name} : {p3.cal_total_price()} ")


import abc

class animal:
    @abstractmethod
    def sound(self):
        pass

class cow(animal):
    def sound(self):
        return "mwoo"

class sheep(animal):
    def sound(self):
        return "meehhee"
cow=cow()
sheep=sheep()
print("cow makes sound like :",cow.sound())
print("sheep makes sound like :",sheep.sound())

#17. Create a class Book with attributes title, author, and year_published. Add a method get_book_info() that returns a formatted string with the book's details.

class book:
    def __init__(self,title,author,year_published):
        self.title=title
        self.author=author
        self.year_published=year_published
    def get_book_info(self):
        return (f"book name :{self.title}\author name :{self.author}\nyear of published :{self.year_published} ")

b1 = book("gunaho ka devta","dharmveer bharti",1949)
b2 = book("psychology of money","morgan housel",2020)
print(b1.get_book_info())
print(b2.get_book_info())

#18. Create a class House with attributes address and price. Create a derived class Mansion that adds an attribute number_of_rooms.

class house:
    def __init__(self,address,price):
        self.address=address
        self.price=price

class mansion(house):
    def __init__(self,address,price,no_of_rooms):
        self.address=address
        self.price=price
        self.no_of_rooms=no_of_rooms

m = mansion("western lane 5th avenue",15000000,5)
print("address :",m.address)
print("no. of rooms :",m.no_of_rooms)
print("price : ",m.price)

