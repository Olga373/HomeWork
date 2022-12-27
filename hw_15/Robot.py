class Robot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def move(self, commands: str):
        new_x = self.x
        new_y = self.y
        for command in commands:
            match command:
                case  "N":
                    new_y += 1
                    if new_y in range(0, 101):
                        return "Robot can't move in this way"
                case  "S":
                    new_y -= 1
                    if new_y in range(0, 101):
                        return "Robot can't move in this way"
                case  "E":
                    new_x += 1
                    if new_x in range(0, 101):
                        return "Robot can't move in this way"
                case  "W":
                    new_x -= 1
                    if new_x in range(0, 101):
                        return "Robot can't move in this way"

        self.x = new_x
        self.y = new_y
        return self.x, self.y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

robot = Robot(0, 0)
print(robot)
print(robot.move("NNNN"))
