class MissAsteroidError(Exception):
    print()


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, current_direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.current_direction = current_direction
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {"E": "N", "S": "E", "W": "S", "N": "W"}
        self.current_direction = turns[self.current_direction]

    def turn_right(self):
        turns = {"E": "S", "S": "W", "W": "N", "N": "E"}
        self.current_direction = turns[self.current_direction]

    def lonely_robot_on_asteroid(self):
        pass

    def robot_move_forward(self, steps):
        if self.current_direction == "N":
            if self.y + steps > self.asteroid.y:
                raise ValueError("The robot fell from asteroid")
            else:
                self.y += steps

        if self.current_direction == "W":
            if self.x - steps < 0:
                raise ValueError("The robot fell from asteroid")
            else:
                self.x -= steps

        if self.current_direction == "S":
            if self.y - steps < 0:
                raise ValueError("The robot fell from asteroid")
            else:
                self.y -= steps

        if self.current_direction == "E":
            if self.x + steps > self.asteroid.x:
                raise ValueError("The robot fell from asteroid")
            else:
                self.x += steps

    def robot_move_back(self, steps):
        if self.current_direction == "N":
            if self.y - steps < 0:
                raise ValueError("The robot fell from asteroid")
            else:
                self.y -= steps

        if self.current_direction == "W":
            if self.y + steps > self.asteroid.y:
                raise ValueError("The robot fell from asteroid")
            else:
                self.x += steps

        if self.current_direction == "S":
            if self.x + steps > self.asteroid.x:
                raise ValueError("The robot fell from asteroid")
            else:
                self.y += steps

        if self.current_direction == "E":
            if self.x - steps < 0:
                raise ValueError("The robot fell from asteroid")
            else:
                self.x -= steps

#if __name__ == "__main__":
    #asteroid = Asteroid(30, 30)
    #robot = Robot(40, 10, asteroid, "N")
