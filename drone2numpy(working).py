# used chatgpt many times to get rid of errors

import re
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

def parse_vector_input(input_str):
    pattern = r"([+-]?\d*)i|([+-]?\d*)j|([+-]?\d*)k"
    matches = re.findall(pattern, input_str.replace(" ", ""))
    x, y, z = 0, 0, 0
    for match in matches:
        if match[0]:
            x += int(match[0]) if match[0] != '+' and match[0] != '-' else int(f"{match[0]}1")
        if match[1]:
            y += int(match[1]) if match[1] != '+' and match[1] != '-' else int(f"{match[1]}1")
        if match[2]:
            z += int(match[2]) if match[2] != '+' and match[2] != '-' else int(f"{match[2]}1")
    return Vector3D(x, y, z)

def main():
    initial_position_str = input("Enter the initial position of the drone (format: xi+yj+zk): ")
    initial_position = parse_vector_input(initial_position_str)
    
    n = int(input("Enter the number of movements: "))
    current_position = initial_position

    positions = [(initial_position.x, initial_position.y, initial_position.z)]
    
    for _ in range(n):
        movement_str = input("Enter movement vector (format: xi+yj+zk): ")
        movement_vector = parse_vector_input(movement_str)
        current_position += movement_vector
        positions.append((current_position.x, current_position.y, current_position.z))
    
    print(f"The final position of the drone is: {current_position}")

    # Plotting
    positions = np.array(positions)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], marker='o')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title('Drone Movement in 3D Space')
    plt.show()

if __name__ == "__main__":
    main()
