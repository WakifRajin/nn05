# Initial position
x = y = z = 0

# Input vector
userInput = input()

# Initialize components to zero
i = 0
j = 0
k = 0

# Extract the values for i, j, k components from the input
if 'i' in userInput:
    i_component = userInput.split('i')[0]
    # Remove the extracted part from the input for further processing
    userInput = userInput.split('i')[1]
    i = int(i_component) if i_component not in ['+', '-'] else int(i_component + '1')

if 'j' in userInput:
    j_component = userInput.split('j')[0]
    # Remove the extracted part from the input for further processing
    userInput = userInput.split('j')[1]
    j = int(j_component) if j_component not in ['+', '-'] else int(j_component + '1')

if 'k' in userInput:
    k_component = userInput.split('k')[0]
    k = int(k_component) if k_component not in ['+', '-'] else int(k_component + '1')

# Output the final coordinates
output_vector = (i, j, k)
print(output_vector)
