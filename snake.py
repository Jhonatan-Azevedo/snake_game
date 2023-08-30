class Snake:
    def __init__(self, 
                 screen_size=(300, 400), 
                 position=[80, 50], 
                 body=[[80, 50], [70, 50], [60,50]],
                 direction='RIGHT'):
        self.screen_size = screen_size
        self.position = position
        self.body = body
        self.direction = direction

    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = new_direction

        if new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = new_direction

        if new_direction == 'TOP' and not self.direction == 'BOTTOM':
            self.direction = new_direction

        if new_direction == 'BOTTOM' and not self.direction == 'TOP':
            self.direction = new_direction

    def move(self, position_food):
        if self.direction == 'RIGHT':
            self.position[0] += 10

        if self.direction == 'LEFT':
            self.position[0] -= 10

        if self.direction == 'TOP':
            self.position[1] -= 10

        if self.direction == 'BOTTOM':
            self.position[1] += 10

        self.body.insert(0, list(self.position))

        if self.position == position_food:
            return True
        
        self.body.pop()
        return False

    def check_collision(self):
        if self.position[0] > (self.screen_size[0]-10) or self.position[0] < 0:
            return True
        
        if self.position[1] > (self.screen_size[1]-10) or self.position[1] < 0:
            return True
        
        for each_part_body in self.body[1:]:
            if self.position == each_part_body:
                return True
            
        return False
