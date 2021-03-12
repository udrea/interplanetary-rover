from typing import List, Tuple


def generate_grid(m: int, n: int) -> List[Tuple[int, int]]:
    return [(x, y) for x in range(m) for y in range(n)]


allowed_commands = ['F', 'B', 'L', 'R']
def calculate_new_pos_vector(current_position, command):
    x_coord, y_coord, orientation = current_position
    
    if command in allowed_commands:
        if (command == 'F' and orientation == 'E') or (command == 'B' and orientation == 'W'):
            x_coord += 1
        elif (command == 'F' and orientation == 'W') or (command == 'B' and orientation == 'E'):
            x_coord -= 1
        elif (command == 'F' and orientation == 'N') or (command == 'B' and orientation == 'S'):
            y_coord += 1
        elif (command == 'F' and orientation == 'S') or (command == 'B' and orientation == 'N'):
            y_coord -= 1
        elif (command == 'L' and orientation == 'E') or (command == 'R' and orientation == 'W'):
            orientation = 'N'
        elif (command == 'L' and orientation == 'W') or (command == 'R' and orientation == 'E'):
            orientation = 'S'
        elif (command == 'L' and orientation == 'N') or (command == 'R' and orientation == 'S'):
            orientation = 'W'
        elif (command == 'L' and orientation == 'S') or (command == 'R' and orientation == 'N'):
            orientation = 'E'
        return wrap_around((x_coord, y_coord)) + (orientation,)
    else:
        print('Unrecognised command.')


def wrap_around(pos_coords):
    g = generate_grid(4, 6)
    m, n = max(g)
    x_coord, y_coord = pos_coords
    
    if x_coord > m:
        return (0, y_coord)
    elif x_coord < 0:
        return (m, y_coord)
    elif y_coord < 0:
        return (x_coord, n)
    elif y_coord > n:
        return (x_coord, 0)
    else:
        return pos_coords


def begin_journey(landing_pos, commands):
    pos_vec = landing_pos
    journey_history = [pos_vec]

    obstacles = [(1, 1), (1, 2), (1, 3)]  # this is already pre-loaded
    # print(f'Obstacles: {obstacles}')

    for command in commands:
        new_pos_vec = calculate_new_pos_vector(pos_vec, command)
        if new_pos_vec[:2] in obstacles:
            print(f'Last position: {pos_vec}')
            print(f'Journey history before halt: {journey_history}')
            raise Exception(f'Encountered obstacle at position: {new_pos_vec}')
        else:
            pos_vec = new_pos_vec
            journey_history.append(pos_vec)
    
    return journey_history