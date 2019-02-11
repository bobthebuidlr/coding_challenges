# IMPORT THE NECESSARY FUNCTIONS
import random
import time

# DEFINTE THE FUNCTIONS THAT TURN THE CUBES
def L(cube):
    i = []
    i.append(cube[3])
    i.append(cube[2])
    i.append(cube[6])
    i.append(cube[7])
    i.append(cube[0])
    i.append(cube[1])
    i.append(cube[5])
    i.append(cube[4])
    return i

def R(cube):
    i = []
    i.append(cube[4])
    i.append(cube[5])
    i.append(cube[1])
    i.append(cube[0])
    i.append(cube[7])
    i.append(cube[6])
    i.append(cube[2])
    i.append(cube[3])
    return i

def U(cube):
    i = []
    i.append(cube[4])
    i.append(cube[0])
    i.append(cube[3])
    i.append(cube[7])
    i.append(cube[5])
    i.append(cube[1])
    i.append(cube[2])
    i.append(cube[6])
    return i

def D(cube):
    i = []
    i.append(cube[1])
    i.append(cube[5])
    i.append(cube[6])
    i.append(cube[2])
    i.append(cube[0])
    i.append(cube[4])
    i.append(cube[7])
    i.append(cube[3])
    return i

# DEFINE A PRINT CUBE FUNCTION
def print_cube(i):
    print( """
      %s-----%s
     /|    /|
    %s-----%s |
    | %s---|-%s
    |/    |/
    %s-----%s
    """ % (i[5], i[6], i[1], i[2], i[4], i[7], i[0], i[3]))

# THE ENCRYPT AND DECRYPT FUNCTIONS
def encrypt(cubes, key):
    encrypted_cubes = {}
    counter = 1
    for cube in cubes:
        time.sleep(1)
        print("""
This is the %ist cube: """ % counter), print_cube(cubes[cube])
        counter += 1
        if cube in key:
            key_list = key[cube]
            target = cubes[cube]
            for command in key_list:
                
                if command == 'L':
                    target = L(target)
                if command == 'R':
                    target = R(target)
                if command == "U":
                    target = U(target)
                if command == "D":
                    target = D(target)
            encrypted_cubes[cube] = target
    time.sleep(2)
    print("""
I'm going to encrypt these cubes using the following key: """, key)

    word = ''

    for cube in encrypted_cubes:
        word = word + ''.join(encrypted_cubes[cube])
    time.sleep(2)
    print("""
The resulting encrypted string is: """, word)

    return encrypted_cubes

def decrypt(cubes, key):
    decrypted_cubes = {}

    counter = 1
    for cube in cubes:
        time.sleep(1)
        print("""
This is the %ist encrypted cube: """ % counter), print_cube(cubes[cube])
        counter += 1
        if cube in key:
            key_list = key[cube]

            key_list = key_list[::-1]

            target = cubes[cube]
            for command in key_list:

                if command == 'L':
                    target = R(target)
                if command == 'R':
                    target = L(target)
                if command == "U":
                    target = D(target)
                if command == "D":
                    target = U(target)
            decrypted_cubes[cube] = target

    word = ''

    for cube in decrypted_cubes:
        word = word + ''.join(decrypted_cubes[cube])
    
    while word[-1] == '*':
        word = word[:-1]
    time.sleep(2)
    print("""
Decrypting the above cubes with the given key provides: 
""", word)

    return decrypted_cubes

# GENERATING THE ENCRYPTION KEY
def generate_key(cubes):

    # Define the amount of cubes
    cubes_amt = len(cubes) - 1

    # Create an empty dict to store the encryption commands in for each cube
    key = {}

    # Loop over each of the cubes
    while cubes_amt >= 0:

        # Clear the encryption command
        command = []

        # Define the number of commands given to each cube, minimum of 2, maximum of 10
        i = random.randint(3, 7)

        
        while i > 0:

            # Randomly choose a command and add it to the list
            c = random.choice(['U', 'D', 'L', 'R'])
            command.append(c)

            i -= 1

        # Add all commands for each cube
        key[cubes_amt] = command

        cubes_amt -= 1
    
    return key

# ASK FOR USER INPUT
word = list(input("""
Welcome! I am going to encrypt anything you want. Please enter any string that you wish for me to secure:  """))

# CREATE NECESSARY AMOUNT OF CUBES DEPENDENT ON INPUT
cubes= {}
n = 0
cubes_amt = len(word) / 8
string = word

while cubes_amt >= 1:
    cube = string[0:8]
    string = string[8:]
    cubes[n] = cube
    cubes_amt -= 1
    n += 1
    
if cubes_amt < 1 and cubes_amt > 0:
    while len(string) < 8:
        string.append('*')
    cubes[n] = string

key = generate_key(cubes)

time.sleep(1)
print("""
I'm going to divide all of that up in cubes.
""")
encrypted = encrypt(cubes, key)

answer = input("""
Do you wish for me to decrypt this string again?
""")

if answer == 'yes':
    decrypt(encrypted, key)
else:
    print("""
This secret is lost forever...
""")