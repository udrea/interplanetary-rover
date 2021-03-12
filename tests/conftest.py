import pytest


@pytest.fixture
def grid_size():
    return (4, 6)


@pytest.fixture
def expected_grid():
    return [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), 
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)
    ]


@pytest.fixture
def rover_landing_position():
    return (0, 0, 'E')


@pytest.fixture
def expected_pos_after_forwards_cmd():
    return (1, 0, 'E')


@pytest.fixture
def expected_pos_after_backwards_cmd():
    return (3, 0, 'E')


@pytest.fixture
def expected_pos_after_left_cmd():
    return (0, 0, 'N')


@pytest.fixture
def expected_pos_after_right_cmd():
    return (0, 0, 'S')


@pytest.fixture
def forwards_command():
    return 'F'


@pytest.fixture
def backwards_command():
    return 'B'


@pytest.fixture
def left_turn_command():
    return 'L'


@pytest.fixture
def right_turn_command():
    return 'R'


@pytest.fixture
def journey_commands():
    return ['F', 'F', 'L', 'F', 'R', 'F', 'B', 'L', 'F', 'F', 'F', 'F']


@pytest.fixture
def expected_journey_path():
    return [
        (0, 0, 'E'), (1, 0, 'E'), (2, 0, 'E'), (2, 0, 'N'), (2, 1, 'N'),
        (2, 1, 'E'), (3, 1, 'E'), (3, 1, 'E'), (2, 1, 'N'), (2, 2, 'N'),
        (2, 3, 'N'), (2, 4, 'N'), (2, 5, 'N')
    ]
