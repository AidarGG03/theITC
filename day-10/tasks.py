#values=[45,"raz",23,"baha",123,"mega"]
#list=[]
#for i in values:
#   try:
#      set(i)
#      list.append(True)
#   except (TypeError, ValueError):
#      list.append(False)
#x=all(list)
#print(list)
#print(x)
#numbers=set()
#for i in range(5):
 #   try:
 #      num=int(input("Enter num: "))
#       numbers.add(num)
#    except TypeError:
#      print("Incorrect num")
#      exit()
#print(min(numbers))
#functions={"print": print}
#func_from_input=input("Enter your function: ")
#functions[func_from_input]("Hello")
#dict={'name':'John','lastname':'Snow', 12: 'age'}
#for x in dict.keys():
#    try:
#       x+'abc'
#    except TypeError:
#       x=str(x)
#       x+=" student"
#print(x)
#user=input("Enter Python function: ")
#function=["print()", "input()","len()"]
#try:
#   if user in function:
#      print("This function exists")
#except:
#      x=user.append(function)
#      print(x)
#while True:
#    try:
#       user_loan=float(input("Enter less than 50000:"))
#       if user_loan < 50000:
#          raise ValueError("Sum must be less than 50000")
#       break
#    except ValueError as x:
#         print(f"Mistake: {x}")
#rate=3.47/100
#over=user_loan*rate
#over=round(over,2)
#print(f"Total Credit will be: {over}")
