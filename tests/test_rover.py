import pytest
from rover.rover import generate_grid


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
    