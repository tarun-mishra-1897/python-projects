#1.What are data structures, and why are they important?

#ans.>> data sturcture are ways of storing , managing different types of data for efficent access and modifications
# importance of data structure:-
#       1.in such way we can do deletion and manupulation of data
#       2. code presented neat and clean and improve performance of code 

#2. Explain the difference between mutable and immutable data types with examples

#ans.>> mutable type of data :- in such type of data structure modification is possible after creation(.i.e list,dictionary,sets)
#example>> 
l1=[1,2,"tarun"]
l1[2]="golu"
print("l1 =",l1)
#       immutable type of data :- in such type of data structure modification is not possible after creation they fixed(.i.e string , tuples)
#example>> 
s="tarun","golu","pintu"
#if s[1]=="karan"
print("strings are immutable")

#3. What are the main differences between lists and tuples in Python

#ans.>> main difference between lists and tuples are
#       lists :- lists are mutable and indexation is also allowed , list is used in dynamic type of data and having slower process
#       tuple:- in case of tuples idexation is allowed but immutable, tuples use for fixed type of data and having faster in process


4. Describe how dictionaries store data

#ans.>> dictionary store data in the pair of key and value
#      example>> 
dict1 = {"name":"amit","age":24,"course":"data analytics"}

#5. Why might you use a set instead of a list in Python

#ans.>> we may use a set instead of list if we don't want any duplicate in list and both are mutable so if want any modification do so.
#       in set indexation is not allowed so it works faster then list

#6. What is a string in Python, and how is it different from a list

#ans.>> string :- strings are sequence of character which is immutable type of data.
# example >> string1="amit","ajit","karan"
#             string1[1]="pankaj" >> it will gives you a error

#       list :- lsits are sequence of items which is mutable type of data.
list1=[1,2,3.5,"tarun","golu"]
list1[3]="tarun" # this will work 

#7. How do tuples ensure data integrity in Python?

#ans.>> tuples are immutable so that we can not change the elements of the tuples so that integrity of the data in case of tuple didn't hamper

8.# What is a hash table, and how does it relate to dictionaries in Python?

#ans.>> A hash table is a data structure that maps keys to values using a hash function

#9. Can lists contain different data types in Python
 #ans.>> yes, list can contain different types of data in python like (interger,float,complex,boolean,string)
list1=[1,2,3.8,3+10j,True,False,"tarun","golu"]

#10. Explain why strings are immutable in Python

#ans.>> string's immutability helps in the performance optimization 

#11. What advantages do dictionaries offer over lists for certain tasks?

#ans.>>  list:- list are ordered collection of data and duplicate elements are allowed , here index are used to call the elements
#dictonaries :- in case of dictionaries there were duplicate keys are allowed , here we call the value by keys
#dictionaries are more persentable then list as case may be 

12.# Describe a scenario where using a tuple would be preferable over a list

#ans.>> as we know tuples are immutable and list are mutable so we use tuples in such case:-
#      1. when we only read the data not changes should be done 
#      2. when we want to use tuples as a dictionary key but list can not use as a dictionary key

#13. How do sets handle duplicate values in Python?

#ans.>> set in python automaticlly discard the dupicate values from set 

#14. How does the “in” keyword work differently for lists and dictionaries?

#ans.>> in list :- "in" use to check exsiting elements/value of list 
#       in dictionary :- "in" use to check exsiting keys only not values

#15. Can you modify the elements of a tuple? Explain why or why not

#ans.>>No, tuples are immutable. Once created, their elements cannot be changed.
#      This makes them safe to use when you don’t want data to be modified.

#16. What is a nested dictionary, and give an example of its use case?

#ans.>> nested dictionary :- it is a type of dictionary which is inside the another dictionary
#use case
d = {"name":"tarun","age":27,"marks":{"maths":58,"accounting":74}}
print("original =",d)
print("marks in accounting =",d["marks"]["accounting"])

#18. In what situations are lists preferred over dictionaries?

#ans.>> situations when are lists preferred over dictionarie :-
#     1. when order of data matters 
#     2. when keys and there values are not define 
#     3. when we need to fequently modification in the data , do so

19.# Why are dictionaries considered unordered, and how does that affect data retrieval?

#ans.>> because there is no positional index but maintains the order of insertion

#20. Explain the difference between a list and a dictionary in terms of data retrieval.

#ans.>> list :- it takes more time to retrive the data and depends upon the size of the data 
#       dictionary :- it takes generally same time to retrives the data not depend on the size of data

#practical question.

