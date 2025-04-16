#theory question.....
# 1. What is the difference between interpreted and compiled languages?

#ans.>> compiled language : this is the language which translated into machine language before code executed(like.. c++)
#       this slow in process

#       interpreted language: this is the language in which code executed line-by-line by interpreter(like python) 
#        this is very fast in process.

#2. What is Exception Handling in Python?

#ans.>> exceptional handling is the way how we handle the suspicious code , so rest of the code executed without any problem
#       for handling the exception/suspicious code we use try catch block.

#3.What is the purpose of the finally block in exception handling?

#ans.>> finally block is the block in which code always executed whether there is exception in code or not 

#4. What is Logging in Python?

#ans.>>Logging is a way to track events and errors in your application without printing everything to the console,
#      It's helpful for debugging and monitoring.

#5.What is the significance of the __del__ method in Python?

#ans.>> it is a method , which is used to delete the object

#6.What is the difference between import and from ... import in Python?

#ans.>> import : it means import whole module
#       from import : means import something from such module , not whole module.

#7.How can you handle multiple exceptions in Python?

#ans.>> we can handle multiple exception in python by using except blocks

#8.What is the purpose of the with statement when handling files in Python?

#ans.>> by using with statement we can read and write without using open(),close(). it automatically handle opening and closing of file

#9.What is the difference between multithreading and multiprocessing?

#ans.>> multithreading : run multiple thread/task in same process , it may take more time than multiprocessor
#      multiprocessing : run task in multiple proceesor , it may take less time than multithreading

#10.What are the advantages of using logging in a program?

#ans.>>Advantages of Using Logging :
#    1.Keeps track of program flow and errors.
#    2.Can be written to files for later analysis.
#    3.Helps debug issues without using print().
#    4.Supports different levels like DEBUG, INFO, WARNING, ERROR, CRITICAL

#11.What is memory management in Python?

#ans.>> memory management is the process in which how memory alloction and releasing memory during code execution
#      1. automatic garbage collection
#      2. counting
#      3.private space

#12.What are the basic steps involved in exception handling in Python?

#ans.>> these are the steps involve in exception handling in python:-
#     1. try block : in this block ,the code in which error may be occur
#     2.except block: in this block , if in try block error occured except block should be execute
#     3.else block : in this block , this block only executed when error occured in try block
#     4.finally block : in this block , this block always execute whether error error occur or not in try block

#13.Why is memory management important in Python ?

#ans.>> improtance of memory management in Python:-
#      1.it prevent memory leaks
#      2. for efficent programming
#      3. memoery doesn't use unused space unnecessarily

#14.What is the role of try and except in exception handling ?

#ans.>>try: it is used when code may be occur error
#      except : it is executed when error occur in try block
# both of the block together , executed rest of the code without failing

#15.How does Python's garbage collection system work ?
#ans.>> it uses the reference counting , when any object has no reference point it will be deleted
#       Garbage collector handles cyclic references (like two objects referencing each other)

#16.What is the purpose of the else block in exception handling ?

#ans.>> this the purpose of the else block in exception henadling:-
#      1. it is execute only when there is error occur in try block,and it should be run when everything goes well

#17.What are the common logging levels in Python?

#ans.>> there are 5 common level of logging which is used in indusrty:-
#      1.DEBUG : it gives a detailed info of any variable , message
#      2.INFO : this is used to convey that the code is working as expected
#      3.WARNING : used to indicate that something unexpected happend, or potential issue in the code
#      4.ERROR : it is use to indicate , there is some serious problem with some function
#      5.CRITICAL : there is some serious error, and programe will not continue further

#18.What is the difference between os.fork() and multiprocessing in Python ?

#ans.>> these are the difference between os.fork() and multiprocessing :- 
#      1.os.fork() (Unix only): Duplicates the current process. Lower-level, less portable.(not teach yet )
#      2.multiprocesssing : this is high level module to create process , scope of work is also broader

#19.What is the importance of closing a file in Python ?

#ans.>> importance of closing file in python :-
#      1.it is sign to comlete file
#      2.free up system resource
#      3.prevent file from corruption


#20.What is the difference between file.read() and file.readline() in Python ?

#ans.>> 1. file.read : it means read whole file as a string in one go.
#       2. file.readline : it means read only one of file in one go 

#21.What is the logging module in Python used for ?

#ans.>>1. it record's the state and flow of your program/code/software
#      2. it is useful tonunderstanding,monitoring and debuggig of your code
#      3. it shows how programe behaves over time

#22.What is the os module in Python used for in file handling W

#ans.>> os module helps in intracting with operating system, with the help of this we can :-
#      1. create/delete files/folders
#      2.we can check path of file folder
#      3.we can know about the size of files/folder
#      4. we can remove and check existens of file and folder

#23.What are the challenges associated with memory management in Python ?

#ans.>> Challenges in Memory Management in Python :-
#       1. give circular refernce to the two objects reffering each other
#       2.Memory leaks ,Due to lingering references
#       3.Large data structures Can consume lots of RAM if not handled carefully.

#24.How do you raise an exception manually in Python ?

#ans.>> we can raise exception manually in python by using "raise" function :-
#               raise ValueError("Invalid input!")

