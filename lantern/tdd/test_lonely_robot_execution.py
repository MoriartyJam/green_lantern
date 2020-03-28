import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        current_direction = "E"
        robot = Robot(x, y, asteroid, current_direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert current_direction == current_direction

    @pytest.mark.parametrize(
        "asteroid_size, robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "E")


class TestTurns:
    def setup(self):
        x, y = 10, 15
        self.asteroid = Asteroid(x * 2, y * 2)

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )
    )
    def test_turn(self, current_direction, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x * 2, y * 2)
        robot = Robot(x, y, asteroid, current_direction)
        if robot.turn_left():
            assert robot.current_direction == expected_direction
        elif robot.turn_right():
            assert robot.current_direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, steps, expected_direction",
        ([
            ("N", 3, (10, 18)),
            ("W", 7, (10, 8)),
            ("S", 5, (5, 15)),
            ("E", 2, (8, 15)),
        ])
    )
    def test_move_forward(self, current_direction, steps, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x * 2, y * 2)
        robot = Robot(x, y, asteroid, current_direction)
        robot.robot_move_forward(steps)
        assert robot.x, robot.y == expected_direction

    @pytest.mark.parametrize(
        "current_direction, steps, expected_direction",
        ([
            ("N", 3, (10, 18)),
            ("W", 7, (10, 8)),
            ("S", 5, (5, 15)),
            ("E", 2, (8, 15)),
        ])
    )
    def test_move_back(self, current_direction, steps, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x * 2, y * 2)
        robot = Robot(x, y, asteroid, current_direction)
        robot.robot_move_back(steps)
        assert robot.x, robot.y == expected_direction

    @pytest.mark.parametrize(
        "current_direction",
        ([
            "N",
            "W",
            "S",
            "E",
        ])
    )
    def test_fall_robot(self, current_direction):
        x, y = 10, 15
        asteroid = Asteroid(x * 2, y * 2)
        robot = Robot(x, y, asteroid, current_direction)
        with pytest.raises(ValueError):
            robot.robot_move_forward(100) and robot.robot_move_back(100)
