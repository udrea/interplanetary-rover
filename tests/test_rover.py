import pytest



class TestPlanetGrid:
    def test_generate_grid(self, planet_grid, expected_grid):
        actual_grid = planet_grid.generate_grid()
        assert actual_grid == expected_grid

class TestNavigation:

    def test_calculate_new_pos_vector_forwards(
        self,
        navigation,
        rover_landing_position,
        forwards_command,
        expected_pos_after_forwards_cmd
    ):
        actual = navigation.calc_new_pos_vec(
            rover_landing_position, forwards_command
        )
        assert expected_pos_after_forwards_cmd == actual


    def test_calculate_new_pos_vector_backwards(
        self,
        navigation,
        rover_landing_position,
        backwards_command,
        expected_pos_after_backwards_cmd
    ):
        actual = navigation.calc_new_pos_vec(
            rover_landing_position, backwards_command
        )
        assert expected_pos_after_backwards_cmd == actual


    def test_calculate_new_pos_vector_left_turn(
        self,
        navigation,
        rover_landing_position,
        left_turn_command,
        expected_pos_after_left_cmd
    ):
        actual = navigation.calc_new_pos_vec(
            rover_landing_position, left_turn_command
        )
        assert expected_pos_after_left_cmd == actual


    def test_calculate_new_pos_vector_right_turn(
        self,
        navigation,
        rover_landing_position,
        right_turn_command,
        expected_pos_after_right_cmd
    ):
        actual = navigation.calc_new_pos_vec(
            rover_landing_position, right_turn_command
        )
        assert expected_pos_after_right_cmd == actual


    @pytest.mark.parametrize(
        'off_grid_coords, expected_coords', [
            ((4, 2), (0, 2)), ((-1, 2), (3, 2)),
            ((1, 6), (1, 0)), ((1, -1), (1, 5))
        ]
    )
    def test_wrap_around(self, navigation, off_grid_coords, expected_coords):
        assert navigation.wrap_around(off_grid_coords) == expected_coords


class TestRover:
    def test_begin_journey(
        self,
        rover,
        journey_commands,
        expected_journey_path,
        fake_obstacles
    ):
        actual = rover.begin_journey(journey_commands, fake_obstacles)
        assert actual == expected_journey_path


    def test_begin_journey_obstacles(
        self,
        rover,
        rover_landing_position,
        journey_commands,
        real_obstacles
    ):
        with pytest.raises(Exception) as excinfo:
            rover.begin_journey(journey_commands, real_obstacles)
        
        assert "(3, 1, 'E')" in str(excinfo.value)
