import pytest
from rover.rover import generate_grid


def test_generate_grid(grid_size, expected_grid):
    actual_grid = generate_grid(*grid_size)
    assert actual_grid == expected_grid

