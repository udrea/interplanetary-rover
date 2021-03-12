import pytest
from rover.rover import generate_grid, calculate_new_pos_vector, wrap_around


def test_generate_grid(grid_size, expected_grid):
    actual_grid = generate_grid(*grid_size)
    assert actual_grid == expected_grid


def test_calculate_new_pos_vector_forwards(
    rover_landing_position,
    forwards_command,
    expected_pos_after_forwards_cmd
):
    actual = calculate_new_pos_vector(rover_landing_position, forwards_command)
    assert expected_pos_after_forwards_cmd == actual


def test_calculate_new_pos_vector_backwards(
    rover_landing_position,
    backwards_command,
    expected_pos_after_backwards_cmd
):
    actual = calculate_new_pos_vector(rover_landing_position, backwards_command)
    assert expected_pos_after_backwards_cmd == actual


def test_calculate_new_pos_vector_left_turn(
    rover_landing_position,
    left_turn_command,
    expected_pos_after_left_cmd
):
    actual = calculate_new_pos_vector(rover_landing_position, left_turn_command)
    assert expected_pos_after_left_cmd == actual


def test_calculate_new_pos_vector_right_turn(
    rover_landing_position,
    right_turn_command,
    expected_pos_after_right_cmd
):
    actual = calculate_new_pos_vector(rover_landing_position, right_turn_command)
    assert expected_pos_after_right_cmd == actual


@pytest.mark.parametrize(
    'off_grid_coords, expected_coords', [
        ((4, 2), (0, 2)), ((-1, 2), (3, 2)), ((1, 6), (1, 0)), ((1, -1), (1, 5))
    ]
)
def test_wrap_around(off_grid_coords, expected_coords):
    assert wrap_around(off_grid_coords) == expected_coords
