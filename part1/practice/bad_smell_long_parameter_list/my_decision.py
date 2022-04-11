class Unit():
    def __init__(self, field, speed=1):
        self.field = field
        self.speed = speed

    def move(self, x_axis, y_axis, direction, is_fly=False):
        if is_fly:
            self.speed *= 1.2
        else:
            self.speed *= 0.5

        if direction == 'UP':
            y_axis += self.speed
        elif direction == 'DOWN':
            y_axis -= self.speed
        elif direction == 'LEFT':
            x_axis -= self.speed
        elif direction == 'RIGHT':
            x_axis += self.speed

        return {'x': x_axis, 'y': y_axis}