#25.Why is it important to use multithreading in certain applications?

#ans.>>  Multithreading is useful when your program :-
#       1. when we want to need to do multiple things at once

#practical question....

#1.How can you open a file for writing in Python and write a string to it ?

with open("assignment5.txt", "w") as file:
    file.write("Hello, this is assigment5 of python")

 #2.Write a Python program to read the contents of a file and print each line ?

with open("assignment5.txt","r") as file:
    read_line = file.read()
print(read_line)

#3.How would you handle a case where the file doesn't exist while trying to open it for reading ?

try:
    with open("file_not_exist.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("This file does not exist as of now.",e)

#4.Write a Python script that reads from one file and writes its content to another file ?

with open("readfile.txt", "w") as read_file:
    read_file.write("this message read from read_file and written in write_file")

with open("readfile.txt", "r") as read_file:
    message = read_file.read()

with open("writefile.txt", "w") as write_file:
    message_written = write_file.write(message)

print(message)    

#5.How would you catch and handle division by zero error in Python ?

try:
    5/0
except Exception as e:
    print(" error found in such code error name is :",e)

#6.Write a Python program that logs an error message to a log file when a division by zero exception occurs ?

import logging
logging.basicConfig(filename="error_file.log", level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Division by zero error: %s", e)

 #7.How do you log information at different levels (INFO, ERROR, WARNING) in Python using the logging module ?
import logging
logging.basicConfig(filename = "log_file5.log",level = logging.DEBUG)

logging.info("this is info about log_file")
logging.error("this is error about log_file")
logging.warning("this is warning about log_file")

#8.Write a program to handle a file opening error using exception handling 

try:
    with open("file_not_exist.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("This file does not exist as of now , error name is :",e)

#9.How can you read a file line by line and store its content in a list in Python ?

with open("assignment5.txt", "w") as file:
    file.write("Hello, this is assigment5 of python")

lines = []
with open("assignment5.txt", "r") as file:
    lines = file.readlines()
print("this is the content in file :" ,lines)

#10.How can you append data to an existing file in Python ?

with open("assignment5.txt", "a") as file:
    file.write("\nthis is appended line of file append by append function")

#11.Write a Python program that uses a try-except block to handle an error when attempting to access a dictionary key that doesn't exist.
d = {"name":"tarun"}
try:
    d["age"]
except KeyError:
    print("this key is not exist")

#12.Write a program that demonstrates using multiple except blocks to handle different types of exceptions.

try:
    5/0
    float("tarun")
except ZeroDivisionError:
    print("ZeroDivisionError : division by zero is not possible")
except ValueError:
    print("ValueError : not possible to convert")

#13How would you check if a file exists before attempting to read it in Python?
import os

filename = "file_exist.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File does not exist.")

#14.Write a program that uses the logging module to log both informational and error messages.
import logging
logging.basicConfig(filename="file5_log.log",level = logging.INFO)
logging.info("this is info message")

try:
    5/0
except ZeroDivisionError as e:
    logging.error("error name is : %s",e)

 #15.Write a Python program that prints the content of a file and handles the case when the file is empty
try:
    with open("assignment5.txt", "r") as file:
        data = file.read()
        if data:
            print(data)
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found.")


#16.Demonstrate how to use memory profiling to check the memory usage of a small program 
!pip- install memory-profiler
%load_ext memory_profiler
from memory_profiler import memory_usage

def create_list():
    return [i for i in range(100000)]

mem_usage = memory_usage(create_list)
print(f"Memory used: {max(mem_usage) - min(mem_usage):.2f} MiB")              

#17.Write a Python program to create and write a list of numbers to a file, one number per line 
number = [1, 2, 3, 4, 5]

with open("number.txt", "w") as file:
    for num in number:
        file.write(f"{num}\n")

#18.How would you implement a basic logging setup that logs to a file with rotation after 1MB 
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("rotating_log.log", maxBytes=1_000_000, backupCount=3)
logger.addHandler(handler)

logger.info("Logging with rotation setup.")

#19.Write a program that handles both IndexError and KeyError using a try-except block 

try:
    l = [1, 2]
    print(l[5])
    d = {}
    print(d["key"])
except IndexError:
    print("Index out of range.")
except KeyError:
    print("Key not found in dictionary.")

 #20.How would you open a file and read its contents using a context manager in Python?
with open("assignment5.txt", "r") as file:
    data = file.read()
    print(data)

#21.Write a Python program that reads a file and prints the number of occurrences of a specific word 

word_count = "t"
count = 0

with open("assignment5.txt", "r") as file:
    for line in file:
        count += line.lower().count(word_count.lower())

print(f"The word '{word_count}' occurs {count} times.")

#22.How can you check if a file is empty before attempting to read its contents ?
import os
if os.path.exists("assignment5.txt") and os.path.getsize("assignment5.txt") > 0:
    with open("assignment5.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist or is empty.")

#23.Write a Python program that writes to a log file when an error occurs during file handling.

import logging
logging.basicConfig(filename="file5_log.log",level = logging.INFO)

try:
    5/0
except ZeroDivisionError as e:
    logging.error("error name is : %s",e)    