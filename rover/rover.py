from typing import List, Tuple

class PlanetGrid:
    """Class responsible for setting up the planet grid
    """
    def __init__(self, grid_size: Tuple[int, int]) -> None:
        self.m, self.n = grid_size  # number of rows/columns of grid
        self.grid = self.generate_grid()

    def generate_grid(self) -> List[Tuple[int, int]]:
        return [(x, y) for x in range(self.m) for y in range(self.n)]

    def is_valid_grid(self):
        if self.generate_grid():
            return True
        else:
            return False


class Navigation(PlanetGrid):
    """Rover navigation commands
    """
    ALLOWED_COMMANDS = ['F', 'B', 'L', 'R']

    def __init__(
        self, landing_position: Tuple[int, int, str], *args, **kwargs
    ) -> None:
        self.landing_position = landing_position
        super().__init__(*args, **kwargs)

    def is_landing_position_valid(self) -> bool:
        """Check if landing position is inside the grid
        """
        x_coord, y_coord, _ = self.landing_position
        if (x_coord, y_coord) in self.grid:
            return True
        else:
            return False

    def calc_new_pos_vec(
        self, current_position: Tuple[int, int, str], command: str
    ) -> Tuple[int, int, str]:
        """Compute new position vector based on current position and command

        Args:
            current_position (Tuple[int, int, str]): Current rover position
            command (str): Command to execute ('F', 'B', 'L' or 'R')
        """
        if self.is_landing_position_valid():
            x_coord, y_coord, orientation = current_position
        else:
            raise Exception('Rover is off planet.')

        if not self.is_valid_grid():
            raise Exception('No planet for the rover to navigate on.')
        
        if command in self.ALLOWED_COMMANDS:
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
            return self.wrap_around((x_coord, y_coord)) + (orientation,)
        else:
            raise Exception('Unrecognised command.')

    def wrap_around(self, pos_coords: Tuple[int, int]) -> Tuple[int, int]:
        """Wrap around edges of grid if coordinates are outside

        Args:
            pos_coords (Tuple[int, int]): Position coordinates of rover
        """
        m, n = max(self.grid)
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

class Rover(Navigation):
    """Class responsible for tracking rover movements
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def begin_journey(
        self, commands: List[str], obstacles: List[Tuple[int, int]]
    ) -> List[Tuple[int, int, str]]:
        """Execute rover movement commands and track its journey

        Args:
            commands (List[str]): List of commands to execute
            obstacles (List[Tuple[int, int]]): Obstacles on the planet
        """
        pos_vec = self.landing_position
        journey_history = [pos_vec]

        for command in commands:
            new_pos_vec = self.calc_new_pos_vec(pos_vec, command)
            xy_coord_pair = new_pos_vec[:2]
            if xy_coord_pair in obstacles:
                print(f'Last position: {pos_vec}')
                raise Exception(f'Encountered obstacle at position: {new_pos_vec}')
            else:
                pos_vec = new_pos_vec
                journey_history.append(pos_vec)
        
        return journey_history
