username = str(input())
real_password = input()

while True:
 password = input()


 if password != real_password:
  continue
   
 if password == real_password:
     print(f"Welcome {username}!")
     break
