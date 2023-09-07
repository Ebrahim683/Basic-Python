# name = 'Ebrahim'
# age = 22
# print(name+'\'s age is ', age)


# a = 12
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a % b)
# print(a//b)  # it gives int value after device
# print(a**b)  # it means a to the power b


# name = input('Enter your name: ')
# age = input('Enter your age: ')
# gpa = input('Enter your gpa: ')
# print('Student info\n.............................')
# print(name)
# print(age)
# print(gpa)


# num1 = int(input('Enter number 1: '))  # typecast string to int
# num2 = int(input('Enter number 2: '))  # typecast string to int
# sum = num1+num2
# sub = num1-num2
# print(f'{num1} + {num2} = {sum}') # formate string
# print(sub)

# print('Name', end=' ')
# print('01749989506')

# from math import *
# print(max(20, 54))
# print(min(20, 54))
# print(pow(2, 4))
# print(sqrt(25))
# print(round(3.5))


# mark = 50
# if mark > 33:
#     print('pass')
#     print(f'mark is {mark}')
# elif mark == 33:
#     print('mark is equal to 33')
#     print(f'mark is {mark}')
# else:
#     print('fail')
#     print(f'mark is {mark}')

# print('program finished')


# if 7 > 5:
#     if 5 > 3:
#         print('statement 1')
#     else:
#         print('else statement')

#     print('7 is gather then 5')
# print('finished')


# num = 40
# print(num if num >= 50 else 'small')  # ternary operator


# char = input("Enter a character: ")
# if char == 'A' or char == 'a':
#     print(char)
# else:
#     print('char is not a or A')


# i = 1
# while i <= 20:
#     print(i)
#     i = i+1
# print('finished')


# list = ['java', 'kotlin', 'dart', 'flutter', 'c', 'c++', 'c#', 'python']
# print(len(list))
# print(list)
# print(list[5])
# print(list[3:])
# print(list[-3])
# print('python' in list)  # check value is available is the list
# print('swift' not in list)  # check value is not available is the list
# list = list+['swift', 20]
# print(list)
# print(len(list))
# print('swift' not in list)  # check value is not available is the list
# list.append('javaStript')
# print(list)
# list.insert(0, 'android')
# print(list)
# list.remove(20)
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list2 = list.copy()
# list.clear()
# print(list)
# print(list2)


# num = list(range(2, 101, 2))
# print(num)


# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in list:
#     print(i)


# n = int(input('enter number: '))
# sum = 0
# for i in range(1, n+1, 2):
#     sum = sum+(pow(i, 2))
# print(sum)


# for i in range(5):
#     print((2*i-1)*'*')


# import random
# guessNumber = int(input('enter number between 1 to 5: '))
# num = random.randint(1, 5)
# # num = random.random() * 5
# if guessNumber == num:
#     print('won')
# else:
#     print('lose')


# list = []
# for i in range(5):
#     data = int(input('enter number: '))
#     list.append(data)
# print(list)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# for row in matrix:
#     for col in row:
#         print(col)


# studentId = {
#     '101': 'A',
#     '102': 'B',
#     '103': 'C',
#     '104': 'D',
# }
# print(studentId.get('105', 'invalid key'))

###function
# def add(x: int, y: int):
#     sum = x+y
#     print(sum)
# add(10, 20)
# add(500,45)


# def sub(x, y):
#     return x-y
# print(sub(x=50, y=30))


### xargs
# def info(*details):
#     print(details)
# info(101, "erbahim", 3.81)

### xargs
# def add(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     print(sum)
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)


### xxargs
# def info(**details):
#     print(details)
# info(id=101, name='ebrahim')


# result = (lambda a, b: a*a+2*a*b+b*b)(2, 3)
# print(result)


# def square(x):
#     return x*x
# data = [1, 2, 3, 4, 5]
# result = list(map(square,data))
# print(result)
# result2 = [x*x for x in data]
# print(result2)
# result3 = list(filter(lambda x: x % 2 == 0, data))
# print(result3)
# result4 = [x for x in data if x % 2 == 0]
# print(result4)


### recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# result = factorial(5)
# print(result)


### file
# file = open('student.txt', 'r')
# text = file.read()
# text = file.readlines()
# print(text)
# file.close()

# file = open('student1.txt', 'a')
# file.write('\nAsraf - 105')
# text = file.read
# print(text)
# file.close


# num = int(input('enter number: '))
# try:
#     result = 20/num
#     print(result)
#     print('done')
# except :
#     print('error')
# finally:
#     print('finished')


### class


# class Student:
#     roll = 0
#     gpa = 0.0

### constructor
#     def __init__(self, roll, gpa):
#         self.roll = roll
#         self.gpa = gpa

#     # def setInfo(self, roll, gpa):
#     #     self.roll = roll
#     #     self.gpa = gpa

#     def display(self):
#         print(f'Roll: {self.roll}, GPA: {self.gpa}')


# rahim = Student(101, 3.5)
# rahim.setInfo(101, 3.5)
# rahim.display()


# class Triangle:
#     def __init__(self, base: float, height: float):
#         self.base = base
#         self.height = height

#     def calculateArea(self) -> float:
#         return 0.5*self.base*self.height


# t1 = Triangle(base=10, height=20)
# print(t1.calculateArea())

# t1 = Triangle(20, 30)
# print(t1.calculateArea())


### inheritance
# class Phone:

#     def __init__(self) -> None:
#         print('Phone init...')

#     def call(self):
#         print('calling....')

#     def message(self):
#         print('messaging...')

# class Samsung(Phone):  # Samsung extends Phone

#     def __init__(self) -> None:
#         super().__init__()
#         print('Samsung init')

#     def takePhoto(self):
#         print('taking photo...')

# s = Samsung()
# s.call()
# s.message()
# s.takePhoto()

# class Shape:
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height

#     def area(self):
#         print('this is shape class')

# class Triangle(Shape):
#     def area(self):
#         result = 0.5*self.height*self.base
#         print(f'area of triangle is: {result}')

# class Rectangle(Shape):
#     def area(self):
#         result = self.height*self.base
#         print(f'area of rectangle is: {result}')

# t = Triangle(20, 30)
# t.area()

# r = Rectangle(20, 30)
# r.area()


### abstraction
from abc import ABC, abstractmethod

class MakeCall(ABC):

    @abstractmethod
    def call(self):
        pass

class Santo(MakeCall):
    def call(self):
        print('santo is calling')

class Ebrahim(MakeCall):
    def call(self):
        print('ebrahim is calling')

s = Santo()
s.call()

e = Ebrahim()
e.call()


### module

import area
area.triangleArea(10, 20)
area.rectangleArea(10, 20)
from area import rectangleArea
rectangleArea(10, 20)
from area import *
triangleArea(10, 20)
rectangleArea(10, 20)
