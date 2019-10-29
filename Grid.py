import settings
from GridCell import GridCell
from Creature import Creature
import random


class Grid:
    """Defines the grid and primary logic of the program"""

    def __init__(self):
        """Initializes the grid according to settings found in settings.py"""

        self.grid = [
            [GridCell(x,
                      y,
                      settings.FOOD_CHANCE * 100 > random.randint(0, 100)) for y in range(settings.Y_SIZE)
             ] for x in range(settings.X_SIZE)
        ]

        self.creaturePopulation = [settings.NUM_CREATURES]
        self.predatorPopulation = [settings.NUM_PREDATORS]

        self.creatures = [Creature(random.randint(0, settings.X_SIZE - 1), random.randint(0, settings.Y_SIZE - 1)) for x in range(settings.NUM_CREATURES)]
        self.predators = [Creature(random.randint(0, settings.X_SIZE - 1), random.randint(0, settings.Y_SIZE - 1), True) for x in range(settings.NUM_PREDATORS)]
        for creature in self.creatures:
            self.grid[creature.xPos][creature.yPos].creatures.append(creature)

    def advance_time(self):
        """Advances the time by length specified in settings"""

        newCreatures = []
        for i in range(settings.DAY_LENGTH):
            random.shuffle(self.creatures)  # Make sure creatures are randomized, no one creature gets an advantage
            for creature in self.creatures:
                dir = random.randint(0, 4)
                self.remove_creature_from_grid(creature)
                if dir == 0:
                    creature.xPos = creature.xPos - 1 if creature.xPos - 1 >= 0 else 1
                elif dir == 1:
                    creature.yPos = creature.yPos + 1 if creature.yPos + 1 < settings.Y_SIZE else settings.Y_SIZE - 2
                elif dir == 2:
                    creature.xPos = creature.xPos + 1 if creature.xPos + 1 < settings.X_SIZE else settings.X_SIZE - 2
                elif dir == 3:
                    creature.yPos = creature.yPos - 1 if creature.yPos - 1 >= 0 else 1
                self.grid[creature.xPos][creature.yPos].creatures.append(creature)
                if self.grid[creature.xPos][creature.yPos].food:
                    creature.food += 1
                    if creature.food > settings.MAXIMUM_FOOD:
                        creature.food = settings.MAXIMUM_FOOD
                    self.grid[creature.xPos][creature.yPos].food = False
                # others = self.another_creature_on_spot(creature.xPos, creature.yPos)
                others = self.grid[creature.xPos][creature.yPos].creatures
                if settings.SEXUAL_REPRODUCTION and len(others) > 0 and creature.age > settings.NON_SEXUAL_AGE_MIN and creature.age < settings.NON_SEXUAL_AGE_MAX:
                    newCreatures.append(Creature(creature.xPos, creature.yPos, False, 1))
        for creature in self.creatures:
            creature.food -= 1
            if creature.food == 0:
                self.remove_creature_from_grid(creature)
                self.creatures.remove(creature)
                continue
            elif random.randint(0, 100) > 100 - 0.75 ** creature.age:
                self.remove_creature_from_grid(creature)
                self.creatures.remove(creature)
                continue
            creature.age += 1
            if not settings.SEXUAL_REPRODUCTION and creature.age > settings.NON_SEXUAL_AGE_MIN and creature.age < settings.NON_SEXUAL_AGE_MAX:
                self.creatures.append(Creature(creature.xPos, creature.yPos, False, 2))
        self.creaturePopulation.append(len(self.creatures))
        self.creatures = self.creatures + newCreatures
        self.print_creatures(True)
        for x in self.grid:
            for y in x:
                y.food = settings.FOOD_CHANCE * 100 > random.randint(0, 100)

    def remove_creature_from_grid(self, creature):
        """Remove a creature"""

        for grid_creature in self.grid[creature.xPos][creature.yPos].creatures:
            if grid_creature.id == creature.id:
                self.grid[creature.xPos][creature.yPos].creatures.remove(grid_creature)

    def another_creature_on_spot(self, x, y):
        """Return other creatures on the given square"""

        ret = []
        for creature in self.creatures:
            if creature.xPos == x and creature.yPos == y:
                ret.append(creature)
        return ret

    def print_food(self):
        """Print out all the cells food info to cout"""

        for x in self.grid:
            print([y.food for y in x])

    def print_creatures(self, num_only=False):
        """Print out a list of creatures and their locations"""

        print("There are %d creatures" % len(self.creatures))

        if not num_only:
            for creature in self.creatures:
                print("X: %d  Y: %d Food: %d  Age: %d" % (creature.xPos, creature.yPos, creature.food, creature.age))