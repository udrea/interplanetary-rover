from rover.rover import generate_grid, calculate_new_pos_vector


if __name__ == '__main__':
    current_position = (0, 0, 'E')
    commands = ['F', 'F', 'L', 'F']

    for command in commands:
        new_position = calculate_new_pos_vector(current_position, command)
        print(f'Current position: {current_position}\nNew position: {new_position}')

