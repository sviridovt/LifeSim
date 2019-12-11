import settings
import random

class Creature:
    """Creature class defines information about a creature"""

    def __init__(self, xPos: int, yPos: int, isPredator = False, food=1):
        """Initialize a creature

        int xPos = x position of the creature, must be less than X_SIZE
        int yPos = y position of the creature, must be less than Y_SIZE
        bool isPredator = is the creature a predator
        """

        if xPos >= settings.X_SIZE or yPos >= settings.Y_SIZE:
            raise ValueError("xPos/yPos cannot be larger than X/Y_SIZE!")
        self.xPos = xPos
        self.yPos = yPos
        self.isPredator = isPredator
        self.id = random.randint(0, 1000000)
        self.food = food
        self.age = 0
        self.bred = settings.MAXIMUM_BABIES


    def set_new_location(self, xPos, yPos):
        """Set a new location for the creature"""

