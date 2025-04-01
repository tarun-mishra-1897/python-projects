# 1. what is python,and why is it popular?
#ans>> python is agenrol programming language known for its simplicity,easy to access,and vesslit
#popular because of:
# easy to read the syntax
# wide libraries i.e numpy,pandas etc
# strong community support
# versatie becaues use in web devlopement , data science etc.

# 2.what is an interpreter in python?
#ans>> an interpreter in python is a programme that executes python code line-by- line, converting it into machine-readablecode.

#3. What are pre-defined keywords in Python?

#ans.>> Pre-defined keywords are per-defined words that have special identity/meaning and functions in Python.
# example >> print(),if,ifelse,while,type etc.

#4. Can keywords be used as variable names?

#ans.>> no , keyword can not use as name because it has reserved by python for secifice function.

#5. What is mutability in Python?

#ans.>> mutability :- possible to change (.i.e list,dictionary ,sets)
#      immutability :- not possible to change (.i.e tuples , string , integers)

#6. Why are lists mutable, but tuples are immutable?

#ans.>> list:- list fuction are made with which is flexible with data modification >> which make it mutable 
#      tuples:- tuple function are made for the data protection and optimization in proformance >> which make it immutable.

#7. What is the difference between == and is operators in Python?

#ans.>> == :- this refers to two variables are equal or same value
#       is :- is operator refers to two variable in same memory.

# 8. What are logical operators in Python?

#ans.>> logical operators are use to conbine conditional statement
#    1. and :- gives true if both of conditions are true
#    2. or :- gives true if any of conditions are true
#    3. not :- gives true if statement are false

#9. What is type casting in Python?

#ans.>> type casting is a proccess in which we change the data type 
# example :- s= "123" >> this is strig 
#            i = int(s) >> now this is integer

#10. What is the difference between implicit and explicit type casting?

#ans.>> implicit type casting :- in which data type change automatically 
#                   example :-  a=5(integer) , b=3.4(float no.)
#                     adding a and b :- c = a+b >> c=8.4 >> now it will automatically change to float from integer

#       explicit :- explicit type casting is a proccess in which we change the data type manually
# example :- s= "123" >> this is strig 
#            i = int(s) >> now this is integer >> we change the data type by using int() 

#11. What is the purpose of conditional statements in Python?

#ans.>> condition statement are useful when we have to many statement and execute only some conditons so it will control the statement folw
#       examples :- if , else , elif 

#12. How does the elif statement work?

#ans.>> elif condition is able to check many conditions which is given at a time one by one 
#example
a=28
b=100
if a ==28 and b < 100:
    print("this is a valid statement")
elif a == 28 and b ==100:
    print("this is valid statement but inside elif condition")
else :
    print("in this data set there is no valid statement")
# this is valid statemrnt but inside elif condition.

#12. How does the elif statement work?

#ans.>> elif condition is able to check many conditions which is given at a time one by one 
#example
#12. How does the elif statement work?

#ans.>> elif condition is able to check many conditions which is given at a time one by one 
#example
a=28
b=100
if a ==28 and b < 100:
    print("this is a valid statement")
elif a == 28 and b ==100:
    print("this is valid statement but inside elif condition")
else :
    print("in this data set there is no valid statement")
    #this is valid statment but inside elif condition.

#3. What is the difference between for and while loops?

#ans.>> for loop :- for loop used for iterating over a sqeuence (.i.e string,list etc)
#example
for i in range(3):
    print("i =",i)
#     while loop :- while loop is used to repeat the block of code until it will true
#example
x = 0
while x < 5:
    print("x =",x)
    x += 1

    #14. Describe a scenario where a while loop is more suitable than a for loop.

#ans.>> A while loop is more suitable when the number of iterations is unknown or depends on a condition.
#example
initial_speed = 0
final_speed = 10
while initial_speed<final_speed:
    print(initial_speed)
    initial_speed=initial_speed+2

# practical question.

#1.Write a Python program to print "Hello, World!
print("hello , world")

#2. Write a Python program that displays your name and age.
name="tarun"
age=27
print("name =" ,name,"age =" ,age)

#3.Write code to print all the pre-defined keywords in Python using the keyword library
import keyword
print(keyword.kwlist)

#4. Write a program that checks if a given word is a Python keyword
word = input("enter a word")
if word in keyword.kwlist:
    print("word is a keyword")
else :
    print("word is not a keyword")

#5. Create a list and tuple in Python, and demonstrate how attempting to change an element works differently for each
l=[1,2,3.4,"tarun","facebook",3+10j]
t=(5,6.7,8,"golu","rishabh")

#list are mutable
l[2] = "tarun"
print("l =",l)
#tuples are immutable>> so it will give you an error.
t(2)=5

#6. Write a function to demonstrate the behavior of mutable and immutable arguments

#ans.>>#list are mutable
l=[1,2,3.4,"tarun","facebook",3+10j]
t=(5,6.7,8,"golu","rishabh")
l[2] = "tarun"
print("l =",l)

# tuples are immutable >> so it will gives you an error
t(2)=5

#7.Write a function to demonstrate the behavior of mutable and immutable arguments
#ans.>> same as a question no. 6

#8.Write a program to demonstrate the use of logical operators

# Define two boolean variables
a = True
b = False

# Using 'and' operator: True if both operands are True
and_result = a and b
print(f"a AND b = {and_result}")  # False because b is False

# Using 'or' operator: True if at least one operand is True
or_result = a or b
print(f"a OR b = {or_result}")  # True because a is True

# Using 'not' operator: Inverts the boolean value
not_a = not a
not_b = not b
print(f"NOT a = {not_a}")  # False because a is True
print(f"NOT b = {not_b}")  # True because b is False

# Combining logical operators
combined_result = (a or b) and not b
print(f"(a OR b) AND NOT b = {combined_result}")  # True because (True or False) and True

#explanation:
#and: Returns True only if both operands are True.

 #or:Returns True if at least one operand is True.

#not: Inverts the boolean value (True becomes False and vice versa).
# this example illustrates how logical operators work with boolean values in Python.

#9. Write a Python program to convert user input from string to integer, float, and boolean types
user_input = input("Enter a value: ")
int_value = int(user_input)
float_value = float(user_input)
bool_value = bool(user_input)

print("Integer:", int_value)
print("Float:", float_value)
print("Boolean:", bool_value)

#10. Write code to demonstrate type casting with list elements
list1 = ["1","2","3","34"]
list2=[]
for i in list1:
    intg = int(i)
    list2.append(intg)
print(list2)

#11. Write a program that checks if a number is positive, negative, or zero
num = int(input("enter a number"))
if num >0 :
    print("number is positive")
if num == 0:
    print("number is zero")
if num <0:
    print("number is negative")

 #12. Write a for loop to print numbers from 1 to 10
for i in range(0,10):
    print(i)

#13. Write a Python program to find the sum of all even numbers between 1 and 50
sum_even = 0
for i in range(100):
    if i%2==0:
        sum_even=(sum_even+i)
print(sum_even)    

#14. Write a program to reverse a string using a while loop

#ans.>> 
s= "tarun"
rs=""
index=len(s)-1
while index>= 0:
    rs+=s[index]
    index -=1
print("revrse_string :",rs)

#15. Write a Python program to calculate the factorial of a number provided by the user using a while loop.

#ans.>> 
integer = int(input("enter a number"))
i = 1
factorial = 1              

while i<=integer:
    factorial = (i*factorial)
    i=i+1
print("factorial of" ,integer,"is", factorial)
    
    

