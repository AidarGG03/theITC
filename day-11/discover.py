import random, string
def generation_password(length):
   characters=string.digits+string.ascii_letters
   password="".join(random.choice(characters) for _ i in range(length))
   return password
try:
   N=input("Enter length of password (integer number): ")
   if =<0:
      print("Length of numbers must be higher than 0")
   else:
      password=generation_password(N)
      print("Generation password:", password)
except ValueError:
    print("Error: Enter integer number") 
