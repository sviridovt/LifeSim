import settings

class GridCell:
    """Grid cell object used to store information about the position"""

    def __init__(self, xPos: int, yPos: int, food=False):
        """Establish initial information about the creature

        int xPos = X position of the cell, must be less than X_SIZE
        int yPos = Y Position of the cell, must be less than Y_SIZE
        bool food = whether or not food exists in this cell
        """
        if xPos >= settings.X_SIZE or yPos >= settings.Y_SIZE:
            raise ValueError("xPos/yPos cannot exceed maximum")
        self.xPos = xPos
        self.yPos = yPos
        self.food = food
        self.creatures = []