import random

# Define the amount of cubes
y = 4

# Create an empty dict to store the encryption commands in for each cube
key = {}

# Loop over each of the cubes
while y > 0:

    # Clear the encryption command
    command = []

    # Define the number of commands given to each cube, minimum of 2, maximum of 10
    i = random.randint(2, 10)

    
    while i > 0:

        # Randomly choose a command and add it to the list
        c = random.choice(['L','R','U','D'])
        command.append(c)

        i -= 1

    # Add all commands for each cube
    key[y] = command

    y -= 1
    
print(key)