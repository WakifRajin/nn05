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
    import re
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
    
    for _ in range(n):
        movement_str = input("Enter movement vector (format: xi+yj+zk): ")
        movement_vector = parse_vector_input(movement_str)
        current_position += movement_vector
    
    print(f"The final position of the drone is: {current_position}")

if __name__ == "__main__":
    main()
