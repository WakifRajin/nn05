# Initial position
x = y = z = 0

# Input vector
userInput = input()

# Extracting the values for i, j, k components from the input
i_component = userInput.split('i')[0]
j_component = userInput.split('i')[1].split('j')[0]
k_component = userInput.split('j')[1].split('k')[0]

# Converting string components to integers
i = int(i_component)
j = int(j_component)
k = int(k_component)

# Output the final coordinates
output_vector = (i, j, k)
print(output_vector)
