from rover.rover import generate_grid, calculate_new_pos_vector, begin_journey


if __name__ == '__main__':
    landing_pos = (0, 0, 'E')
    commands = ['F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F']
    fake_obstacles = [(1, 1), (1, 2), (1, 3)]
    real_obstacles = [(1, 1), (1, 2), (3, 1)]

    journey_history = begin_journey(landing_pos, commands, real_obstacles)
    print(f'Journey history:\n{journey_history}')
    