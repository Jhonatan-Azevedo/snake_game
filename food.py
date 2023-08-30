
import random

class Food:
    def __init__(self, screen_size=(300, 400)):
        self.screen_size = screen_size
        self.position = [
                random.randrange(10, self.screen_size[0], 10),
                random.randrange(10, self.screen_size[1], 10)
                ]
        self.already_ate = False

    def generate_new_food(self):
        if self.already_ate: 
            self.position = [
                random.randrange(10, self.screen_size[0], 10),
                random.randrange(10, self.screen_size[1], 10)]
            self.already_ate = False

        return self.position