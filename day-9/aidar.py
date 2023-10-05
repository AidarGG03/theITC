with open('database.txt','w') as file:
    file.write("Aidar:Aidar111\n")
    file.write("Baya:Bayel123\n")
    file.write("Urmat_01\n")
with open('database.txt','r') as file:
    login=file.read()
    words=login.split()
print("Dear, user! sign-in")
login=input("Login: ")
password=input("password: ")
for word in words:
    s_login, s_password=word.split(":")
    if login==s_login and password==s_password:
            print("this user exists")
    elif login==s_login and password==s_password:
            login=input("Login: ")
            password=input("password: ")
    else:
            login=input("Login: ")
            password=input("password: ")
            login=input("Login: ")
            password=input("password: ")
            word
print(word)
