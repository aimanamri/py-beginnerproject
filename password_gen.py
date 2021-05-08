import random

print("Yeehaww welcome to PASSWORD GENERATOR ! ")

# chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$-?_&(){]}[1234567890'
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890'                  # some websites requires different type of characters
# chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$%1234567890'
# chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

number = int(input('Amount of passwords to generate:  '))

length=int(input('Input your password length:  '))
print('\nHere are your passwords:  ')

main_list = []
for password in range(number):
    pwd = ''
    for c in range(length):
        pwd += random.choice(chars)            
    main_list.append(pwd + '\n')

print(main_list) #print passwords on the terminal

## Generated passwords will be save as text file
with open('generated_passwords.txt','w') as output:
    for item in main_list:
        output.write(item)


