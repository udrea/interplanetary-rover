from rover.rover import Rover


if __name__ == '__main__':
    grid_size = (4, 6)
    landing_position = (1, 1, 'E')
    journey_commands = ['F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F']
    
    rover = Rover(grid_size=grid_size, landing_position=landing_position)
    print(f'Grid:\n{rover.grid}')

    journey_history = rover.begin_journey(journey_commands)
    
    print(journey_history)