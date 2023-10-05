#my_file=open("./user.txt","w")
#a=input("Enter your login: ")
#b=input("Enter your password: ")
#print(my_file.write(f"login: {a}\n "))
#print(my_file.write(f"password: {b}\n"))
#my_file.close()
#task
#my_file=open("./user.txt","r+")
#if "w" in my_file.read():
#   print("YES! W MTF")
#else:
#   print("NO STFU")
#my_file.close()
#t_words=[]
#with open("./python.txt", 'r') as file:
#    my_file=file.read()
#    words=my_file.split()
#for files in words:
#    if 't' in files or 'T' in files:
#        t_words.append(files)
#print(t_words)
#login=input("Login: ")
#password=input("Password: ")
#image=input("upload image (file path): ")
#allowed_extensions={'jpg', 'jpeg', 'png'}
#file_extension=image.split(".")[-1].lower()
#if file_extension not in allowed_extensions:
#    print("Error: only allowed jpg, jpeg, png")
#else:
#    with open("./database.txt", "a+") as file:
#         myfile=file.write(f"Login: {login}, password: {password}, your image: {image}")
#    print("Registration succesfull!") 
#import os
#def copy_image(src_path, src_path2):

#   try:
#      with open(src_path, "rb") as src_file, open(src_path2,'wb') as src_file2:
#           src_file2.write(src_file.read())
#      print("image is changed! ")
#   except FileNotFoundError as x:
#       if not os.path.exists(src_path):
#           print(f"image doesnt '{src_path}'exists")
#       if not os.path.exists(src_path2):
#           print(f"image doesnt '{src_path2}'")
#   except Exception as x:
#       print(f"Some mistakes during copy:{str(x)}")
#image1=input("Enter path image: ")
#image2=input("Enter path image2: ")

#copy_image(image1, image2)
#with open('./python.txt', 'r') as file:
#    total_salary=0
#    num_months=0
#    for line in file:
#         parts=line.strip().split(',')
#         if len(parts)==2:
#            month, salary=parts
#            if month in ["May", "June", "September", "November"]:
#               total_salary+=float(salary)
#               num_months+=1
#if num_months>0:
#    avarage_salary=total_salary/num_months
#    print(f"middle salary for May, July, September and November:{avarage_salary:.2f}")
#else:
#    print(f"Not data about salary.")
#with open('./example.txt', 'w') as file:
#     numbers=[10,5,8,4,15]
#     for number in numbers:
#        file.write(str(number)+'\n')
#with open('./example.txt', 'r') as file:
#     lines=file.readlines()
#     numbers=[int(line.strip()) for line in lines]
#max_number=max(numbers)
#min_number=min(numbers)
#with open('max_min_numbers.txt', 'w') as output_file:
#    output_file.write(f"Max number: {max_number}\n")
#    output_file.write(f"Min number: {min_number}\n")
