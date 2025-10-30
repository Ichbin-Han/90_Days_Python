import random

#Defining the character lists
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','*','?','(','+','-',')']

print("Welcome to the Password Generator")

#This loop ensure the user is giving valid input
while True:
    try:
        lenght = int(input("How long the password should be? "))
        number_of_symbols = int(input("How many symbols should be in the password? "))
        number_of_numbers = int(input("How many numbers should be in the password? "))
    
    except ValueError:
        print("\nLooks like you wrote an invalid input!")
        print("Don't worry! Let's try again. \n")
        continue

    number_of_letters = lenght - number_of_symbols - number_of_numbers
    if number_of_letters < 0:
        print("\nI believe you miscalculated the number of symbols and numbers in the password, they are not matching with the total lenght!")
        print("Don't worry! Let's try again. \n")
        continue

    break

#Generating the password
password = []
for _ in range(number_of_letters):
    password.append(random.choice(letters))

for _ in range(number_of_symbols):
    password.append(random.choice(symbols))

for _ in range(number_of_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

#Turning the list into string
final_password = "".join(password)

#Printing output
print(f"\n Here is the password: {final_password}")

