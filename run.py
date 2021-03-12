from rover.rover import Rover


if __name__ == '__main__':
    grid_size = (4, 6)
    landing_position = (0, 0, 'E')
    # obstacles = [(1, 4), (3, 1)]
    obstacles = [(1, 4)]
    journey_commands = [
        'F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F'
    ]
    rover = Rover(grid_size=grid_size, landing_position=landing_position)
    
    journey_history = rover.begin_journey(journey_commands, obstacles)
    
    print(journey_history)