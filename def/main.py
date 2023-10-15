# def add(a,b):
#   plus=a+b
#   return plus
# print(add(1,6))
# def substract(a,b):
#   sub=a-b
#   return sub
# print(substract(10,2))
# def multiply(a,b):
#    multi=a*b
#    return multi
# print(multiply(6,4))
# def divide(a,b):
#    divide=a/b
#    return divide
# print(divide(40,4))
# def scount(string):
#    count=0
#    for i in string:
#       count+=1
#    return count
# sentence="This is world"
# print(scount(sentence))
# def dictionaries_adding(dict1,dict2):
#  for key,value in dict2.items():
#      dict1[key]=value
# dictionary1={"Aidar":20,"Beka":22}
# dictionary2={"Ceka":31,"Denis":24}
# dictionaries_adding(dictionary1, dictionary2)
# print(dictionary1)
# def menu(eat,drink):
#    with open("./menu.txt", 'w') as file:
#         file.write(f"Your order for food: {user_eat}\n,Your drink is: {user_drink}\n")
# user_eat=input("Order your food: ")
# user_drink=input("Order your drink: ")

# print(menu(eat=user_eat,drink=user_drink))
# def creating_file_user(user_request):
#    with open(user_file,'a+') as file:
#        file.write(f"{user_file}")
# import os.path
# user_file=input("Enter your file name to create txt")
# print(creating_file_user(user_request=user_file))
# def creating_file(file_name):
#      if os.path.isfile(file_name):
#          print("This file is already exists")
#          return
#       open(file_name,'w').close()

# print(creating_file(user_file))
# def slicing_object(lst):
#    middle=len(lst)//2
#    first_half=lst[middle:]
#    second_half=lst[:middle]
#    reversed_list=second_half[::-1]+ first_half[::-1]
#    return reversed_list
# list_1=['name','age','1','19']
# result=slicing_object(list_1)
# print(result)
# def generate_fibonacci(n):
#   fibonacci_numbers=[1,1]
#   while len(fibonacci_numbers) < n:
#       next_number=fibonacci_numbers[-1] + fibonacci_numbers[-2]
#       fibonacci_numbers.append(next_number)
#   return fibonacci_numbers[:n]
# fibonacci_10=generate_fibonacci(10)
# print(fibonacci_10)
# def add(a,b):
#    plus=a+b
#    return plus
# def substraction(a,b):
#    sub=a-b
#    return sub
# def last_function(a,b):
#    sum_result=add(a,b)
#    difference_result=substraction(a,b)
#    return sum_result, difference_result
# result=last_function(10,5)
# print(result[0])
# print(result[1])
import random

# def gen_number():
#   code="0444"
#   digits=[random.choice("145790") for _ in range(6)]
#   phone_number=code+''.join(digits)
#   return phone_number
# for _ in range(5):
#   phone=gen_number()
#   print(phone)
# def first_function(first):
#   first="I'm the main function"
#   return first
# def second_function(second):
#   second="I'm the nested one"
#   return second
# def union_function(first,second):
#   function1=first_function(first)
#   function2=second_function(second)
#   return function1, function2

# func1="I'm the main one"
# func2="Nested one"
# result=union_function(func1, func2)
# print(result[0])
# print(result[1])
# def dict(dictionary):
#   key=tuple(dictionary.keys())
#   value=tuple(dictionary.values())
#   return key,value
# my_dict={"Aidar":20, "Baha":19, "Askat": 20, "Atabek":20}
# key_tuple, value_tuple=dict(my_dict)
# print(key_tuple)
# print(value_tuple)
# def simple_numbers(number):
#    if number<=1:
#       return False
#    elif number<=3:
#       return True
#    elif number%2==0 or number%3==0:
#       return False
#    i=5
#    while i*i<=number:
#       if number%i==0 or number %(i+2)==0:
#          return False
#       i+=6
#    return True
# num=int(input("Enter number: "))
# if simple_numbers(num):
#    print(num, "is simple number")
# else:
#    print(num, "isnt simple number")
# def function_list(arg1,arg2):
#    x=[arg1,arg2]
#    return x
# argument1=(1,2,51,5)
# argument2={"apple", "banana", "cherry"}
# a=function_list(argument1,argument2)
# print(a)


# def user_multiply():
#    try:
#       n=int(input("Enter number: "))
#       if n<0:
#           print("Enter non-negative number")
#           return
#       for _ in range(n):
#           print("GOLD")
#    except ValueError:
#           print("Enter integer number")
# user_multiply()
# def generate_list(N):
#    if N < 0 or N >= len(List):
#        print("Enter between 0 to 3")
#    else:
#        print(List[N])
#

# N = int(input("Enter a number (int number): "))
# List = ["Aidar", "Uri", "Kanday", "Jakwy"]
# (generate_list(N))


# def user_salary(user_name, salary="5000"):
#    x = f"{user_name} - {salary}"
#   return x


# argument1 = input("Enter your name: ")
# argument2 = input("Enter your salary: ")
# print(user_salary(argument1, argument2))


# def odd_numbers(n):
#    if n <= 0:
#        return
#    if n % 2 == 0:
#        print(n)
#  odd_numbers(n - 1)


# x = int(input("Enter numbers: "))
# print("odd_numbers:")
# odd_numbers(x)


# def delete_each(set)
#    n=set()
#    return n

# x=int(input())