#1. Write a code to create a string with your name and print it.
s="tarun"
print(s)

#2. Write a code to find the length of the string "Hello World"
s = "tarun mishra"
len(s)

3.# Write a code to slice the first 3 characters from the string "Python Programming"
s="python programming"
s[0:3] # slicing 

#4. Write a code to convert the string "hello" to uppercase.
s="hello"
s.upper()

#5. Write a code to replace the word "apple" with "orange" in the string "I like apple".
s="i like apple"
print(s.replace("apple","orange"))

6. Write a code to create a list with numbers 1 to 5 and print it
l=[1,2,3,4,5]
print(l)

#7. Write a code to append the number 10 to the list [1, 2, 3, 4]
l=[1,2,3,4]
l.append(10)
print(l)

#8. Write a code to remove the number 3 from the list [1, 2, 3, 4, 5].
l=[1,2,3,4,5]
l.remove(3)
print(l)

#9. Write a code to access the second element in the list ['a', 'b', 'c', 'd'].
l=['a', 'b', 'c', 'd']
l[1]

#10. Write a code to reverse the list [10, 20, 30, 40, 50].
l= [10, 20, 30, 40, 50]
l.reverse()
print(l)

#11.Write a code to create a tuple with the elements 100, 200, 300 and print it.
t=(100,200,300)
print(t)

12. #Write a code to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow').
t=('red', 'green', 'blue', 'yellow')
t[-2]

13.# Write a code to find the minimum number in the tuple (10, 20, 5, 15).
t=(10, 20, 5, 15)
min(t)

#14. Write a code to find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit').
t=('dog', 'cat', 'rabbit')
t.index("cat")

#15.Write a code to create a tuple containing three different fruits and check if "kiwi" is in it.
t=("apple","orange","chiku")
print("kiwi" in t)

#16.Write a code to create a set with the elements 'a', 'b', 'c' and print it.
st={"a","b","c"}
print(st)

#17. Write a code to clear all elements from the set {1, 2, 3, 4, 5}
st={1,2,3,4,5}
st.clear()
print(st)

#18. Write a code to remove the element 4 from the set {1, 2, 3, 4}.
st={1,2,3,4}
st.remove(4)
print("remove from remove function =",st)

st={1,2,3,4}
st.discard(4)
print("remove from discard function =",st)

#19.Write a code to find the union of two sets {1, 2, 3} and {3, 4, 5}
s1={1,2,3}
s2={3,4,5}
s1|s2

#20.Write a code to find the intersection of two sets {1, 2, 3} and {2, 3, 4}.
s1={1,2,3}
s2={2,3,4}
s1&s2

#21.Write a code to create a dictionary with the keys "name", "age", and "city", and print it.
d={"name":"tarun","age":27,"city":"new delhi"}
print(d)

#22.Write a code to add a new key-value pair "country": "USA" to the dictionary {'name': 'John', 'age': 25}.
d={'name': 'john', 'age': 25}
d["country"]= "USA"
print(d)

#23. Write a code to access the value associated with the key "name" in the dictionary {'name': 'Alice', 'age': 30}.
d={'name': 'Alice', 'age': 30}
d["name"]

#24.Write a code to remove the key "age" from the dictionary {'name': 'Bob', 'age': 22, 'city': 'New York'}
d= {'name': 'Bob', 'age': 22, 'city': 'New York'}
d.pop("age")
print(d)

#25.Write a code to check if the key "city" exists in the dictionary {'name': 'Alice', 'city': 'Paris'}.
d={'name': 'Alice', 'city': 'Paris'}
"city" in d

#26.Write a code to create a list, a tuple, and a dictionary, and print them all.
l=[1,2,3.5,"tarun",4+8j]
t=(1,2,3,"tarun")
d={'name': 'Alice', 'city': 'Paris'}
print("list =",l)
print("tuples =",t)
print("dictionary =",d)

#27. Write a code to create a list of 5 random numbers between 1 and 100, sort it in ascending order, and print the replaced result
l=[3,55,95,100,89]
l.sort()
print(l)

#28.Write a code to create a list with strings and print the element at the third index.
l=["tarun","mishra","golu","mishra"]
l[3]

#29.Write a code to combine two dictionaries into one and print the result.
d1={"name":"tarun","city":"new delhi"}
d2={"course":"data analytics"}
d3={**d1,**d2}
print(d3)

#30.Write a code to convert a list of strings into a set.
list1=["tarun","mishra","golu"]
set1=set(list1)
print(set1)
# project done.